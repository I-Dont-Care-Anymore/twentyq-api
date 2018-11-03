import requests
import json
import sys

apikey = 'SHDI00MDI69UUBY7'

def stockLookup(query):
    url = 'https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY&symbol=' + query +'&apikey=' + apikey #+ '&datatype=csv'
    data = requests.get(url)
    try:
        return json.loads(data.text)
    except ValueError:
        print("Decoding JSON has failed")

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


def loadStocks(company):
    dates = []
    open = []
    high = []
    low = []
    close = []
    volume = []
    data = stockLookup(symbolLookup(company))
    metadata = data["Meta Data"]
    timeSeries = data["Monthly Time Series"]
    #for i in range(0, 250):
     #   print(timeSeries[i].title)
    #timeSeries = sorted(timeSeries)
    for i in timeSeries:
        dates.append(i)
        open.append(timeSeries[i]['1. open']) 
        high.append(timeSeries[i]['2. high'])
        low.append(timeSeries[i]['3. low'])
        close.append(timeSeries[i]['4. close'])
        volume.append(timeSeries[i]['5. volume'])
    print(open)

loadStocks("Microsoft")