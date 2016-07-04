# pickl-metrics
Statistical exploration of the game of pickleball (see usapa.org for information on the game)

Simulated games can provide insight into the relation between player skill and game score.  This will help lay the
foundation for analyzing actual match results: estimating player skill levels, predicting the results of matches, and other fun things.  The model is essentially a Markov chain, with the transition probabilities being the probability that a team wins a rally (and thus a point) if they serve.

A few open questions that are tackled here:
- Does the structure of the game favor the team that serves first?
- For equally talented opponents, how many matches are blowouts (losing team scores less than 5 points)?
- For equally talented opponents, how many matches go above 11 points and into "you must win by 2" territory?
- For equally talented opponents, how many rallies occur during games? 

*simulateGames.py* - Simulates a series of pickleball games between two teams (Team A, Team B).  Team A serves first.
                   Input parameters are the probability that Team A wins the rally when serving, and the corresponding
                   probability for Team B.
                   output is a .csv file.  Each line contains Team A's score, Team B's score, the number of rallies in the game.
                  
*analytics.py* -  takes the .csv file from simulateGames as input,
                prints the number of games in which the score surpassed 11,
                prints the number of wins by Team A (the team that serves first),
                creates a histogram of the margin of victory of Team A (margin is negative if Team A loses), and
                creates a histogram of the number of rallies per game
                
Example histograms are included here for 100,000 games, with probabilities set at 0.5 (i.e. coin flip) for every rally.
                
*early results.txt* - some quick and dirty early results

*markovTransitionMatrix.py* - Markov chain style treatment of pickleball games, using a transition matrix.  Takes as input probabilities of Team A and Team B winning rallies.  Output is a histogram of the margins of victory of games.
