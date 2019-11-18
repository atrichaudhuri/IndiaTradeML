import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def cleanup(df):
    cleandf = df.dropna(inplace = False)
    return cleandf

def commodity10(df):
    commodity_values = df.groupby('Commodity').agg({'value': 'sum'})
    print(commodity_values)
    print("Top 10 Commodities in 8 years \n" , commodity_values.nlargest(10, 'value'))
    commodity_10 = commodity_values.nlargest(10, 'value')

    commodity_x = [['Mineral Fuels etc.'],['Natural or Cultured Pearls etc.'],['Electrical Machinery and Equipment etc.'],
                   ['Nuclear Reactors, Boilers etc'], ['Organic Chemicals'], ['Plastics and Articles Thereof'],['Iron and Steel'],
                   ['Animal and Vegetable Fats etc.'],['Optical, Photographic/Medical Surgical Tools'],['Fertilizers']]

    #plt.plot(commodity_x,commodity_10)


def country10(df):
    country_values = df.groupby('country').agg({'value' : 'sum'})
    country_10 = country_values.nlargest(10, 'value')
    print("The Top 10 Countries of Import by Value are \n", country_10)



import_df = pd.read_csv('2018-2010_import.csv')
print("Description of Dataset \n", import_df.describe())
print("Description of all null values \n", import_df.isnull().sum())
clean_imports = cleanup(import_df)
commodity10(clean_imports)
country10(clean_imports)

