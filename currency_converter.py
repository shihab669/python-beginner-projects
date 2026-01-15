import requests

API = "https://v6.exchangerate-api.com/v6/APIKEY/latest/USD"

response = requests.get(API)

# Will work later on implementing the currency conversion logic