# player.py

# USED BY: battle.py, scenes.py
from items import *

SPECIALABILITIES = ['heal', 'smash', ]


# defines the stats for the player
class Player:
    name = 'Default'
    health = 100
    healthMax = 100
    healthMin = 0
    # base attack stat
    attack = 12
    # the weapon when it changes can make a call to change this
    weapon = rock
    defense = 3
    speed = 10
    run = False
    playerLevel = 1
    # exp is set in battle() to be max of 100 until next level and to increase a level
    exp = 0
    expMax = 100
    leftExp = 0
    money = 0
    evasiveness = 6
    inventory = ['healthpotion']
    special = ['heal', 'smash', ]


# defines object of the class
player = Player()


def printPlayerSpecial(player):
    print('SPECIAL SKILLS\n=============')
    print('\n'.join(player.special))
    print('=============\n')


def usePlayerSpecial(player):
    print('Which special ability will you use? --BACK--')
    printPlayerSpecial(player)
    choice = input('')
    try:
        choice = str(choice.lower())
    except ValueError:
        print('Did you type that right?')
        usePlayerSpecial(player)
    if choice == 'b' or choice == 'back':
        return False
    for ability in SPECIALABILITIES:
        if choice in SPECIALABILITIES and choice in player.special:
            print('You are using {}'.format(choice))
            if choice == 'heal':
                player.health += 20
                print('You health is now {}'.format(player.health))
            elif choice == 'smash':
                player.attack += 20
            return True
        elif choice in SPECIALABILITIES and choice not in player.special:
            print('You cannot use this ability')
            usePlayerSpecial(player)
        else:
            print('Did you type that right?')
            usePlayerSpecial(player)