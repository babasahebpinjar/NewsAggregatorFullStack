import transformers
from transformers import pipeline
#from transformers import pipeline
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import requests
import streamlit as st
import requests


classifier = None
tokenizer = AutoTokenizer.from_pretrained("mrm8488/distilroberta-finetuned-financial-news-sentiment-analysis")
model = AutoModelForSequenceClassification.from_pretrained("mrm8488/distilroberta-finetuned-financial-news-sentiment-analysis")
classifier = pipeline("sentiment-analysis", model = model, tokenizer = tokenizer)
weightageList = []


#def newsapi(params): 
def newsapi(stockName,date):    
    url = "https://newsapi.org/v2/everything"
    params = {
        "q": stockName,#Apple
        "from": date,
        "sortBy": "popularity",
        "apiKey": "e57cdb6ec34943ea8917c0e520fce4cc"
    }
    val = []
    # Send the GET request
    response = requests.get(url, params=params)    
    request_url = requests.Request('GET', url, params=params).prepare().url
    info = "Fetching news articles for : " + request_url
    st.subheader("News Articles")
    st.info(info)
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Process the response data (in JSON format)
        data = response.json()
        
        # Extract and print the articles
        articles = data.get("articles", [])
        for article in articles:
            description = article.get("description", "")
            val.append(description)
            print(val)
    else:
        print(f"Request failed with status code: {response.status_code}")

    st.write(val)
    return val



def calculate_average(lst):
    if len(lst) == 0:
        return 0  # Return 0 if the list is empty to avoid division by zero error
    else:
        return sum(lst) / len(lst)


def generateSentiment(stockName,date):
    global classifier
    print("Calculatin Sentiment for : ", stockName)
    newsList = newsapi(stockName,date)
    #newsList = ['Amid a bunch of new products']

    for news in newsList:        
        results = classifier(news)         
        sentimentVal = round(results[0]['score'] * 10, 2)   
        print(sentimentVal)                                                                                                                                             
        weightageList.append(sentimentVal)

    return calculate_average(weightageList)
    

st.title("Financial News Sentiment Analysis")

# Create the main content of the app
stock_name = st.text_input("Enter the stock name:")
date = st.text_input("Enter the date in the following format : YYYY-MM-DD")
if st.button("Generate Sentiment"):
    if stock_name:
        sentiment = generateSentiment(stock_name,date)
        st.write("The sentiment is : " + str(sentiment))
        #generate_sentiment(stock_name)
    else:
        st.warning("Please enter a stock name.")

# Add a section to display the news articles (optional)
# You can modify this section according to your needs
# st.subheader("News Articles")
# news_endpoint = "/newsapi"

# def get_news_articles(stock_name):
#     params = {"stockName": stock_name}
#     st.info("Fetching news articles...")
    #st.write("Hello")
    # response = requests.get(base_url + news_endpoint, params=params)
    # if response.status_code == 200:
    #     articles = response.json()
    #     for article in articles:
    #         st.write(article)
    
    #else:
    #    st.error("Failed to fetch news articles.")

# if stock_name:
#     #st.info("Fetching news articles...")
#     newsapi(stock_name)
