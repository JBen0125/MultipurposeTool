"""
Classes:

        mini_games

Functions:

        flip_a_coin()                       # Used
        roll_dice()                         # Used


Objects:

        None

Description:

        This module includes mini-games
"""
import random as rand


# Flip a coin
def flip_a_coin():
    """
    This function flips a coin.

    returns None
    """
    h = "Heads"
    t = "Tails"
    r = rand.randint(1, 2)
    if r == 1:
        print(h)
    else:
        print(t)


# Roll the dice
def roll_dice():
    """
    This function rolls a dice.

    returns None
    """
    r = rand.randint(1, 6)
    print(r)
