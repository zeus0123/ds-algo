from openai import OpenAI 
import time
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
        if temp.shape[0] > 3:
            temp = temp.head(3)
        
        if col in ['created_hr','created_day']:
            suggestion_dict[col] = list(temp[col])
        else:
            suggestion_dict[col] = temp[col].mean()

    custom_text_length_mapping = {'Less than 25 words':[0,25],
                                    'Between 25-50 words':[25,50],
                                    '50-100 words':[50,100],
                                    '100 or more words but readable':[100,10**5]}
    custom_text_sentiment_mapping = {'Keep it Simple and Neutral':[-1,0.1],
                                    'Slightly positive tone':[0.1,0.5],
                                    'Use positive tone':[0.5,10]}
    number_of_hashtags_mapping = {'0-2':[0,2],
                                 '2-5': [2,5],
                                 '5 or more':[5,50]}
            
   new_dict = []   
    for key, value in suggestion_dict.items():
        if key == 'custom_text_sentiment':
            new_dict.append('caption sentiment adjustment-'+ apply_mapping(value, custom_text_sentiment_mapping))
        elif key == 'custom_text_length':
            new_dict.append('caption length adjustment-'+ apply_mapping(value, custom_text_length_mapping))
        elif key == 'number_of_hashtags':
            new_dict.append('number of hashtags adjustment-'+ apply_mapping(value, number_of_hashtags_mapping))
    suggestion_dict = {key: suggestion_dict[key] for key in ['created_hr','created_day']}
   
             
    return new_dict,openai_insights

######################### New Open AI Model that takes in open_ai_insights from above , custom_text,summary & title from the caption typed by advisor ###########

client = OpenAI(api_key =[API_KEY])

Prompt = f"""You are a social media post caption writer and have received some edit remarks. Your goal is to provide suggestions for the caption while adhering to the given principles. Return your suggestion as a list
Use the following principles while responding:
1.Your suggestions must not change meaning of caption.
2.Always explain your suggestion with an example.
3.Each suggestion should be less than 2 sentences.
4.Your output should always have a suggestion caption which includes all the suggestions and then 3 bullet points each for the edit remarks.
6.Given remarks, adjust the caption's sentiment, length, and number of hashtags. If the current caption is below the recommended range, add context accordingly. If within the range, enhance impact; if exceeding, make it more direct. Also, optimize hashtags and remove redundant words with this logic.
Example -
Input Caption: Weekly Newsletter - Difficult time ahead this quarter
Input Edit remarks: caption sentiment adjustment : Slightly positive tone , caption length adjustment: 10-20 words,number of hashtags in caption: 5-10.
Formatted Output -
Suggested Caption: Here's what to expect this quarter and things you can do in these challenging times #budgeting #financialwellness #easyfinance

1. Try adding  positive and optimistic connotation to your caption, like you can change "Difficult times" to "Challenging times".

2. You can try adding more information in your caption to make it lucid and also captivate your audience , like "Coming up this quarter".

3. Adding hashtags will increase the visisbility , you can try adding #budgeting #financialwellness #quarternews #finaneweekly #newsletter etc.
Now suggest edits for the following caption with given edit remarks:
Edit remarks: {openai_insights}
Current caption: {custom_text}
Summary:{summary}
Title : {title}
Response starts here -"""
        
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
end = time.time()

print(response.choices[0].text, "Time taken", end-start)
