import csv
from datetime import datetime

class CSVManager:
    def __init__(self, filepath='data/news_data.csv'):
        self.filepath = filepath

    def save_news(self, articles):
        with open(self.filepath, mode='a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            for article in articles:
                writer.writerow([
                    datetime.now(), article['title'], article['description'], article['url']
                ])
