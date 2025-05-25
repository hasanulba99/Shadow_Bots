import openai
from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

class AIMLNewsBot:
    def __init__(self):
        self.model = "gpt-3.5-turbo"

    def answer_question(self, question, context):
        prompt = f"""
You are an expert AI/ML news assistant. Based on the following summarized articles, answer the user's question:

{context}

Question: {question}
Answer:
"""
        try:
            response = openai.ChatCompletion.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": "You are an expert in summarizing and interpreting AI/ML news."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.5,
                max_tokens=300
            )
            return response['choices'][0]['message']['content'].strip()
        except Exception as e:
            return f"Sorry, I couldn't process your request. ({str(e)})"
