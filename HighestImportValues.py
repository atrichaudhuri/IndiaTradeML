import numpy as np
import pandas as pd  
import matplotlib.pyplot as plt 

ImportsData = pd.read_csv('/home/atri/Documents/NTCC Sem 5/india-trade-data/2018-2010_import.csv')

Import2018 = [ImportsData['year'] == 2018]
HighestImport = Import2018.loc[Import2018['value'].idxmax()]


print(HighestImport)

