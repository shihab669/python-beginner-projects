import requests

API = "https://v6.exchangerate-api.com/v6/2d859472b3eb018f5f2281db/latest/USD"

response = requests.get(API)

# Will work later 