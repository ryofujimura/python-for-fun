import json, requests

def get_stock_price():
    url = 'https://query2.finance.yahoo.com/v10/finance/quoteSummary/tsla?modules=price'
    response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    # print(response.text)
    data = json.loads(response.text)
    return data

def marketprice(data):
    print(data['quoteSummary']['result'][0]['price']['regularMarketPrice']['raw'])

def main():
    data = get_stock_price()
    # print(get_stock_price())
    marketprice(data)

if __name__ == '__main__':
    main()