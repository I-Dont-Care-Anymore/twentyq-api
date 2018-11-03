import requests
import json

apikey = 'SHDI00MDI69UUBY7'

def stockLookup(query):
    url = 'https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY&symbol=' + query +'&apikey=' + apikey
    data = requests.get(url)
    print(data.text)

def symbolLookup(query):
    url = 'http://d.yimg.com/autoc.finance.yahoo.com/autoc?query=' + query +'&region=1&lang=en&callback=YAHOO.Finance.SymbolSuggest.ssCallback'
    data = requests.get(url)
    dataText = data.text[39: -2]
    try:
        results = json.loads(dataText)
        resultset = results["ResultSet"]
        resultTable = resultset["Result"]
        #print (resultTable[0]["symbol"])
        return resultTable[0]["symbol"]
    except ValueError:
        print("Decoding JSON has failed")
    return None


stockLookup(symbolLookup('Microsoft'))
