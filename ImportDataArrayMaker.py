import numpy as np
import pandas as pd


#importing the dataset
ImportDataSet = pd.read_csv('2018-2010_import.csv')

#dropping all na values from ImportDataSet and storing as ImportDataSet_dropna
ImportDataSet_dropna = ImportDataSet.dropna(axis=0, how='any', thresh=None, subset=None, inplace=False)

#seperating data year wise 
ImportDataSet_dropna_2018 = ImportDataSet_dropna[ImportDataSet_dropna['year'] == 2018]
ImportDataSet_dropna_2017 = ImportDataSet_dropna[ImportDataSet_dropna['year'] == 2017]
ImportDataSet_dropna_2016 = ImportDataSet_dropna[ImportDataSet_dropna['year'] == 2016]
ImportDataSet_dropna_2015 = ImportDataSet_dropna[ImportDataSet_dropna['year'] == 2015]
ImportDataSet_dropna_2014 = ImportDataSet_dropna[ImportDataSet_dropna['year'] == 2014]
ImportDataSet_dropna_2013 = ImportDataSet_dropna[ImportDataSet_dropna['year'] == 2013]
ImportDataSet_dropna_2012 = ImportDataSet_dropna[ImportDataSet_dropna['year'] == 2012]
ImportDataSet_dropna_2011 = ImportDataSet_dropna[ImportDataSet_dropna['year'] == 2011]
ImportDataSet_dropna_2010 = ImportDataSet_dropna[ImportDataSet_dropna['year'] == 2010]

#getting the values for each year
ImportDataSet_dropna_2018_value_year = ImportDataSet_dropna_2018['value']
ImportDataSet_dropna_2017_value_year = ImportDataSet_dropna_2017['value']
ImportDataSet_dropna_2016_value_year = ImportDataSet_dropna_2016['value']
ImportDataSet_dropna_2015_value_year = ImportDataSet_dropna_2015['value']
ImportDataSet_dropna_2014_value_year = ImportDataSet_dropna_2014['value']
ImportDataSet_dropna_2013_value_year = ImportDataSet_dropna_2013['value']
ImportDataSet_dropna_2012_value_year = ImportDataSet_dropna_2012['value']
ImportDataSet_dropna_2011_value_year = ImportDataSet_dropna_2011['value']
ImportDataSet_dropna_2010_value_year = ImportDataSet_dropna_2010['value']

#creating numpy array year wuse for values
value_year_2018_ar = np.array(ImportDataSet_dropna_2018_value_year)
value_year_2017_ar = np.array(ImportDataSet_dropna_2017_value_year)
value_year_2016_ar = np.array(ImportDataSet_dropna_2016_value_year)
value_year_2015_ar = np.array(ImportDataSet_dropna_2015_value_year)
value_year_2014_ar = np.array(ImportDataSet_dropna_2014_value_year)
value_year_2013_ar = np.array(ImportDataSet_dropna_2013_value_year)
value_year_2012_ar = np.array(ImportDataSet_dropna_2012_value_year)
value_year_2011_ar = np.array(ImportDataSet_dropna_2011_value_year)
value_year_2010_ar = np.array(ImportDataSet_dropna_2010_value_year)

#summation of import value per year
import_value_2018 = np.sum(value_year_2018_ar)
import_value_2017 = np.sum(value_year_2017_ar)
import_value_2016 = np.sum(value_year_2016_ar)
import_value_2015 = np.sum(value_year_2015_ar)
import_value_2014 = np.sum(value_year_2014_ar)
import_value_2013 = np.sum(value_year_2013_ar)
import_value_2012 = np.sum(value_year_2012_ar)
import_value_2011 = np.sum(value_year_2011_ar)
import_value_2010 = np.sum(value_year_2010_ar)

#creating a Y axis numpy array 
