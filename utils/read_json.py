import json

def load_json():
    with open("test_data/login_data.json", "r") as file:
        return json.load(file)