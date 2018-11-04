import excelsearcher
import stocklookup
import json

def passNAICS(number):    
     excelData = json.dumps(excelsearcher(number) ) 
     stockData = json.dumps(excelData["comp0"] ) 
     for i in range(1, 10): 
         stockData = stockData.concat(json.dumps(excelData["comp"+ str(i)]) ) 
     returnedData = excelData.concat(stockData ) 
     return returnedData


     