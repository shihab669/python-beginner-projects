import requests

def info():
    while True:
        baseCurrency = input("Please enter the base currency (Example 'USD'): ").strip().upper()
        targetCurrency = input("Please enter the target currency (Example 'BDT'): ").strip().upper()

        try:
            amount = float(input("Please enter the amount: "))
        except ValueError:
            print("Amount must be a number.")
            continue

        if not baseCurrency or not targetCurrency:
            print("Currency codes cannot be empty.")
            continue

        if baseCurrency == targetCurrency:
            print("Base and target currency must be different.")
            continue

        if amount <= 0:
            print("Amount must be greater than zero.")
            continue

        return baseCurrency, targetCurrency, amount


def apiStuff(bcur):
    API = (f"https://v6.exchangerate-api.com/v6/c1b21653832e3b674562427c/latest/{bcur}")
    response = requests.get(API).json()
    return response

def calculation(baseCurrency,targetCurrency, amount, response):

    targetCurrencyRate = response['conversion_rates'].get(targetCurrency)

    mainCalculation = targetCurrencyRate*amount

    print(f'{amount} {baseCurrency} = {mainCalculation} {targetCurrency}')



baseCurrency, targetCurrency, amount = info()

apiEesponse = apiStuff(baseCurrency)

calculation(baseCurrency, targetCurrency, amount, apiEesponse)




