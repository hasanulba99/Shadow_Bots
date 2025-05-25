import streamlit as st
from src.news_fetcher import NewsFetcher
from src.summarizer import NewsSummarizer
from src.csv_manager import CSVManager
from src.chatbot import AIMLNewsBot

fetcher = NewsFetcher()
summarizer = NewsSummarizer("sshleifer/distilbart-cnn-12-6")
csv_manager = CSVManager()
chatbot = AIMLNewsBot()

st.set_page_config(page_title="ShadowBots AI News", layout="wide")
st.title("🧠 ShadowBots AI News - Daily Digest + Assistant")

# Auto-fetch news
with st.spinner("Loading today's AI/ML news..."):
    articles = fetcher.fetch_news()
    summaries = []
    for article in articles:
        text = article['description'] or article['content'] or ""
        summary = summarizer.summarize(text)
        summaries.append({"title": article['title'], "summary": summary, "url": article['url']})

        st.subheader(article['title'])
        st.write(summary)
        st.markdown(f"[Read more]({article['url']})", unsafe_allow_html=True)

    csv_manager.save_news(articles)
    st.success("News loaded and saved!")

# Sidebar chatbot
st.sidebar.title("🤖 AI/ML News Assistant")
user_query = st.sidebar.text_input("Ask me something about today's news:")
if user_query and summaries:
    context = "\n".join([f"{s['title']}: {s['summary']}" for s in summaries])
    answer = chatbot.answer_question(user_query, context)
    st.sidebar.markdown("---")
    st.sidebar.write("**Answer:**")
    st.sidebar.write(answer)
