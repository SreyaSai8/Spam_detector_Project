'''this is for single input testing'''
import requests

url = "http://127.0.0.1:5000/predict"
data = {"post": "Don't miss this chance to earn money fast!"}
response = requests.post(url, json=data)

print(response.json())

'''this is for multiple inputs testing'''

import requests

url = "http://127.0.0.1:5000/predict"

test_cases = [
    "Congratulations! You've won a free recharge.",
    "Let's meet for lunch tomorrow.",
    "Click this link to claim your free reward now!",
    "Hey, how was your weekend?",
    "Win ₹1000 instantly. Tap now!"
]

for i, text in enumerate(test_cases, start=1):
    response = requests.post(url, json={"post": text})
    result = response.json()
    print(f"Test Case {i}:")
    print(f"  Input: {text}")
    print(f"  Label: {result['label']}")
    print(f"  Confidence: {result['confidence']}\n")
