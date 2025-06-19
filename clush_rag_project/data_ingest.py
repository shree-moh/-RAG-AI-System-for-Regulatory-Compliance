import json

def load_cases(json_file):
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data

def extract_texts(data):
    return [entry['text'] for entry in data]
