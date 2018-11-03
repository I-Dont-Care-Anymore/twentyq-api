from bs4 import BeautifulSoup
from flask import Flask
import requests
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

page = requests.get("https://www.naics.com/company-profile-page/?co=111")
soup = BeautifulSoup(page.content, 'html.parser')

desired = soup.find('table',  class_='companyDetail topCompanyDetail')
cells = list(desired.children)

compDUNS, corpName, tradeName, POC, title, addr, tele, totEmp, empSite, sales, pub, lat = []
long, nics1, nics1Name, nics2, nics2Name, sic1, sic1Name, sic2, sic2Name = []

compDUNS.append((cells[0].get_text())[15:])      # Company DUNS#:

cutoff = (cells[1].get_text()).index("Tradestyle Name: ")
corpName.append((cells[1].get_text())[16:cutoff])      # Corporate Name:
cutoff = cutoff + 17

tradeName.append((cells[1].get_text())[cutoff:])  # Tradestyle Name:

cutoff = (cells[2].get_text()).index("Title: ")
POC.append((cells[2].get_text())[18:cutoff])      # Point of Contact:
cutoff = cutoff + 7

title.append((cells[2].get_text())[cutoff:])  # Title:

addr.append((cells[3].get_text())[9:])       # Address:

tele.append((cells[4].get_text())[11:])      # Telephone:

cutoff = (cells[5].get_text()).index("Employees On Site: ")
totEmp.append((cells[5].get_text())[17:cutoff])      # Total Employees:
cutoff = cutoff + 19
empSite.append((cells[5].get_text())[cutoff:])  # Employees on Site:

sales.append((cells[6].get_text())[14:])      # Sales Volume:

cutoff = (cells[7].get_text()).index("Year Started: ")
pub.append((cells[7].get_text())[16:cutoff])      # Public/Private:
cutoff = cutoff + 14

year.append((cells[7].get_text())[cutoff:])       # Year Started:

cutoff = (cells[8].get_text()).index("Longitude: ")
lat.append((cells[8].get_text())[10:cutoff])       # Latitude:
cutoff = cutoff + 11

long.append((cells[8].get_text())[cutoff:])      # Longitude:

nics1.append((cells[9].get_text())[9:15])     # NAICS 1:

nics1Name.append((cells[9].get_text())[15:])      # NAICS 1 Name:

nics2.append((cells[10].get_text())[9:15])    # NAICS 2:

nics2Name.append((cells[10].get_text())[15:])     # NAICS 2 Name:

sic1.append((cells[11].get_text())[7:15])    # SIC 1:

sic1Name.append((cells[11].get_text())[15:])     # SIC 1 Name:

sic2.append((cells[12].get_text())[7:15])    # SIC 2:

sic2Name.append((cells[12].get_text())[15:])     # SIC 2 Name:
    
