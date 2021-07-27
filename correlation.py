import pandas as pd 
import csv 
import numpy as np  

def getdatasource(datapath) : 
    icecreamsales = [] 
    coldrinksales = [] 
    with open (datapath) as f : 
        df = csv.DictReader(f) 
        for i in df: 
            icecreamsales.append(float(i["Marks In Percentage"]))
            coldrinksales.append(float(i["Days Present"])) 
        return {"x":icecreamsales, "y":coldrinksales} 

def findcorrelation (datasource) : 
    correlation = np.corrcoef(datasource["x"], datasource["y"])
    print(correlation[0,1])

def setup():
    datapath = "./data-2.csv"
    datasource = getdatasource(datapath)
    findcorrelation(datasource) 

setup() 