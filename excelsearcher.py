#import stocklookup.py

import pandas as pd
import openpyxl

def routine(number):
   # data = pd.read_excel("NAICSData.xlsx")

    ##companies = data[data.NAICS1 == number]
    
    ##if()
    #print("Relevant companies".format(
    #len(companies)))

    #start here
    dictionary = {'comp0': None, 'comp1': None, 'comp2': None, 'comp3': None, 'comp4': None, 'comp5': None, 'comp6': None, 'comp7': None, 'comp8': None, 'comp9': None }
    book = load_workbook(filename = "NAICSData.xlsx")
    sheet = book['Sheet1']
    compNum = 0
    for row in range(2, 12500):
        if compNum == 10:
            break
        if (sheet['G' + str(row)].value) == number:
            dictionary['comp' + str(compNum)] = sheet['C' + str(row)]
            dictionary.update({'duns' + str(compNum) : sheet['B' + str(row)]},
                             {'sEmp' + str(compNum) : sheet['D' + str(row)]},
                             {'lat' + str(compNum) : sheet['E' + str(row)]},
                             {'long' + str(compNum) : sheet['F' + str(row)]},
                             {'sales' + str(compNum) : sheet['Q' + str(row)]},
                             {'tEmp' + str(compNum) : sheet['T' + str(row)]},
                             {'year' + str(compNum) : sheet['V' + str(row)]})
            ++compNum
        elif (sheet['I' + str(row)].value) == number:
            dictionary['comp' + str(compNum)] = sheet['C' + str(row)]
            dictionary.update({'duns' + str(compNum) : sheet['B' + str(row)]},
                             {'sEmp' + str(compNum) : sheet['D' + str(row)]},
                             {'lat' + str(compNum) : sheet['E' + str(row)]},
                             {'long' + str(compNum) : sheet['F' + str(row)]},
                             {'sales' + str(compNum) : sheet['Q' + str(row)]},
                             {'tEmp' + str(compNum) : sheet['T' + str(row)]},
                             {'year' + str(compNum) : sheet['V' + str(row)]})
            ++compNum
    book = load_workbook(filename = "audience1.xlsx")
    sheet = book['Sheet1']
    for row in range(2, 26):
        if (sheet['A' + str(row)]) == (str(number))[0:2]:
            dictionary.update({'SUPPLY' : sheet['C' + str(row)]},
                             {'DRIVER' : sheet['D' + str(row)]},
                             {'DEMAND' : sheet['E' + str(row)]},
                             {'sec' : sheet['B' + str(row)]})
            break
    return dictionary

    


#routine(331313)