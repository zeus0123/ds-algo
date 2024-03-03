    from openai import OpenAI 
    ################## Function to get caption insights ##############################
    ######### Function call is get_social_media_insights(advisor=[advisor hash email])

    def get_social_media_insights(insight_columns=['custom_text_sentiment', 'custom_text_length',
       'number_of_hashtags','created_hr','created_day'],advisor=None):
        """
        Returns : Two dictionaries , new_dict includes all the caption insights on 'custom_text_sentiment', 'custom_text_length',
       'number_of_hashtags','created_hr','created_day' and openai_insights includes only the caption inisghts that are used by Open AI API Call
        """
    
    
        def apply_mapping(value, mapping_dict):
            for key, (min_val, max_val) in mapping_dict.items():
                if min_val <= value <= max_val:
                    return key
        return "No Mapping Found"
    
    ################################# Read file given to you on email here #######################################

    all_data = pd.read_csv("s3://tw-sagemaker-notebooks/research/algos/openai/social_engagements_processed.csv")
    if advisor is None:
        agg_data = all_data
    else:
        agg_data = all_data[all_data.advisor_email == advisor]
        
    suggestion_dict = dict.fromkeys(insight_columns)



    for col in insight_columns:
        temp=agg_data.groupby(col)['article_click_count'].sum().reset_index().sort_values(by='article_click_count',ascending=False)  
        if temp.shape[0] > 5:
            temp = temp.head(5)
        
        if col in ['created_hr','created_day']:
            suggestion_dict[col] = list(temp[col])
        else:
            suggestion_dict[col] = temp[col].mean()

    custom_text_length_mapping = {'Less than 25 words':[0,25],
                                    'Between 25-50 words':[25,50],
                                    '50-100 words':[50,100],
                                    'More than 100 words but still readable':[100,10**5]}
    custom_text_sentiment_mapping = {'Keep it Simple':[-1,0.1],
                                    'Make the tone slightly positive':[0.1,0.5],
                                    'Tone should be super exciting and optimistic':[0.5,10]}
    number_of_hashtags_mapping = {'Less than 2 hashtags':[0,2],
                                 '2-5 Hashtags': [2,5],
                                 'More than 5 hashtags but still readable':[5,50]}
            
    new_dict = {}    
    for key, value in suggestion_dict.items():
        if key == 'custom_text_sentiment':
            new_dict['caption sentiment'] = apply_mapping(value, custom_text_sentiment_mapping)
        elif key == 'custom_text_length':
            new_dict['caption length'] = apply_mapping(value, custom_text_length_mapping)
        elif key == 'number_of_hashtags':
            new_dict['number of hashtags in caption'] = apply_mapping(value, number_of_hashtags_mapping)
        else:
            new_dict[key] = value
    openai_insights = {key: new_dict[key] for key in ['caption sentiment', 'caption length',
       'number of hashtags in caption']}
   
             
    return new_dict,openai_insights

######################### New Open AI Model that takes in open_ai_insights from above , custom_text,summary & title from the caption typed by advisor ###########

Prompt = f"""Write editing suggestions in the form of a list for
                    social media post caption,strictly according 
                    to the recommendation given to you on parameters like: number of words,
                    number of hashtags and sentiment of text.
                    Here's the recommendation on parameters:{open_ai_insights}
                    Here's the caption: {custom_text}
                    Use the Summary and Title of the article attached to the post for context clues to suggest 
                    better edits for the caption.
                    Summary: {summary}
                    Title : {title}
                    Rules to follow while giving suggestions:
                    1. Make sure that your suggestion are not more than 4 bullet points. One for each parameter, and the 
                    last one an example caption that follows all the recommendations you have listed previusly.
                    2. Always explain your suggestions concisely
                    3. Give examples with each suggestion, you can also edit the caption for the user when necessary.
                    4. Do not clash your suggestions , the user should not be left confused with opposite suggestions
                    5. Each suggestion should be always one bullet point and one line only
                    Your output should always follow the format of:
                    1. Sugestion 1 , Example
                    2. Suggestion 2, Example 
                    3. Suggestion 3, Example
                    4. Example caption"""
        
        start = time.time()

        response = client.completions.create(
        model="gpt-3.5-turbo-instruct",
        prompt=Prompt,
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
        )

        print(response.choices[0].text)