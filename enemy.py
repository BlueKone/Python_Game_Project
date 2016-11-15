# enemy.py

# USED BY: main.py


class Enemy:
    def __init__(self, name, health, healthMax, healthMin, defence, speed, attack, attackMax, attackMin, evasiveness,
                 giveExp):
        self.name = name
        self.health = health
        self.healthMax = healthMax
        self.healthMin = healthMin
        # attack is the enemies base attack stat
        self.attack = attack
        # attack min and max are used for adding to attack a random number
        self.attackMax = attackMax
        self.attackMin = attackMin
        # other stats:
        self.defense = defence
        self.speed = speed
        self.evasiveness = evasiveness
        self.giveExp = giveExp

    def is_alive(self):
        return self.health > 0


class GiantSpider(Enemy):
    def __init__(self):
        super().__init__(name="Giant Spider", health=100, healthMax=100, healthMin=0, defence=3,
                         attack=5, attackMin=3, attackMax=7, speed=10, evasiveness=5, giveExp=100)
giant_spider = GiantSpider()


# currently does not have all necessary variables set
class Ogre(Enemy):
    def __init__(self):
        super().__init__(name="Ogre", health=100, healthMax=100, healthMin=0, defence=6,
                         attack=5, attackMin=13, attackMax=16, speed=10, evasiveness=5, giveExp=100)
ogre = Ogre()


class Shadow(Enemy):
    def __init__(self):
        super().__init__(name="Shadow", health=100, healthMax=100, healthMin=0, defence=6,
                         attack=5, attackMin=3, attackMax=5, speed=8, evasiveness=5, giveExp=100)
shadow = Shadow()
