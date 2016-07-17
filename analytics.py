"""
Performs some analytics on the results of simulated pickleball matches

input is a .csv file (gameResults.csv)
each line contains Team A's score, Team B's score, the number of rallies in the game

this script:
    prints the number of games in which the score surpassed 11
    prints the number of wins by Team A (the team that serves first)
    creates a histogram of the margin of victory of Team A (margin is negative if Team A loses)
    creates a histogram of the number of rallies per game
    
    

This is part of a statisctical exploration of the game of pickleball
begun in June 2016.  See usapa.org for information about the game.
Warning to potential players: the game is addictive!



Tim Dellinger

"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.style.use('ggplot')


myColumnNames = ('teamAScore','teamBScore','numberOfRallies')
df = pd.read_csv('gameResults.csv', names = myColumnNames)

# margin of victory for team A (negative if they lost!)
df['marginOfVictory'] = df.teamAScore - df.teamBScore

# did the game get into "you must win by two" territory? (True/False)
df['isScoreGreaterThanEleven'] = (df['teamAScore']>11) | (df['teamBScore']>11)
print('how many times was the game score greater than eleven?')
winByTwoStats = df.isScoreGreaterThanEleven.value_counts()
print( 'it was greater than eleven ',winByTwoStats[1],' times' )

# how many games did Team A (the team that serves first) win?
mOfVictory = df.marginOfVictory
posMOfVictory = mOfVictory[mOfVictory > 0]
print('\n','number of wins by team A:',posMOfVictory.count(),' wins','\n' )

# how many blowouts (one team scored 5 or fewer points)?
df['isBlowout'] = (df['teamAScore']<6) | (df['teamBScore']<6)
print('how many times was the game a blowout (one team scores 5 or fewer points)?')
blowoutStats = df.isBlowout.value_counts()
print( 'it was a blowout ',blowoutStats[1],' times' )

# margin of victory histogram
plt.figure();
df.marginOfVictory.plot.hist(bins=np.arange(-11.5,15.5,1))
plt.xlabel('margin of victory for Team A')
plt.show()

# number of rallies per game histogram
plt.figure();
df.numberOfRallies.plot.hist(bins=range(0,100,1))
plt.xlabel('number of rallies per game')
plt.show()


