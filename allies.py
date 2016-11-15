# allies.py

# USED BY: battle.py, scenes.py
from items import *

SPECIAL_ABILITIES = ['heal', 'smash', ]


# defines the stats for the player
class Player:
    name = 'Default'
    health = 100
    healthMax = 100
    healthMin = 0
    # base attack stat
    attack = 25
    # the weapon when it changes can make a call to change this
    weapon = rock
    defense = 3
    speed = 10
    level = 1
    # exp is set in battle() to be max of 100 until next level and to increase a level
    exp = 0
    expMax = 100
    leftExp = 0
    evasiveness = 6
    special = ['smash']
player = Player()

# defines stats for Heiku
class Heiku:
    name = 'Heiku'
    health = 100
    healthMax = 100
    healthMin = 0
    attack = 15
    weapon = rock
    defense = 2
    speed = 8
    level = 2
    exp = 0
    expMax = 100
    leftExp = 0
    evasiveness = 6
    special = ['heal']  # this will not be seen, as only player specials are seen atm
heiku = Heiku()

# stats shared between the player and heiku
allyTeam = [player, heiku]
allyInventory = ['healthpotion']
allyMoney = 0
possibleSpiritNames = ['spirit', 'test']

class Spirits:
    name = possibleSpiritNames
    health = 100
    healthMax = 100
    healthMin = 0
    attack = 10
    weapon = rock
    defense = 2
    speed = 8
    level = 2
    exp = 0
    expMax = 100
    leftExp = 0
    evasiveness = 6
    special = ['heal']  # this will not be seen, as only player specials are seen atm
spirits = Spirits()

# -----------------------------SPECIAL--------------------------- #

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
    for ability in SPECIAL_ABILITIES:
        if choice in SPECIAL_ABILITIES and choice in player.special:
            print('You are using {}'.format(choice))
            if choice == 'heal':
                player.health += 20
                print('You health is now {}'.format(player.health))
            elif choice == 'smash':
                player.attack += 20
            return True
        elif choice in SPECIAL_ABILITIES and choice not in player.special:
            print('You cannot use this ability')
            usePlayerSpecial(player)
        else:
            print('Did you type that right?')
            usePlayerSpecial(player)

# ------------------------------ITEMS----------------------------------- #

def itemGet(item):
    if item in POSSIBLE_USE_ITEMS or item in POSSIBLE_EQUIP_ITEMS or item in POSSIBLE_SPECIAL_ITEMS:
        allyInventory.append(item)
    else:
        print('DEBUG: this item does not exist!')


def printItem():
    print('INVENTORY\n=============')
    print('\n'.join(allyInventory))
    print('=============\n')


# return true or false, depending on if there was an item used or not
# currently only useful for battles, as equip and special items cannot be used from this
# will only give values to player, never spirits or Heiku yet
def useItem():
    print('Which item will you use? --BACK--')
    printItem()
    choice = input(''.lower())
    if choice == 'b' or choice == 'back':
        return False
    # currently cannot use equip or special items in this function
    if choice in POSSIBLE_EQUIP_ITEMS or choice in POSSIBLE_SPECIAL_ITEMS:
        print('You cannot use that now!')
        useItem()
    # item must be able to be used and in the players inventory
    elif choice in POSSIBLE_USE_ITEMS and choice in allyInventory:
        print('You have used {}'.format(choice))
        allyInventory.remove(choice)
        if choice == 'healthpotion':
            print('You have used {}'.format(choice))
            player.health += healthpotion.restore
            if player.health >= player.healthMax:
                player.health = player.healthMax
            print('You now have {} health'.format(player.health))
        return True
    elif choice in POSSIBLE_USE_ITEMS and choice not in allyInventory:
        print('You do not have any of this item!')
        useItem()
    else:
        print('Did you type that right?')
        useItem()


# --------------old method below:

# def useItem(player):
#     print('Which item will you use?')
#     printItem(player)
#     for item in player.inventory:
#         choice = input('')
#         try:
#             player.inventory.remove(choice)
#             print('You have used: {}'.format(choice))
#             choice.use(player)
#             printItem(player)
#             break
#         except ValueError:
#             print('Did you type that right?')
#             useItem(player)
#             break
