"""

markov chain transition matrix style analysis of the game of pickleball

this code creates a transition matrix, iterates for nRallys steps,
and outputs a bar chart of the margins of victory

The transition matrix:
there are 144 different possible score states:
 each team can have 0-11 points. 12x12=144.
 I'll re-use the 10-10 state to be equivalent to e.g. 11-11, 12-12, 13-13
 and similarly 11-10 equiavlent to e.g. 13-12
 and finally I'll use the 11-11 state to represent the we-won-by-two state 
with four possible servers, there are thus 144x4 = 576 states.

The transition matrix is therefore 576x576, although most entries are 0.

(Runtime for 100 rallies is less than a minute, so I'll just use
standard matrix methods instead of exploring "sparse matrix" methods.)

note that Pij is P(j|i) is the probability of moving from state i to j.
the top row is thus the list of probabilities of moving from state 0
and the leftmost column is the list of probabilities of moving to state 0

Transition probabilities are:
 p_winRallyA - probability (0 -> 1) of Team A winning the rally if Team A serves
 p_winRallyB - the corresponding probability for Team B serving

strictly speaking, the data structure used here is a python array, not a matrix.
np.dot is used instead of matrixmultiply for python 3.5 compatability

In the future: consider separating "win by two" scores above 10 from the 11-9 scores
consider extending the matrix to include scores up to 20


This is part of a statisctical exploration of the game of pickleball
begun in June 2016.  See usapa.org for information about the game.
Warning to potential players: the game is addictive!



Tim Dellinger

"""
import numpy as np
import matplotlib.pyplot as plt

nRallys = 100

p_winRallyA = 0.5
p_winRallyB = 0.5

p_loseRallyA = 1 - p_winRallyA
p_loseRallyB = 1 - p_winRallyB

transitionMatrix = np.zeros((576,576))


# the overall formula for matrix position is:
# (scoreA + 48 * score B) for A1 serving
#   + 12 for A2 serving
#   + 24 for B1 serving
#   + 36 for B2 serving
#
# the positions of states in the matrix aren't hard coded anywhere
# i.e. all code here uses the findState() function

# find position in the matrix from score and server identity    
def findState(scoreA, scoreB, server):
    return ( scoreA + 48 * scoreB + 12 * server)
    # server runs 0 -> 4 for A1, A2, B1, B2
 
# note that there are four places where the score is 11-11 (which can't happen)
# I'll use these to respresent the "winning the game by two points" state, e.g. 12-10

# win a point as server A1
for scoreB in range(11): # can only score if their score is 0-10
    for scoreA in range(11): # only can score if your score is 0-10
        transitionMatrix[ (findState(scoreA,scoreB,0),findState(scoreA+1,scoreB,0))]= p_winRallyA
# the 11-10 case for server A1 winning the game.  recall that the (11,11,0) state is used here for a win
transitionMatrix[ (findState(11,10,0),findState(11,11,0))] = p_winRallyA
# the 10-11 case for server A1 winning the rally to tie: move score to the 10-10 state
transitionMatrix[ (findState(10,11,0),findState(10,10,0))] = p_winRallyA

# lose the rally as server A1
for scoreB in range(11): # can only play if their score is 0-10
    for scoreA in range(11): # only can play if your score is 0-10
        transitionMatrix[(findState(scoreA,scoreB,0),findState(scoreA,scoreB,1))]= p_loseRallyA
# the 11-10 case for server A1 -> server A2
transitionMatrix[ findState(11,10,0),findState(11,10,1)] = p_loseRallyA
# the 10-11 case for server A1 -> server A2
transitionMatrix[ findState(10,11,0),findState(10,11,1)] = p_loseRallyA

# win a point as server A2
for scoreB in range(11): # can only score if their score is 0-10
    for scoreA in range(11): # only can score if your score is 0-10
        transitionMatrix[(findState(scoreA,scoreB,1),findState(scoreA+1,scoreB,1))]= p_winRallyA
# the 11-10 case for server A2 winning the game.  recall that the (11,11,1) state is used here for a win
transitionMatrix[ (findState(11,10,1),findState(11,11,1))] = p_winRallyA
# the 10-11 case for server A2 winning the rally to tie: move score to the 10-10 state
transitionMatrix[ (findState(10,11,1),findState(10,10,1))] = p_winRallyA

# lose the serve as server A2
for scoreB in range(11): # can only play if their score is 0-10
    for scoreA in range(11): # only can play if your score is 0-10
        transitionMatrix[(findState(scoreA,scoreB,1),findState(scoreA,scoreB,2))]= p_loseRallyA
# the 11-10 case for server A2 -> server B1
transitionMatrix[ findState(11,10,1),findState(11,10,2)] = p_loseRallyA
# the 10-11 case for server A2 -> server B1
transitionMatrix[ findState(10,11,1),findState(10,11,2)] = p_loseRallyA

# win a point as server B1
for scoreB in range(11): # can only score if their score is 0-10
    for scoreA in range(11): # only can score if your score is 0-10
        transitionMatrix[(findState(scoreA,scoreB,2),findState(scoreA,scoreB+1,2))]= p_winRallyB
# the 10-11 case for server B1 winning the game.  recall that the (11,11,2) state is used here for a win
transitionMatrix[ (findState(10,11,2),findState(11,11,2))] = p_winRallyB
# the 11-10 case for server B1 winning the rally to tie: move score to the 10-10 state
transitionMatrix[ (findState(11,10,2),findState(10,10,2))] = p_winRallyB

# lose the rally as server B1
for scoreB in range(11): # can only play if their score is 0-10
    for scoreA in range(11): # only can play if your score is 0-10
        transitionMatrix[(findState(scoreA,scoreB,2),findState(scoreA,scoreB,3))]= p_loseRallyB
# the 11-10 case for server B1 -> server B2
transitionMatrix[ findState(11,10,2),findState(11,10,3)] = p_loseRallyB
# the 10-11 case for server B1 -> server B2
transitionMatrix[ findState(10,11,2),findState(10,11,3)] = p_loseRallyB

# win a point as server B2
for scoreB in range(11): # can only score if their score is 0-10
    for scoreA in range(11): # only can score if your score is 0-10
        transitionMatrix[(findState(scoreA,scoreB,3),findState(scoreA,scoreB+1,3))]= p_winRallyB
# the 10-11 case for server B2 winning the game.  recall that the (11,11,3) state is used here for a win
transitionMatrix[ (findState(10,11,3),findState(11,11,3))] = p_winRallyB
# the 11-10 case for server B1 winning the rally to tie: move score to the 10-10 state
transitionMatrix[ (findState(11,10,3),findState(10,10,3))] = p_winRallyB

# lose the rally as server B2
for scoreB in range(11): # can only play if their score is 0-10
    for scoreA in range(11): # only can play if your score is 0-10
        transitionMatrix[(findState(scoreA,scoreB,3),findState(scoreA,scoreB,0))]= p_loseRallyB
# the 11-10 case for server B2 -> server A1
transitionMatrix[ findState(11,10,3),findState(11,10,0)] = p_loseRallyB
# the 10-11 case for server B2 -> server A1
transitionMatrix[ findState(10,11,3),findState(10,11,0)] = p_loseRallyB


# set all win states (11 points) to a value of "1" (stationary)
for theServer in range(4):
    for scoreB in range(10): #only up to a score of 9
        transitionMatrix[(findState(11,scoreB,theServer),findState(11,scoreB,theServer))]= 1
    for scoreA in range(10): #only up to a score of 9
        transitionMatrix[(findState(scoreA,11,theServer),findState(scoreA,11,theServer))]= 1
    # skip the score of 10, now catch the score of 11-11:        
    transitionMatrix[(findState(11,11,theServer),findState(11,11,theServer))]= 1

    
# making sure things sum correctly:
# print("number of rows that sum to 1 (should be 576):")
# print(list(transitionMatrix.sum(axis=1)).count(1.))
# print("number of empty colums (should be 0):")
# print(list(transitionMatrix.sum(axis=0)).count(0))

r1 = transitionMatrix
rN = np.dot(r1,r1)


for i in range(nRallys):
    rN = np.dot(r1,rN)

outcomes = rN[findState(0,0,1),:]    # game begins with second server, team A
    
xs = list(range(-11,12,1))
marginsOfVictory = [0 for x in xs]

# print (marginsOfVictory)

# margins of victory are positive if A wins, negative if B wins
for theServer in range(4):
    for scoreB in range(10): #only up to a score of 9.
        marginsOfVictory[22-scoreB]=marginsOfVictory[22-scoreB] + outcomes[findState(11,scoreB,theServer)]
    for scoreA in range(10): #only up to a score of 9
            marginsOfVictory[scoreA]=marginsOfVictory[scoreA] + outcomes[findState(scoreA,11,theServer)]
# catch the games that got past 11 
marginsOfVictory[13] = marginsOfVictory[13] + outcomes[findState(11,11,0)] + outcomes[findState(11,11,1)]
marginsOfVictory[9] = marginsOfVictory[9] + outcomes[findState(11,11,2)] + outcomes[findState(11,11,3)]

# print(marginsOfVictory)


# perhaps bump the xs by 0.5 to center them in the bar chart?
# use some variation on list(np.arrange(-11.5,0,1))

plt.style.use('ggplot')
fig = plt.bar(xs,marginsOfVictory)
plt.show()
