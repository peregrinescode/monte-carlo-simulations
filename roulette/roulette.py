"""
Monte Carlo simulation for simulating a roulette wheel
Author: Ross <ross dot warren at pm dot me>
Reproduced from MIT online course 'Introduction to Computational Thinking and Data Science'
"""


import random

class Roulette():
    """Set up the roulette wheel."""
    def __init__(self):
        self.pockets = []
        for i in range (1, 37):
            self.pockets.append(i)  # Create 36 pockets in roulette wheel
        self.ball = None
        self.pocketOdds = len(self.pockets) - 1 # Payback is $35 for correct pocket ie odds of 35/1

    def spin(self):
        self.ball = random.choice(self.pockets) # Ball randomly falls in a pocket

    def betPocket(self, pocket, amt):
        if str(pocket) == str(self.ball):
            return amt * self.pocketOdds
        else:
            return -amt

    def __str__(self):
        return 'Fair Roulette Wheel'


class EuRoulette(Roulette):
    """European roulette wheel with one green zero. Odds do not change"""
    def __init__(self):
        Roulette.__init__(self)
        self.pockets.append('0')    # add a zero pocket

    def __str__(self):
        return 'European Roulette'

class AmRoulette(EuRoulette):
    """American roulette wheel with two greens. Odds do not change"""
    def __init__(self):
        EuRoulette.__init__(self)
        self.pockets.append('00')    # add a zero pocket

    def __str__(self):
        return 'American Roulette'


def playRoulette(game, numSpins, pocket, bet):
    """Method for playing the game."""
    totPocket = 0   # initially we have won 0
    for i in range(numSpins):
        game.spin()
        totPocket += game.betPocket(pocket, bet)

    # print(numSpins, 'spins of', game)
    # print('Expected return betting', pocket, '=', str(100*totPocket/numSpins), '%\n')
    return (totPocket/numSpins)


def getMeanAndStd(X):
    """Takes a list and return mean and std."""
    mean = sum(X)/len(X)
    tot = 0.0
    for x in X:
        tot += (x - mean)**2
    std = (tot / len(X))**0.5
    return mean, std


### PROGRAM ###

if __name__ == '__main__':
    games = (Roulette, EuRoulette, AmRoulette)
    pocket = 2
    numTrial = 20
    for numSpins in (1000, 100000):
        for game in games:
            results = []
            print('Simulating of', game(), ': Betting on a pocket for', numTrial, 'number of trials of ', numSpins, 'spins each')
            for i in range(numTrial):
                pocketReturns = playRoulette(game(), numSpins, pocket, 1)
                results.append(pocketReturns)

            mean,std = getMeanAndStd(results)
            print('Expected return betting on', pocket, '=', round(mean*100, 2), '+/-', round(std*1.96*100, 2),  '% with 95% confidence.\n')