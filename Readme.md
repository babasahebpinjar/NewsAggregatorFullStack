# Financial News Sentiment Analysis App

This is a Streamlit app for analyzing the sentiment of financial news articles related to a specific stock. The app utilizes the transformers library for sentiment analysis and the News API for fetching news articles.

Setup
To run this app, make sure you have the following dependencies installed:

transformers
streamlit
requests

You can install the dependencies by running the following command:


pip install transformers streamlit requests

# Usage
# Clone the GitHub repository:

git clone <repository_url>

# Change to the project directory:

cd <project_directory>

# Run the Streamlit app:

streamlit run app.py

or 

if you want to run it in docker

docker build -t financial-news-sentiment .
docker run -p 8501:8501 financial-news-sentiment

# The app will launch in your web browser on Port 8501

Functionality

Enter the stock name and the date in the specified format (YYYY-MM-DD).
Click the "Generate Sentiment" button to analyze the sentiment of financial news articles related to the specified stock.

The app will fetch news articles using the News API and display their descriptions.
The sentiment analysis is performed on each news article using a pre-trained sentiment classification model (mrm8488/distilroberta-finetuned-financial-news-sentiment-analysis).
The average sentiment score is calculated based on the sentiment of the news articles.
The app displays the calculated sentiment score.
Note: You need to provide your own News API key to fetch news articles. Replace the "apiKey" value in the newsapi function with your API key.

Feel free to customize the app according to your needs by modifying the code in the app.py file.

Acknowledgments
This app utilizes the transformers library developed by Hugging Face for natural language processing tasks.
The sentiment classification model used in this app is provided by mrm8488 and is based on the DistilRoBERTa architecture.
News articles are fetched using the News API.

