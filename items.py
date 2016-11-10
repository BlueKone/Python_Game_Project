# items.py

# USED BY: player.py


POSSIBLE_USE_ITEMS = ['healthpotion', 'magicpotion', 'powerup', ]
POSSIBLE_EQUIP_ITEMS = ['rock', 'dagger', ]
POSSIBLE_SPECIAL_ITEMS = ['shinyrock', 'pumpkin', ]


# Superclass of all items in the game
class Item:
    def __init__(self, name, description, value):
        self.name = name
        self.description = description
        self.value = value

    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\n".format(self.name, self.description, self.value)


class ShinyRock(Item):
    def __init__(self):
        super().__init__(name="Shiny Rock",
                         description="A strange shining stone that was found on a monster.",
                         value=0)
shinyrock = ShinyRock()


# superclass of weapons, subclass of items
class Weapon(Item):
    def __init__(self, name, description, value, attackMax, attackMin):
        self.attackMax = attackMax
        self.attackMin = attackMin
        super().__init__(name, description, value)

    def __str__(self):
        return "{}:\n=====\n{}\nValue: {}\nMin Attack: {}\nMax Attack: {}".format(self.name, self.description,
                                                             self.value, self.attackMin, self.attackMax)


class Rock(Weapon):
    def __init__(self):
        super().__init__(name="Rock",
                         description="A fist-sized rock, suitable for bludgeoning.",
                         value=1,
                         attackMin=2,
                         attackMax=5)
rock = Rock()


# --------currently does not have all the weapon variables set------------
class Dagger(Weapon):
    def __init__(self):
        super().__init__(name="Dagger",
                         description="A small iron dagger with some rust.",
                         value=10,
                         attackMin=2,
                         attackMax=8)
dagger = Dagger()


class Ceremonial_Sword(Weapon):
    def __init__(self):
        super().__init__(name="Ceremonial sword",
                         description="An old and worn short sword. It has seen better days.",
                         value=10,
                         attackMin=5,
                         attackMax=12)
ceremonial_sword = Ceremonial_Sword()


class Potion(Item):
    def __init__(self, name, description, value, stat, restore, increase, time):
        self.stat = stat
        self.restore = restore
        self.increase = increase
        self.time = time
        super().__init__(name, description, value)

    def __str__(self):
        return "{}:\n=====\n{}\nValue: {}\nStat: {}\nRestore: {}".format(self.name, self.description,
                                                             self.value, self.stat, self.restore)


class HealthPotion(Potion):
    def __init__(self):
        super().__init__(name="Health Potion",
                         description="A potion designed to quickly heal your wounds.",
                         value=10,
                         stat='health',
                         restore=20,
                         increase=0,
                         time=0)

healthpotion = HealthPotion()

# --------------------------------------------------------------------------------------


def itemGet(player, item):
    if item in POSSIBLE_USE_ITEMS or item in POSSIBLE_EQUIP_ITEMS or item in POSSIBLE_SPECIAL_ITEMS:
        player.inventory.append(item)
    else:
        print('DEBUG: this item does not exist!')


def printItem(player):
    print('INVENTORY\n=============')
    print('\n'.join(player.inventory))
    print('=============\n')


# return true or false, depending on if there was an item used or not
# currently only useful for battles, as equip and special items cannot be used from this
def useItem(player):
    print('Which item will you use? --BACK--')
    printItem(player)
    choice = input(''.lower())
    if choice == 'b' or choice == 'back':
        return False
    # currently cannot use equip or special items in this function
    if choice in POSSIBLE_EQUIP_ITEMS or choice in POSSIBLE_SPECIAL_ITEMS:
        print('You cannot use that now!')
        useItem(player)
    # item must be able to be used and in the players inventory
    elif choice in POSSIBLE_USE_ITEMS and choice in player.inventory:
        print('You have used {}'.format(choice))
        player.inventory.remove(choice)
        if choice == 'healthpotion':
            print('You have used {}'.format(choice))
            player.health += healthpotion.restore
            if player.health >= player.healthMax:
                player.health = player.healthMax
            print('You now have {} health'.format(player.health))
        return True
    elif choice in POSSIBLE_USE_ITEMS and choice not in player.inventory:
        print('You do not have any of this item!')
        useItem(player)
    else:
        print('Did you type that right?')
        useItem(player)


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
