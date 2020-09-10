import requests

def getExchangeRate(fromCurrency,toCurrency):
    # fromCurrency="USD"
    # toCurrency="INR"
    url="https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency="+fromCurrency+"&to_currency="+toCurrency+"&apikey=LSMFUIUCI1F12AK5"
    result = requests.get(url)
    result=result.json()
    exchangeRate=result['Realtime Currency Exchange Rate']['5. Exchange Rate']
    exchangeRate = float(exchangeRate)
    return exchangeRate

def takeInput():
    print("---------Welcome to Currency Exchanges!!------------")
    print("Select option:")
    print("1. Go to currency converter")
    print("2. Exit")
    option = int(input("Select option : "))

    if option == 2:
        exit() 
    else:
        print("\neg (INR,USD,JPY etc...)\n")
        fromCurrency=input("From which currency do you want to convert: ")
        toCurrency=input("To which currency do you want to convert: ")
        amount=float(input("Amount: "))
        exchangeRate=getExchangeRate(fromCurrency,toCurrency)
        print(exchangeRate*amount)

takeInput()
