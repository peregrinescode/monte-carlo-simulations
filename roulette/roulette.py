"""
Monte Carlo simulation for calculating pi.
Author: Ross <ross dot warren at pm dot me>
Reproduced from MIT online course 'Introduction to Computational Thinking and Data Science'
"""


import random
import math

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

def playRoulette(game, numSpins, pocket, bet):
    """Method for playing the game."""
    totPocket = 0   # initially we have won 0
    for i in range(numSpins):
        game.spin()
        totPocket += game.betPocket(pocket, bet)

    print(numSpins, 'spins of', game)
    print('Expected return betting', pocket, '=', str(100*totPocket/numSpins), '%\n')
    return (totPocket/numSpins)

if __name__ == '__main__':
    game = Roulette()
    for numSpins in (100, 100000):
        for i in range(3):
            playRoulette(game, numSpins, 2, 1)