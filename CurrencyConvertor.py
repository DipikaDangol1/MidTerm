import re
import urllib.request
import json

api_endpoint='https://api.exchangerate-api.com/v4/latest/'

def page_exists(page):
	try:
		urllib.request.urlopen(page)
		return True
	except:
		return False

amount = input("Enter amount to be converted (q to quit): ")
if amount == 'q' or amount == 'Q':
    print("Exitting..")
    exit()
try:
    amount = float(amount)
except (TypeError, ValueError):
    print('Invalid amount')
    exit()

fromCurrency = input("Enter FROM currency 3 letter code: ")
if fromCurrency == 'q' or fromCurrency == 'Q':
    print("Exitting..")
    exit()
if len(fromCurrency) != 3:
    print('Invalid FROM currency')
    exit()
if not fromCurrency.isupper():
    print('Invalid FROM currency')
    exit()

toCurrency = input("Enter TO currency 3 letter code: ")
if toCurrency == 'q' or toCurrency == 'Q':
    print("Exitting..")
    exit()
if len(fromCurrency) != 3:
    print('Invalid FROM currency')
    exit()
if not fromCurrency.isupper():
    print('Invalid FROM currency')
    exit()

endpoint = 'https://api.exchangerate-api.com/v4/latest/' + fromCurrency
print(endpoint)

request = urllib.request.urlopen(endpoint)
d = json.load(request)
print(d['rates'][toCurrency] * amount)