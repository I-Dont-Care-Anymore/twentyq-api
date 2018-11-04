# import stocklookup
import requests
import json
from mstrio import microstrategy

URL = 'https://env-113279.customer.cloud.microstrategy.com/MicroStrategyLibrary/api'
USER = 'davidlu'
PASS = 'v4ndyhax'
PROJ = 'Relationships Project'

#conn = microstrategy.Connection(base_url=URL, username=USER, password=PASS, project_name=PROJ, login_mode=1)

#conn.connect()

#json_model = {
#  "datasetId": "9D61A62C4DF507A115A677AE9CF8F7BB",
#  "name": "Finance",
#  "tables": [
#    {
#      "id": "string",
#      "name": "string"
#    }
#  ]
#}

# create data model - PASS
#response = requests.post(url=conn.base_url + '/datasets/models', headers={'X-MSTR-AuthToken': conn.auth_token, 'X-MSTR-ProjectID': conn.project_id},
                             #cookies=conn.cookies,
                             #json=json_model,
                             #verify=conn.ssl_verify)

#print(response)

#stocklookup.loadStocks("Microsoft")


#################################################################################

response = (requests.post('https://env-113279.customer.cloud.microstrategy.com/MicroStrategyLibrary/api/auth/login', data = { 
  "username": "davidlu",
  "password": "v4ndyhax",
  "loginMode": 1,
  "maxSearch": 3,
  "workingSet": 0,
  "changePassword": "false",
  "newPassword": "string",
  "metadataLocale": "en_us",
  "warehouseDataLocale": "en_us",
  "displayLocale": "en_us",
  "messagesLocale": "en_us",
  "numberLocale": "en_us",
  "timeZone": "UTC",
  "applicationType": 35} )) 
authToken = response.headers['X-MSTR-AuthToken']
cookies = dict(response.cookies)
print(response.headers)

response = (requests.get('https://env-113279.customer.cloud.microstrategy.com/MicroStrategyLibrary/api/sessions', headers = {
  'X-MSTR-AuthToken' : authToken
  })) 
print(response.content)

response = (requests.put('https://env-113279.customer.cloud.microstrategy.com/MicroStrategyLibrary/api/sessions', headers = {
  'X-MSTR-AuthToken' : authToken
  })) 
print(response.content)

response = (requests.get('https://env-113279.customer.cloud.microstrategy.com/MicroStrategyLibrary/api/sessions/privileges', headers = {
  'X-MSTR-AuthToken' : authToken
  })) 
print(response.content)


response = (requests.get('https://env-113279.customer.cloud.microstrategy.com/MicroStrategyLibrary/api/projects', headers = {
  'X-MSTR-AuthToken' : authToken
  })) 

print(response)

response = (requests.post('https://env-113279.customer.cloud.microstrategy.com/MicroStrategyLibrary/api/auth/logout', headers = {
  'X-MSTR-AuthToken' : authToken
  })) 
print(response)

#response = (requests.get('https://env-113279.customer.cloud.microstrategy.com/MicroStrategyLibrary/api/sessions/projectId', headers = { 
 # 'X-MSTR-AuthToken' : authToken,
 # 'X-MSTR-ProjectID' : 'B3FEE61A11E696C8BD0F0080EFC58F44'} )) 
#projectId, cookies = response.headers['X-MSTR-AuthToken'], dict(response.cookies)
#print(response)

 
#print(response)
