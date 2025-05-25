from transformers import pipeline

class NewsSummarizer:
    def __init__(self, model_name="Falconsai/text_summarization"):
        self.summarizer = pipeline("summarization", model=model_name)

    def summarize(self, text):
        if len(text) < 50:
            return text
        return self.summarizer(text[:1024], max_length=120, min_length=30, do_sample=False)[0]['summary_text']
