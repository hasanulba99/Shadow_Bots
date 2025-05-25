import requests
from config import NEWS_API_KEY

class NewsFetcher:
    def fetch_news(self):
        params = {
            'q': "Artificial Intelligence OR Machine Learning",
            'apiKey': NEWS_API_KEY,
            'language': 'en',
            'pageSize': 10
        }
        try:
            response = requests.get("https://newsapi.org/v2/everything", params=params, timeout=10)
            data = response.json()
            return data.get('articles', [])
        except requests.exceptions.RequestException as e:
            import streamlit as st
            st.warning(f"Failed to fetch news: {e}")
            return []
