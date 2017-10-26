"""
analytics on .csv data scraped from pickleballratings.com
    I've combined mens doubles and womens doubles
    (for some reason, mixed wouldn't show the number of matches on the website)
    
    

"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.style.use('ggplot')


myColumnNames = ('number of matches','rating','age')
df = pd.read_csv('mens and womens combined with zeros for blanks no names.csv', names = myColumnNames)



plt.figure();
df['number of matches'].plot.hist(bins=np.arange(0,120,1))
plt.xlabel('number of matches')
plt.show()

plt.figure();
df['rating'].plot.hist(bins=np.arange(1.5,6,0.005))
plt.xlabel('rating')
plt.show()

plt.figure();
df['age'].plot.hist(bins=np.arange(5,100,1))
plt.xlabel('age')
plt.show()

plt.figure();
df['age'].plot.hist(bins=np.arange(10,100,5))
plt.xlabel('age')
plt.show()


# 'last name','first name',

# maybe use    count, bins = np.histogram(df['marginOfVictory'],bins=np.arange(-11.5,15.5,1))
