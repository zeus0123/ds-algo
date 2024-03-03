import io
import json
import os
import string

import boto3
import numpy
import pandas


def apply_mapping(value, mapping_dict):
    for key, (min_val, max_val) in mapping_dict.items():
        if min_val <= value <= max_val:
            return key
    return "No Mapping Found"


def lambda_handler(event, context):
    
    s3client=boto3.client(service_name='s3')
    
    advisor = event['rawQueryString'].split("=")
    
    if len(advisor) == 1 :
        response = s3client.get_object(Bucket='tw-sagemaker-notebooks', Key='research/algos/engagement/content_performance_train_10_23.csv')
        content_data = pandas.read_csv(io.BytesIO(response['Body'].read()))
    else:
        response = s3client.get_object(Bucket='tw-sagemaker-notebooks', Key='research/algos/engagement/advisor_content_performance_train_10_24.csv')
        content_data = pandas.read_csv(io.BytesIO(response['Body'].read()))
        content_data = content_data[content_data.advisor_email == advisor[1]]

    insight_columns=['theme_name','created_hr', 'created_day', 'article_type', 'article_format','subject_number_of_words', 'subject_sentiment', 
       'sentiment_body', 'length_of_body', 
       'image_number']

        
    suggestion_dict = dict.fromkeys(insight_columns)
    suggested_dict_ranking = dict.fromkeys([key+"_ranked" for key in insight_columns])
    # current_date = pd.to_datetime('today')
    # current_month = content_data[content_data['created_month']==current_date.month_name()]

    for col in insight_columns:
        temp=content_data.groupby(col)['total_clicks'].sum().reset_index().sort_values(by='total_clicks',ascending=False)
       
        if col in ['theme_name','subject_number_of_words', 'subject_sentiment', 'sentiment_body', 'length_of_body', 'image_number']:
            temp = temp.head(5)
        temp['weight'] = temp['total_clicks']/temp['total_clicks'].sum() 
        suggestion_dict[col] = list(temp[col])
        suggested_dict_ranking[col+"_ranked"] = list(temp['weight'])
        
        
    for key,value in suggestion_dict.items():
        if key in ['subject_number_of_words','subject_sentiment','subject_ner','subject_number_exclamation','subject_number_question','sentiment_body',
               'length_of_body','number_of_orgs','body_number_of_exclamation','body_number_of_question','image_number']:
            suggestion_dict[key] = numpy.median(numpy.array(value))
            

    sentiment_mappings= { 'Simple and Straight forward':[0,0.1],
    'Positive and Exciting':[0.1,0.7],
    }
    subject_number_of_words_mappings= {'Short and Direct':[0,5],
    'Medium length with relevant information':[5,10],
    'As much information as possible':[10,50]}

    subject_ner_mappings = {'Add organization names in your subject line':[1,10]}
    
    subject_number_exclamation_mapping = {'Add some excitement to the subject line':[1,4]}
    
    subject_number_question_mapping = {'Make your subject line inquisitive':[1,4]}
    
    length_of_body_mapping = {'Quick and Short':[0,100],
    'Informative yet brief':[100,500],
    'Lengthy and Descriptive':[500,1000],
    'Longer the better':[1000,2000]}

    body_number_of_orgs={"Don't make it more complex by adding organization,company or people names":[0,3],
    'Try to add some organization,people and places when possible':[3,15]}
    
    body_number_of_question_mappings = {'No need to make it more complicated with questions':[0,1],
    'Inquisitive is better':[1,5]
    }
    
    body_number_of_exclamation_mappings = {'Excitinga and fun':[1,5]
    }
    
    img_number_mappings={'Only text':[0,2],
    'Make it pictorial':[2,18]}
    
    new_dict = {}
    for key, value in suggestion_dict.items():
        if key == 'subject_sentiment' or key == 'sentiment_body':
            new_dict[key] = apply_mapping(value, sentiment_mappings)
        elif key == 'subject_number_of_words':
            new_dict[key] = apply_mapping(value, subject_number_of_words_mappings)
        elif key == 'subject_number_exclamation':
            new_dict[key] = apply_mapping(value, subject_number_exclamation_mapping)
        elif key == 'subject_ner':
            new_dict[key] = apply_mapping(value, subject_ner_mappings)
        elif key == 'subject_number_question':
            new_dict[key] = apply_mapping(value, subject_number_question_mapping)
        elif key == 'length_of_body':
            new_dict[key] = apply_mapping(value, length_of_body_mapping)
        elif key == 'number_of_orgs':
            new_dict[key] = apply_mapping(value, body_number_of_orgs)
        elif key == 'body_number_of_exclamation':
            new_dict[key] = apply_mapping(value, body_number_of_exclamation_mappings)
        elif key == 'body_number_of_question':
            new_dict[key] = apply_mapping(value, body_number_of_question_mappings)
        elif key == 'image_number':
            new_dict[key] = apply_mapping(value, img_number_mappings)
        else:
            new_dict[key] = value
    
    
            
    return json.dumps([new_dict,suggestion_dict, suggested_dict_ranking])