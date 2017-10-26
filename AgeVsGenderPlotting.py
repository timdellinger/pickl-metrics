"""
analytics on .csv data scraped from pickleballratings.com
    I've combined mens doubles and womens doubles
    (for some reason, mixed wouldn't show the number of matches on the website)
    
    here I'm pulling in .csv files that have # of matches, rating, age
    
    let's see if gender or if singles/doubles effects the age distribution
   
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.style.use('ggplot')

# I have to name the columns so that the legend ends up readable

myColumnNames = ('number of matches','rating','MD age')
dfMD = pd.read_csv('mens doubles matches rating age.csv', names = myColumnNames)

myColumnNames = ('number of matches','rating','MS age')
dfMS = pd.read_csv('mens singles matches rating age.csv', names = myColumnNames)

myColumnNames = ('number of matches','rating','WD age')
dfWD = pd.read_csv('womens doubles matches rating age.csv', names = myColumnNames)

myColumnNames = ('number of matches','rating','WS age')
dfWS = pd.read_csv('womens singles matches rating age.csv', names = myColumnNames)

plt.figure();
dfMS['MS age'].plot.hist(histtype='step',bins=np.arange(5,100,1))
dfMD['MD age'].plot.hist(histtype='step',bins=np.arange(5,100,1))
dfWS['WS age'].plot.hist(histtype='step',bins=np.arange(5,100,1))
dfWD['WD age'].plot.hist(histtype='step',bins=np.arange(5,100,1))
plt.xlabel('age')
plt.legend()
plt.show()
