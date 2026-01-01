import requests

API_KEY =  " HS4MLG23HB491YKZ"

api_url = "https://www.alphavantage.co/"

symbol = "IBM"
query = f"query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={API_KEY}"
print (api_url+query)

def stock_market_data():
    respone = requests.get(url=api_url+query)
    print(respone.json())

stock_market_data()
