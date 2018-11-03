from bs4 import BeautifulSoup
import sys
import requests

import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import numpy as np


for i in range(200, 202) :
    url = "https://clients1.ibisworld.com/reports/us/industry/default.aspx?entid=" + str (i)
    page = requests.get(url)

    if page.url == url:
        continue

    soup = BeautifulSoup(page.content, 'html.parser')

    desired = soup.find('div', class_="Industry_SupplyChain")

    print(desired.prettify())



