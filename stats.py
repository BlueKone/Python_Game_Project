# stats.py

# USED BY: battle.py

import random


# call this when the player gets a new level
def increaseLevel(player):
    statIncreaseMin = 0
    statIncreaseMax = 3
    player.attack = player.attack + random.randint(statIncreaseMin, statIncreaseMax)
    print('Your attack is now: {}'.format(player.attack))
    player.defense = player.attack + random.randint(statIncreaseMin, statIncreaseMax)
    print('Your defense is now: {}'.format(player.defense))
    player.speed = player.speed + random.randint(statIncreaseMin, statIncreaseMax)
    print('Your speed is now: {}'.format(player.speed))
