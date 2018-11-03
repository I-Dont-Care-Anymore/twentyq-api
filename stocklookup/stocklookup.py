
import requests
import json


query = 'microsoft'
url = 'http://d.yimg.com/autoc.finance.yahoo.com/autoc?query=' + query +'&region=1&lang=en&callback=YAHOO.Finance.SymbolSuggest.ssCallback''
data = requests.get(url)
results = json.loads(data.text)
for result in results:
    if result["symbol"]:
        print(result)