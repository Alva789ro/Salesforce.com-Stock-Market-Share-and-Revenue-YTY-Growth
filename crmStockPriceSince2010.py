import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#import seaborn as sns

#Select the stock you will use
crm=yf.download('CRM', start='2009-12-31', interval='1d')
c_crm = crm.reset_index()

#time frame for the values
list=[2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019]
list2=[0]
dic1={}


def years_prices(db):
    #Gets the % change of any given stock from 2010 to 2019.
    # will get updated at year-end
    y10=(float(db['Close'].loc[db['Date']=='2010-12-31'])-float(db['Close'].loc[db['Date']=='2010-01-04']))/float(db['Close'].loc[db['Date']=='2010-01-04'])
    y11=(float(db['Close'].loc[db['Date']=='2011-12-30'])-float(db['Close'].loc[db['Date']=='2011-01-03']))/float(db['Close'].loc[db['Date']=='2011-01-03'])
    y12=(float(db['Close'].loc[db['Date']=='2012-12-31'])-float(db['Close'].loc[db['Date']=='2012-01-03']))/float(db['Close'].loc[db['Date']=='2012-01-03'])
    y13=(float(db['Close'].loc[db['Date']=='2013-12-31'])-float(db['Close'].loc[db['Date']=='2013-01-02']))/float(db['Close'].loc[db['Date']=='2013-01-02'])
    y14=(float(db['Close'].loc[db['Date']=='2014-12-31'])-float(db['Close'].loc[db['Date']=='2014-01-02']))/float(db['Close'].loc[db['Date']=='2014-01-02'])
    y15=(float(db['Close'].loc[db['Date']=='2015-12-31'])-float(db['Close'].loc[db['Date']=='2015-01-02']))/float(db['Close'].loc[db['Date']=='2015-01-02'])
    y16=(float(db['Close'].loc[db['Date']=='2016-12-30'])-float(db['Close'].loc[db['Date']=='2016-01-04']))/float(db['Close'].loc[db['Date']=='2016-01-04'])
    y17=(float(db['Close'].loc[db['Date']=='2017-12-29'])-float(db['Close'].loc[db['Date']=='2017-01-03']))/float(db['Close'].loc[db['Date']=='2017-01-03'])
    y18=(float(db['Close'].loc[db['Date']=='2018-12-31'])-float(db['Close'].loc[db['Date']=='2018-03-02']))/float(db['Close'].loc[db['Date']=='2018-01-02'])
    y19=(float(db['Close'].loc[db['Date']=='2019-12-31'])-float(db['Close'].loc[db['Date']=='2019-01-02']))/float(db['Close'].loc[db['Date']=='2019-01-02'])
    list2.append(y10)
    list2.append(y11)
    list2.append(y12)
    list2.append(y13)
    list2.append(y14)
    list2.append(y15)
    list2.append(y16)
    list2.append(y17)
    list2.append(y18)
    list2.append(y19)



def dict_generator(l1,l2):
    #creates a disctionary that will store the year and its %change of the stock.
    #use the value from the lists created (list and list2) when you call the function.
    dic1.setdefault('Year', l1)
    dic1.setdefault('% Change', l2)
#    print(dic1)


years_prices(c_crm)
dict_generator(list,list2)

df=pd.DataFrame(dic1)
#print(df)
#plt.plot(list, list2, c='red')
#plt.show()
