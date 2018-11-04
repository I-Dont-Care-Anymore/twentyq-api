from bs4 import BeautifulSoup
import sys
import requests

import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import numpy as np


for i in range(15, 17) :
    url = "https://clients1.ibisworld.com/reports/us/industry/default.aspx?entid=" + str (i)
    page = requests.get(url)

    if page.url == url:
        continue

    sys.stdout.write(str(i) + " ")
    sys.stdout.flush()

    soup = BeautifulSoup(page.content, 'html.parser')

    desired = soup.find_all("Industry_SupplyChain_KeyEconmicDrivers")

    for p in desired:
        print(p.prettify())
  



