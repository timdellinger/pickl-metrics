"""
creates a plot of blowouts vs. Pwin for evenly matched teams

blowouts are games in which one team scores 5 or fewer points
Pwin is the probability that the serving team wins the rally

500,000 games were simulated using simulateGames.py
for seven values of pWin.  results are included below.


This is part of a statisctical exploration of the game of pickleball
begun in June 2016.  See usapa.org for information about the game.
Warning to potential players: the game is addictive!



Tim Dellinger

"""


import matplotlib.pyplot as plt

plt.style.use('ggplot')



p_values = [0.2,0.25,0.3,0.35,0.4,0.45,0.5]
blowoutsPer500000 = [131192,140060,147320,156429,166738,177359,189141]

blowoutPercents = [i/500000 * 100 for i in blowoutsPer500000]

width = 0.03
plt.figure()
plt.bar(p_values,blowoutPercents, width, align='center')
plt.xlabel('probability of the serving team winning a rally')
plt.ylabel('percent of games that are a blowout')
plt.show()

