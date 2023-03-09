import json

import os
from moderation import Moderation
import requests
import csv

os.environ['HTTP_PROXY'] = "http://localhost:7890"
os.environ['HTTPS_PROXY'] = "http://localhost:7890"

requests_header = {
    'Authorization': 'Bearer TOKEN',
}

cleaned_data_dir = "data/cleaned_data"
cleaned_data_files = []

for _ in os.listdir(cleaned_data_dir):
    if _.endswith(".csv"):
        cleaned_data_files.append(_)

for _ in cleaned_data_files:
    with open(os.path.join(cleaned_data_dir, _), "r", encoding="utf8") as r:
        reader = csv.reader(r)
        for line in reader:
            try:
                text = line[0]
                input_data = {'input': text}
                response = requests.post("https://api.openai.com/v1/moderations", headers=requests_header,
                                         json=input_data)
                results = json.loads(response.text)['results'][0]
                moderation = Moderation(text,
                                        results['category_scores']['hate'],
                                        results['category_scores']['hate/threatening'],
                                        results['category_scores']['self-harm'],
                                        results['category_scores']['sexual'],
                                        results['category_scores']['sexual/minors'],
                                        results['category_scores']['violence'],
                                        results['category_scores']['violence/graphic'],
                                        results['categories']['hate'], results['categories']['hate/threatening'],
                                        results['categories']['self-harm'],
                                        results['categories']['sexual'], results['categories']['sexual/minors'],
                                        results['categories']['violence'],
                                        results['categories']['violence/graphic'],
                                        results['flagged'])
                moderation.insert_to_db()
                # print(results)
                print("success query text moderation result")
            except Exception:
                print("failed query text moderation result")
            print("--------------")
