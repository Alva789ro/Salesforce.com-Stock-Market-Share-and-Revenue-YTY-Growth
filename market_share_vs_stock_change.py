import xlsxwriter
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from crmStockPriceSince2010 import list, list2, dic1, df

crm_ms=pd.read_excel(r'\Users\jesica\Desktop\Salesforce.com Market share vs Stock Growth\Market share since 2010.xlsx', sheet_name='CRM Market Share')


#dict_generator(crm_ms['Year'], crm_ms['Market Share Growth'])
crm_msg=[]
crm_rg=[]

def list_generator(val, list):
    for x in val:
        list.append(x)
#    print(list)


list_generator(crm_ms['Market Share Growth'],crm_msg)
list_generator(crm_ms['Revenues Growth'], crm_rg)

print(list, list2, crm_msg, crm_rg)
plt.plot(list, list2, label='Stock Growth')
plt.plot(list, crm_msg, label='Market Share Growth')
plt.plot(list, crm_rg, label='Revenues Growth')
plt.title('Stock Growth vs Market Share Growth vs Revenue Growth')
plt.legend(loc='best')
plt.show()
