import json

config = None

with open('config.json', 'r') as f:
    config = json.load(f)

def getConfig():
    return config