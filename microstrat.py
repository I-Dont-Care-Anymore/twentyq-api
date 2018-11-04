import stocklookup
import requests
import json
from mstrio import microstrategy

URL = 'https://env-113279.customer.cloud.microstrategy.com/MicroStrategyLibrary/api'
USER = 'davidlu'
PASS = 'v4ndyhax'
PROJ = 'Relationships Project'

conn = microstrategy.Connection(base_url=URL, username=USER, password=PASS, project_name=PROJ, login_mode=1)

conn.connect()

json_model = {
  "datasetId": "9D61A62C4DF507A115A677AE9CF8F7BB",
  "name": "Finance",
  "tables": [
    {
      "id": "string",
      "name": "string"
    }
  ]
}

# create data model - PASS
response = requests.post(url=conn.base_url + '/datasets/models', headers={'X-MSTR-AuthToken': conn.auth_token, 'X-MSTR-ProjectID': conn.project_id},
                             cookies=conn.cookies,
                             json=json_model,
                             verify=conn.ssl_verify)

print(response)

#stocklookup.loadStocks("Microsoft")