import requests

API_KEY =  " HS4MLG23HB491YKZ"

api_url = "https://www.alphavantage.co/"


def stock_market_data(symbol):
    query = f"query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={API_KEY}"
    response = requests.get(url=api_url+query)
    for i,j in response.json().items():
       if i == "Meta Data":
           print(i,j)
       else:
        continue


symbol = input("Enter the symbol you want for stock market API eg. (AMZN,IBM,GOGL) : ") 
stock_market_data(symbol)
