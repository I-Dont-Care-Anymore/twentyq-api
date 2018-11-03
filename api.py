from flask import Flask
import requests
import sys

import naics

app = Flask(__name__)
 
#@app.route("/")
#def hello():
#   return "Hello World!"
    
#@app.route("/")
#def getInfo():
#   page = requests.get("https://www.naics.com/company-profile-page/?co=795")
#    if page.status_code != 200:
#        return
#    soup = BeautifulSoup(page.content, 'html.parser')
#    print (soup.prettify())
#    return 

#if __name__ == "__main__":
#    app.run()
