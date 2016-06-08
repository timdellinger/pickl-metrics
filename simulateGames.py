"""
Simulates a series of pickleball games between two teams (Team A, Team B)
Team A serves first

input parameters:
    rallyProbWhenAServes - probability (0 -> 1) of Team A winning the rally if Team A serves
    rallyProbWhenBServes - the corresponding probability for Team B serving
    numberOfGames - number of games to be played.  100000 gives decent statistics in less than a minute.
    
output is a .csv file (gameResults.csv)
each line contains Team A's score, Team B's score, the number of rallies in the game



This is part of a statisctical exploration of the game of pickleball
begun in June 2016.  See usapa.org for information about the game.
Warning to potential players: the game is addictive!



Tim Dellinger
 
"""

import random
import pandas as pd
import csv

rallyProbWhenAServes = 0.5
rallyProbWhenBServes = 0.5
numberOfGames = 100000

def isGameOver(a,b):
    if a == 11 and b < 10 : return True
    elif b == 11 and a < 10 : return True
    elif a == b - 2 and b > 11 : return True
    elif b == a - 2 and a > 11 : return True
    else: return False

def incrementServer(theServer):
    if theServer == 'a1' : return 'a2'
    elif theServer == 'a2' : return 'b1'
    elif theServer == 'b1' : return 'b2'
    else: return 'a1'
    
    
def playGame(rallyProbWhenAServes, rallyProbWhenBServes):
    score = (0,0)
    numberOfRallies = 0
    whoServes = 'a2'
    while isGameOver(*score) == False :
        numberOfRallies += 1
        if whoServes == 'a1' or whoServes == 'a2':
            if random.random() < rallyProbWhenAServes: score = (score[0]+1,score[1])
            else: whoServes = incrementServer(whoServes)
        elif whoServes == 'b1' or whoServes == 'b2':
            if random.random() < rallyProbWhenBServes: score = (score[0],score[1]+1)
            else: whoServes = incrementServer(whoServes)
    return (score[0],score[1],numberOfRallies)

gameResults = []

for n in range(numberOfGames):
    gameResults.append(playGame(rallyProbWhenAServes,rallyProbWhenBServes))
     
print('done')  

gameResultsDF = pd.DataFrame(gameResults)
gameResultsDF.to_csv('gameResults.csv', index=False, header=False)
