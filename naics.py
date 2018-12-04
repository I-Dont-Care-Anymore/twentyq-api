from typing import Dict, List
from collections import namedtuple

import pandas as pd
import numpy as np

import spacy
from spacy.tokens import Doc
from spacy.vocab import Vocab
spacy.prefer_gpu()
spacy.cli.download('en_core_web_sm')
nlp = spacy.load('en_core_web_sm')

# Representation of what entries in the CompanyInfo list look like
CompanyInfo = namedtuple('CompanyInfo', ['Address', 'CompanyDUNSNumber', 'CorporateName', 'EmployeesOnSite', 'Latitude', 'Longitude', 'NAICS1', 'NAICS1Name', 'NAICS2', 'NAICS2Name',
                                         'PointofContact', 'PublicOrPrivate', 'SIC1', 'SIC1Name', 'SIC2', 'SIC2Name', 'SalesVolume', 'Telephone', 'Title', 'TotalEmployees', 'TradestyleName', 'YearStarted'])

# Company info list
company_infos: List[CompanyInfo] = []

for tup in pd.read_excel('NAICSData.xlsx').itertuples(name='CompanyInfo', index=False):
    company_infos.append(tup)

names: Dict[int, str] = {}
definitions: Dict[int, Doc] = {}

for tup in pd.read_excel('2017_NAICS_Descriptions.xlsx').itertuples():
    if len(str(tup.Code)) != 6:
        continue
    names[tup.Code] = tup.Title
    definitions[tup.Code] = Doc(nlp.vocab).from_disk(f'naics/{tup.Code}.sdoc')
