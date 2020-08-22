import requests
import json
from itertools import groupby
import pandas as pd
import numpy as np
url = "https://api.covid19api.com/total/country/united-kingdom"
res = requests.get(url)
data = res.json()
df = pd.DataFrame.from_dict(data)
#first question
print(df.head())
table = pd.pivot_table(df, values=['Country','Recovered'],index=['Confirmed'],columns=["Date"],aggfunc=np.sum, margins=True)
table.stack('Date')
print(table)

#second question
print(df[["Country","Recovered"]])

