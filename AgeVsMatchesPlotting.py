"""
analytics on .csv data scraped from pickleballratings.com
    I've combined mens doubles and womens doubles
    (for some reason, mixed wouldn't show the number of matches on the website)
    
    here I'm pulling in .csv files that have # of matches, rating, age
    
    let's see how many games people play as a funtion of age
    this might need a box and whisker instead of just showing all the datapoints!
   
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.style.use('ggplot')


myColumnNames = ('number of matches','rating','age')
dfMD = pd.read_csv('mens doubles matches rating age.csv', names = myColumnNames)
dfMS = pd.read_csv('mens singles matches rating age.csv', names = myColumnNames)
dfWD = pd.read_csv('womens doubles matches rating age.csv', names = myColumnNames)
dfWS = pd.read_csv('womens singles matches rating age.csv', names = myColumnNames)

plt.figure();
plt.plot(dfMD['age'],dfMD['number of matches'],'bs')
plt.ylabel('number of matches')
plt.xlabel('age')
plt.show()

plt.figure();
plt.plot(dfMS['age'],dfMS['number of matches'],'bs')
plt.ylabel('number of matches')
plt.xlabel('age')
plt.show()

plt.figure();
plt.plot(dfWD['age'],dfWD['number of matches'],'bs')
plt.ylabel('number of matches')
plt.xlabel('age')
plt.show()

plt.figure();
plt.plot(dfWS['age'],dfWS['number of matches'],'bs')
plt.ylabel('number of matches')
plt.xlabel('age')
plt.show()