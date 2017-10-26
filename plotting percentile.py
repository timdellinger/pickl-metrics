"""
analytics on .csv data scraped from pickleballratings.com
    I've combined mens doubles and womens doubles
    (for some reason, mixed wouldn't show the number of matches on the website)
    
    here I'm pulling in a .csv that has number of games played in ~1 yr vs. percentile

"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.style.use('ggplot')


myColumnNames = ('number of matches','percentile')
df = pd.read_csv('number of matches vs percentile for both genders combined.csv', names = myColumnNames)



plt.figure();
plt.plot(df['percentile'],df['number of matches'])
plt.xlabel('percentile')
plt.ylabel('number of matches')
plt.show()


