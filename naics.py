from typing import Dict, List
from collections import namedtuple

import pandas as pd
import numpy as np
import spacy

nlp = spacy.load('en_core_web_lg')

CompanyInfo = namedtuple('CompanyInfo', ['Address', 'CompanyDUNSNumber', 'CorporateName', 'EmployeesOnSite', 'Latitude', 'Longitude', 'NAICS1', 'NAICS1Name', 'NAICS2', 'NAICS2Name',
                                         'PointofContact', 'PublicOrPrivate', 'SIC1', 'SIC1Name', 'SIC2', 'SIC2Name', 'SalesVolume', 'Telephone', 'Title', 'TotalEmployees', 'TradestyleName', 'YearStarted'])

company_infos: List[CompanyInfo] = []

for tup in pd.read_excel('NAICSData.xlsx').itertuples(name='CompanyInfo', index=False):
    company_infos.append(tup)

cross_references: Dict[int, spacy.tokens.doc.Doc] = {}

for tup in pd.read_excel('2017_NAICS_Cross_References.xlsx').itertuples():
    cross_references[tup.Code] = nlp(tup.CrossReference)
