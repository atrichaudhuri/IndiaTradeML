import pandas as pd
import matplotlib.pyplot as plt


ImportData = pd.read_csv('2018-2010_import.csv')


ImportData2018 = ImportData[ImportData['year']==2018]
ImportData2017 = ImportData[ImportData['year']==2017]
ImportData2016 = ImportData[ImportData['year']==2016]
ImportData2015 = ImportData[ImportData['year']==2015]
ImportData2014 = ImportData[ImportData['year']==2014]
ImportData2013 = ImportData[ImportData['year']==2013]
ImportData2012 = ImportData[ImportData['year']==2012]

ImportData2018HSandValue = ImportData2018[['HSCode' , 'value']]
ImportData2017HSandValue = ImportData2017[['HSCode' , 'value']]
ImportData2016HSandValue = ImportData2016[['HSCode' , 'value']]
ImportData2015HSandValue = ImportData2015[['HSCode' , 'value']]
ImportData2014HSandValue = ImportData2014[['HSCode' , 'value']]
ImportData2013HSandValue = ImportData2013[['HSCode' , 'value']]
ImportData2012HSandValue = ImportData2012[['HSCode' , 'value']]

ImportData2018HSandValue.plot(kind='scatter', x='HSCode', y='value', title='2018 Import Value For Each HSCode')
ImportData2017HSandValue.plot(kind='scatter', x='HSCode', y='value', title='2017 Import Value For Each HSCode')
ImportData2016HSandValue.plot(kind='scatter', x='HSCode', y='value', title='2016 Import Value For Each HSCode')
ImportData2015HSandValue.plot(kind='scatter', x='HSCode', y='value', title='2015 Import Value For Each HSCode')
ImportData2014HSandValue.plot(kind='scatter', x='HSCode', y='value', title='2014 Import Value For Each HSCode')
ImportData2013HSandValue.plot(kind='scatter', x='HSCode', y='value', title='2013 Import Value For Each HSCode')
ImportData2012HSandValue.plot(kind='scatter', x='HSCode', y='value', title='2012 Import Value For Each HSCode')

plt.show()





