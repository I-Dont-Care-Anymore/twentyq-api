import requests
import json
from newsapi import NewsApiClient

#!/usr/bin/python
import hmac
from hashlib import sha1
import urllib


def getRelevantInformation(queryString):
	urls = {}
	article_results = []
	search_results = []

	for v in getRelatedArticles(queryString)["articles"]:
		url_string = v["url"]
		article_results.append({url_string : getSnapshot(url_string)}) 

	for v in getRelatedBingResults(queryString)["webPages"]["value"]:
		url_string = v["url"]
		search_results.append({url_string : getSnapshot(url_string)}) 

	urls['articles'] = article_results[:5]
	urls['searches'] = search_results

	return json.dumps(urls)



def getRelatedArticles(queryString):
	newsapi = NewsApiClient(api_key='f6119036065140a0a53cbd91e483dcd2')

	return newsapi.get_top_headlines(q=queryString,
                                          language='en',
                                          country='us')





def getRelatedBingResults(queryString):
	headers = {"Ocp-Apim-Subscription-Key" : "43e51dfe095442efbd308d0f3e30b0b1"}
	params  = {"q": queryString, "textDecorations":True, "textFormat":"HTML", "count" : 5, "cc" : "en-US"}
	response = requests.get("https://api.cognitive.microsoft.com/bing/v7.0/search", headers=headers, params=params)
	response.raise_for_status()
	return response.json()




def getSnapshot(url, thumb_width = 400):
    argsDict = {'url' : url, 'thumb_width': thumb_width}
    apiKey = "4icq1KiBD5oQNmCv"
    apiSecret = "e773240c41994fd99dc24fd87a54e538"
    queryString = urllib.urlencode(argsDict, True)
    hmacToken = hmac.new(apiSecret, queryString, sha1)
    token = hmacToken.digest().encode('hex')
    return "https://api.urlbox.io/v1/%s/%s/png?%s" % (apiKey, token, queryString)