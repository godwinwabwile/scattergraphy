import numpy as np
import pylab as pl
import matplotlib.pyplot as plt
import pandas  as  pd
import requests
from io import StringIO

'''read data  from csv'''
orig_url='https://drive.google.com/file/d/1wwK7gifM3J_1Lq9bqW-7Zkds_EAZ5fjx/view?usp=sharing'

file_id = orig_url.split('/')[-2]
dwn_url='https://drive.google.com/uc?export=download&id=' + file_id
url = requests.get(dwn_url).text
csv_raw = StringIO(url)
df = pd.read_csv(csv_raw)
df.dropna(inplace=True)

'''axis and arrea variables'''
x = df['MP']
y = df['SALARY']
area = np.pi*8

'''scatter graph'''
plt.scatter(x, y, s=area)# scatter plot
plt.title('Scatter plot')#title
plt.xlabel('MP')
plt.ylabel('Salary')
'''trendline'''
z = np.polyfit(x, y,1) 
p = np.poly1d(z)
pl.plot(x,p(x),"r-") 
plt.show()
'''coefficient'''
coeff = np.corrcoef(x, y)
print(coeff[0, 1])
