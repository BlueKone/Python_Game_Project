# items.py

# USED BY: allies.py


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
