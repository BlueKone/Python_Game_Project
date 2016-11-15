# battle.py

# USED BY: scenes.py
# USING: allies.py

import random
from allies import *


'''Features'''
# --set a maximum? -- max 9 enemies, number of players is not handled here (max of 5 spirits, 2 players = 7)
# player and heiku are different than the spirits (always player and heiku in battle, unless defeated)
# --can have different enemies in single battle
# (player.py) each spirit has different abilities and skills, stats, etc.
# player and heiku cannot get hit until spirits are defeated, unless special situations
# --random ranges of attacks
# (maybe use this in player.py) each spirit can be equiped with specific items
# --special situations when you cannot run from a battle
# only the player and heiku are able to use items, run
# --one team is faster, will go together first (team turn based)
# temporary stats: battle temp and turn temp
# enemy decisions based on probability (random ranges and actions between numbers)

'''System'''
# have a main function to do the battle loop

global alive

# function is ALWAYS called outside of this script, starting the entire battle system, never called locally
# special is a bool called outside of function to determine if you can run, etc. (maybe define what kind of special)
def battleStart(special, enemyOne, enemyTwo=False, enemyThree=False, enemyFour=False, enemyFive=False,
                enemySix=False, enemySeven=False, enemyEight=False, enemyNine=False):
    maxEnemies = [enemyOne, enemyTwo, enemyThree, enemyFour, enemyFive, enemySix, enemySeven, enemyEight, enemyNine]
    enemies = []
    # checking how many enemies are in the battle
    for ecount in maxEnemies:
        if ecount:
            enemies.append(ecount)
        else:
            pass

    # check who is faster
    allyFaster = checkSpeed(enemies)

    # if the ally team is faster, they go first
    global alive
    alive = True
    if allyFaster:
        while alive:
            print('--Allies Turn--')
            allyAction(enemies, special)
            print('--Enemies Turn--')
            enemiesAction(enemies)
            continue
        print('alive loop broken')
        battleEnd()
    # if enemy team is faster, they go first
    else:
        while alive:
            print('--Enemies Turn--')
            enemiesAction(enemies)
            print('--Allies Turn--')
            allyAction(enemies, special)
            continue
        battleEnd()


# returns true or false based on if the player is faster than the enemies or not.
def checkSpeed(enemies):
    TeamEnemyValues = []
    for ecounter in range(len(enemies)):
        enemySpeed = enemies[ecounter].speed
        TeamEnemyValues.append(enemySpeed)
    teamEnemySpeed = sum(TeamEnemyValues)

    TeamPlayerValues = []
    for pcounter in range(len(allyTeam)):
        playerSpeed = allyTeam[pcounter].speed
        TeamPlayerValues.append(playerSpeed)
    teamPlayerSpeed = sum(TeamPlayerValues)

    if teamPlayerSpeed >= teamEnemySpeed:
        return True
    else:
        return False


# what the allies will do on their turn
def allyAction(enemies, special):
    acounter = 0
    global alive
    # acounter is used to determine for many allies there are and that thre should only be that many turns
    while acounter < len(allyTeam):
        currentAlly = allyTeam[acounter].name
        print('\nIt is {}\'s turn, What will you do?'.format(currentAlly))
        if acounter < 2:

            # -------------------------player actions below---------------------------

            print('-(a)ttack--(i)tem--(s)pecial--(r)un-')
            allyChoice = input(''.lower())
            # if chose to attack
            if allyChoice == 'a' or allyChoice == 'attack':
                # does nothing, there will always be at least 0 enemies
                if len(enemies) > 0:
                    print('Which enemy will you attack?')
                    for counter in range(len(enemies)):
                        # lists the enemies number, name and health. Input the number you want to attack
                        print('{} :: {} with {} health'.format(counter, enemies[counter].name, enemies[counter].health))
                    choseEnemy = int(input('Enemy number: '))
                    try:
                        enemy = enemies[choseEnemy]
                        checkDecision = input('You want to attack {}? -(y)es--(n)o-'.format(enemy.name))
                        if checkDecision == 'y' or checkDecision == 'yes':
                            pAccuracy = random.randint(0, 100) - enemy.evasiveness
                            allyWeaponAttack = random.randint(allyTeam[acounter].weapon.attackMin,
                                                              allyTeam[acounter].weapon.attackMax)
                            if pAccuracy >= 10:
                                allyDamage = allyTeam[acounter].attack + allyWeaponAttack - enemy.defense
                                if allyDamage < 0:
                                    allyDamage = 0
                                print('{} attack\'s the enemy doing {} damage!'.format(currentAlly, allyDamage))
                                enemy.health -= allyDamage
                                acounter += 1
                                if enemy.health <= 0:
                                    enemy.health = enemy.healthMin
                                    print('The enemy has been defeated!')
                                    # removes the enemy from the list of active enemies
                                    enemies.remove(enemy)
                                    if len(enemies) == 0:
                                        alive = False
                                        break
                                else:
                                    print('The enemy has {} health left!'.format(enemy.health))
                            else:
                                print('You missed!')
                                acounter += 1
                        else:
                            continue
                    except:
                        print('This enemy does not exist...!')
                        continue
                elif len(enemies) == 0:
                    alive = False
                    break

            # disable defending for now
            # elif allyChoice == 'd' or allyChoice == 'defend':
            #     pass

            elif allyChoice == 'i' or allyChoice == 'item':
                item = useItem()
                # useItem() will return true or false
                if item is False:
                    continue
                else:
                    acounter += 1

            # will only show the players special abilities since heiku is not mentioned in usePlayerSpecial()
            elif allyChoice == 's' or allyChoice == 'special':
                ability = usePlayerSpecial(player)
                if ability is False:
                    continue
                else:
                    acounter += 1

            elif allyChoice == 'r' or allyChoice == 'run':
                # if special battle, cannot run away
                if special:
                    print('You cannot run from this battle!')
                    continue
                else:
                    runInt = random.randint(1, 6)
                    global teamPlayerSpeed
                    global teamEnemySpeed
                    runChance = (teamPlayerSpeed - teamEnemySpeed) * runInt
                    if runChance > teamEnemySpeed:
                        print('You have run successfully!')
                        # end the battle
                        pass
                    else:
                        print('You could not escape!')
                        acounter += 1

            else:
                # this may increase counter...
                print('Did you type that right?')
                continue

        # -----------------------Spirit actions below-------------------------

        else:
            print('-(a)ttack--(s)pecial-')
            allyChoice = input(''.lower())
            # if chose to attack
            if allyChoice == 'a' or allyChoice == 'attack':
                # does nothing, there will always be at least 0 enemies
                if len(enemies) > 0:
                    print('Which enemy will you attack?')
                    for counter in range(len(enemies)):
                        # lists the enemies number, name and health. Input the number you want to attack
                        print('{} :: {} with {} health'.format(counter, enemies[counter].name, enemies[counter].health))
                    choseEnemy = int(input('Enemy number: '))
                    try:
                        enemy = enemies[choseEnemy]
                        checkDecision = input('You want to attack {}? -(y)es--(n)o-'.format(enemy))
                        if checkDecision == 'y' or checkDecision == 'yes':
                            pAccuracy = random.randint(0, 100) - enemy.evasiveness
                            allyWeaponAttack = random.randint(currentAlly.weapon.attackMin,
                                                              currentAlly.weapon.attackMax)
                            if pAccuracy >= 10:
                                allyDamage = player.attack + allyWeaponAttack - enemy.defense
                                if allyDamage < 0:
                                    allyDamage = 0
                                print('{} attack\'s the enemy doing {} damage!'.format(currentAlly, allyDamage))
                                enemy.health -= allyDamage
                                if enemy.health <= 0:
                                    enemy.health = enemy.healthMin
                                    print('The enemy has been defeated!')
                                    # removes the enemy from the list of active enemies
                                    enemies.remove(enemy)
                                    if len(enemies) == 0:
                                        alive = False
                                        break
                                else:
                                    print('The enemy has {} health left!'.format(enemy.health))
                            else:
                                print('You missed!')
                        else:
                            continue
                    except:
                        print('This enemy does not exist...!')
                        continue
                elif len(enemies) == 0:
                    alive = False
                    break

            # disable defending for now
            # elif allyChoice == 'd' or allyChoice == 'defend':
            #     pass

            elif allyChoice == 's' or allyChoice == 'special':
                ability = usePlayerSpecial(player)
                if ability is False:
                    continue

            else:
                # this may increase counter...
                print('Did you type that right?')
                continue


# --------------------------Finished with allies-----------------------------------


# --------------------------Enemies bellow----------------------------------------

# the enemies have no strategy involved in who they attack
# they will always attack the spirits before the players
# if no spirits, then the players will be available for them to attack
def enemiesAction(enemies):
    for acounter in range(len(enemies)):
        currentEnemy = enemies[acounter].name
        print('\nIt is {}\'s turn!'.format(currentEnemy))
        # randomly pick a spirit to attack, if no spirit is available, attack a player
        allyValidTeam = allyTeam
        # if there are spirits on the battlefield, this will call and they will be attackable
        try:
            spiritDice = random.randint(2, len(allyTeam))
            eAccuracy = random.randint(0, 100) - allyValidTeam[spiritDice].evasiveness
            enemyMainAttack = random.randint(allyValidTeam[spiritDice].weapon.attackMin,
                                             allyValidTeam[spiritDice].weapon.attackMax)
            if eAccuracy >= 10:
                enemyDamage = (allyValidTeam[spiritDice].attack + enemyMainAttack) - player.defense
                if enemyDamage < 0:
                    enemyDamage = 0
                print('The enemy did {} damage to {}!'.format(enemyDamage, allyValidTeam[spiritDice].name))
                allyValidTeam[spiritDice].health -= enemyDamage
                if allyValidTeam[spiritDice].health < 0:
                    allyValidTeam[spiritDice].health = allyValidTeam[spiritDice].healthMin
                print('{} has {} health left!'.format(allyValidTeam[spiritDice].name, allyValidTeam[spiritDice].health))
            else:
                print('The enemy missed')

        # if there are no spirits on the battlefield, it will default to attacking the players
        # -----if one player is dead though, this will not handle it and an error will be raised!--------
        except:
            playerDice = random.randint(0, 1)
            eAccuracy = random.randint(0, 100) - allyValidTeam[playerDice].evasiveness
            enemyMainAttack = random.randint(allyValidTeam[playerDice].weapon.attackMin,
                                             allyValidTeam[playerDice].weapon.attackMax)
            if eAccuracy >= 10:
                enemyDamage = (allyValidTeam[playerDice].attack + enemyMainAttack) - player.defense
                if enemyDamage < 0:
                    enemyDamage = 0
                print('The enemy did {} damage to {}!'.format(enemyDamage, allyValidTeam[playerDice].name))
                allyValidTeam[playerDice].health -= enemyDamage
                if allyValidTeam[playerDice].health < 0:
                    allyValidTeam[playerDice].health = allyValidTeam[playerDice].healthMin
                print('{} has {} health left!'.format(allyValidTeam[playerDice].name, allyValidTeam[playerDice].health))
            else:
                print('The enemy missed')


# needs to incorporate that there will be more than just the player getting exp.
# maybe have modifyers and max and min exp that can be recieved for each character
# maybe a for loop that determines how many characters there are
# this also only takes into account that the player won
def battleEnd():
    # ---------FOR EXP---------------
    print('All enemies have been defeated!\n--you win!--')
    # experience cant be higher than the max, instead, it will give you a level and subtract your current from
    # the max. It is a loop in case you get many levels from one battle, it will check until true.
    for expCounter in range(len(allyTeam)):
        # determines how much experience the player will receive
        allyTeam[expCounter].exp = 10  # placeholder
        print('{} got {} experience from this battle\n'.format(allyTeam[expCounter].name, allyTeam[expCounter].exp))
        while allyTeam[expCounter].exp >= allyTeam[expCounter].expMax:
            allyTeam[expCounter].leftExp = allyTeam[expCounter].exp
            allyTeam[expCounter] -= allyTeam[expCounter].expMax
            allyTeam[expCounter].level += 1
            if allyTeam[expCounter].level + 1:
                # sets which stats to increase and increases them, also prints what your new stat is
                statIncreaseMin = 0
                statIncreaseMax = 3
                allyTeam[expCounter].attack = allyTeam[expCounter].attack + random.randint(statIncreaseMin,
                                                                                           statIncreaseMax)
                print('{}\'s attack is now: {}'.format(allyTeam[expCounter].name, allyTeam[expCounter].attack))
                allyTeam[expCounter].defense = allyTeam[expCounter].attack + random.randint(statIncreaseMin,
                                                                                            statIncreaseMax)
                print('{}\'s defense is now: {}'.format(allyTeam[expCounter].name, allyTeam[expCounter].defense))
                player.speed = player.speed + random.randint(statIncreaseMin, statIncreaseMax)
                print('{}\'s speed is now: {}'.format(allyTeam[expCounter].name, allyTeam[expCounter].speed))

            allyTeam[expCounter].exp = allyTeam[expCounter].leftExp
            print('{}\'s level is now {}!\n'.format(allyTeam[expCounter].name, allyTeam[expCounter].level))

    '''
    while player.exp >= player.expMax:
        player.leftExp = player.exp
        player.leftExp -= player.expMax
        player.playerLevel += 1
        if player.playerLevel + 1:
            # sets which stats to increase and increases them, also prints what your new stat is
            increaseLevel()
        player.exp = player.leftExp
        print('Your level is now {}!\n'.format(player.playerLevel))
    '''

# --------------OLD BATTLE SYSTEM BELOW: (updated nov12, 2016)-------------------

'''

# function is ALWAYS called outside of this script, starting the entire battle system, never called locally
# special is a bool called outside of function to determine if you can run, etc. (maybe define what kind of special)
def battleStart(enemy, special):
    global defend
    defend = False
    if special:
        special = True
    else:
        special = False
    print('You are battling {}'.format(enemy.name))
    # checks if the enemy goes first or not
    goesFirst = checkSpeed(enemy)
    # checks if the enemy goes first or not based on the return of goesFirst
    # offloads into the functions designated for it
    if goesFirst:
        dead = playerFaster(enemy, special)
        if dead:
            playerDead()
        else:
            pass
    else:
        dead = enemyFaster(enemy, special)
        if dead:
            playerDead()
        else:
            pass


def checkSpeed(enemy):
    if player.speed >= enemy.speed:
        return True
    else:
        return False


# needs work as later parts are complete
def enemyFaster(enemy, special):
    while player.health > 0 or enemy.health > 0:
        # currently there is no enemy decision manager so it can only attack, these print statements are okay here
        enemyDamage = enemyAttack(enemy)
        print('The enemy did {} damage to you!'.format(enemyDamage))
        player.health -= enemyDamage
        if player.health < 0:
            player.health = player.healthMin
            return True
        print('You have {} health left!'.format(player.health))
        # players turn
        decision = decisionManager(enemy, special)
        if decision == 'enemyDead':
            # break out of the battle
            battleEnd(enemy)
            break
        # whether run is valid or not in the battle is handled in decisionManager()
        elif decision == 'run':
            break
        elif decision == 'defend':
            global defend
            defend = True
        else:
            pass


# needs work as later parts are complete
def playerFaster(enemy, special):
    while player.health > 0 or enemy.health > 0:
        # players turn
        decision = decisionManager(enemy, special)
        if decision == 'enemyDead':
            # break out of the battle
            battleEnd(enemy)
            break
        # whether run is valid or not in the battle is handled in decisionManager()
        elif decision == 'run':
            # if you run, break out of the battle loop
            break
        elif decision == 'defend':
            global defend
            defend = True
        else:
            # if nothing special, go to the enemies turn
            pass
        # currently there is no enemy decision manager so it can only attack, these print statements are okay here
        enemyDamage = enemyAttack(enemy)
        print('The enemy did {} damage to you!'.format(enemyDamage))
        player.health -= enemyDamage
        if player.health < 0:
            player.health = player.healthMin
            return True
        print('You have {} health left!'.format(player.health))


# feeds and is called by decisionManager()
def playerDecision():
    print('What will you do?\n-attack--defend--item--special--run-')
    playerChoice = input(''.lower())
    # maybe not needed since inputs are always strings
    try:
        playerChoice = str(playerChoice)
    except ValueError:
        print('Did you type that right?')
        playerDecision()
    # will be lower() by default since it is placed in the input()
    if playerChoice == 'attack' or playerChoice == 'a':
        return 'attack'
    elif playerChoice == 'defend' or playerChoice == 'd':
        return 'defend'
    elif playerChoice == 'item' or playerChoice == 'i':
        return 'item'
    elif playerChoice == 'special' or playerChoice == 's':
        return 'special'
    elif playerChoice == 'run' or playerChoice == 'r':
        return 'run'
    else:
        print('Did you type that right?')
        return 'DEBUG: invalid input'


# manages the decisions for the battle system, all must return some value
# returns to enemy/playerFaster()
def decisionManager(enemy, special):
    playerChoice = playerDecision()
    if playerChoice == 'attack':
        Damage = playerAttack(enemy)
        print('You attack the enemy doing {} damage!'.format(Damage))
        enemy.health -= Damage
        if enemy.health < 0:
            enemy.health = enemy.healthMin
            print('The enemy is dead')
            return 'enemyDead'
        print('The enemy has {} health left!'.format(enemy.health))
    elif playerChoice == 'defend':
        return 'defend'
    elif playerChoice == 'item':
        playerItem(enemy, special)
        return 'DEBUG: generic return'
    elif playerChoice == 'special':
        playerSpecial(enemy, special)
    elif playerChoice == 'run':
        run = playerRun(enemy, special)
        if run == True and special == False:
            print('You escaped from battle!')
            return 'Run'
        elif run == True and special == True:
            print('You cannot run away from this battle!')
            decisionManager(enemy, special)
        else:
            print('You could not run away!')
            return 0
    # if invalid input from playerDecision()
    else:
        decisionManager(enemy, special)


# return a number
def playerAttack(enemy):
    pAccuracy = random.randint(0, 100) - enemy.evasiveness
    playerWeaponAttack = random.randint(player.weapon.attackMin, player.weapon.attackMax)
    if pAccuracy >= 10:
        playerDamage = player.attack + playerWeaponAttack - enemy.defense
        if playerDamage < 0:
            return 0
        return playerDamage
    else:
        print('You missed!')
        return 0


def enemyAttack(enemy):
    eAccuracy = random.randint(0, 100) - player.evasiveness
    enemyMainAttack = random.randint(enemy.attackMin, enemy.attackMax)
    # currently alter only means that the player is defending
    if eAccuracy >= 10:
        enemyDamage = (enemy.attack + enemyMainAttack) - player.defense
        if enemyDamage < 0:
            return 0
        if defend:
            print('You prepare for the enemies next attack!')
            enemyDamage = int(enemyDamage / 2)
            return enemyDamage
        return enemyDamage
    else:
        print('The enemy missed')
        return 0


# items still broken
def playerItem(enemy, special):
    item = useItem(player)
    # useItem() will return true or false
    if item is False:
        decisionManager(enemy, special)


def playerRun(enemy, special):
    runInt = random.randint(1, 6)
    runChance = (player.speed - enemy.speed) * runInt
    # if special, return True to run and decisionManager() will detect and not allow it
    if special:
        return True
    if runChance >= 10:
        return True
    else:
        return False


# make a reasoning system for why the enemy would want to run away
def enemyRun(enemy):
    runInt = random.randint(1, 6)
    runChance = (enemy.speed - player.speed) * runInt
    if runChance >= 10:
        return True
    else:
        return False


# return a number
def playerSpecial(enemy, special):
    ability = usePlayerSpecial(player)
    if ability is False:
        decisionManager(enemy, special)


def enemySpecial(enemy):
    print()


# this will be used only if the player wins
def battleEnd(enemy):
    # ---------FOR EXP---------------
    print('The enemy has been defeated!\n--you win!--')
    # determines how much experience the player will receive
    player.exp = enemy.giveExp
    print('You got {} experience from this battle'.format(player.exp))
    # experience cant be higher than the max, instead, it will give you a level and subtract your current from
    # the max. It is a 'while loop' in case you get many levels from one battle, it will check until true.
    while player.exp >= player.expMax:
        player.leftExp = player.exp
        player.leftExp -= player.expMax
        player.playerLevel += 1
        if player.playerLevel + 1:
            # sets which stats to increase and increases them, also prints what your new stat is
            increaseLevel(player)
        player.exp = player.leftExp
        print('Your level is now {}!\n'.format(player.playerLevel))
    # --------------FOR ELSE--------------------
    specialEvent()


def specialEvent():
    # none yet, not sure which event would go here, but could be recycled later for something
    pass


# not working for some reason (?)
def playerDead():
    import main
    print('\nYou died! The beginning awaits!\n\n\n\n\n\n\n\n-----------------')
    main()






# -----------------VERY OLD BATTLE SYSTEM BELOW:----------------------



# the enemy constraint is called when a battle scene is called (ex. from main.py) THe player is always the same,
# but the enemy will be different depending on the situation
def battle(enemy):
    print('You are battling: {}!'.format(enemy.name))
    while player.health >= 1 and enemy.health >= 1:
        # determines who is faster
        while player.speed >= enemy.speed:
            print('What will you do? -attack-defend-item-run-')
            playerMove = input('')
            if playerMove.lower() == 'a' or playerMove.lower() == 'attack':
                playerAttack(enemy)
                # if the enemy has lower than one health, it must be dead, and end the battle
                if enemy.health < 1:
                    enemy.health = enemy.healthMin
                    break
                print('The enemy has {} health left\n'.format(enemy.health))
                time.sleep(1)
                # ## The enemy attacks
                enemyAttack(enemy)
                # if the player has lower than one health, the player must be dead, no need to 'break' since the while
                # loop will be triggered and automatically break.
                if player.health < 1:
                    player.health = player.healthMin
                    break
                print('You have {} health left\n'.format(player.health))
                time.sleep(1)

            # currently does nothing when you select defend, what if the enemy is going first?

            elif playerMove.lower() == 'd' or playerMove.lower() == 'defend':
                print('You prepare for the enemies attack!')
                enemyLessAttack = (enemyAttack(enemy) - player.defense)
                if player.health < 1:
                    player.health = player.healthMin
                    break
                print('You have {} health left')
                time.sleep(1)

            # if player selects run

            elif playerMove.lower() == 'r' or playerMove.lower() == 'run':
                runInt = random.randint(1, 6)
                runChance = (player.speed - enemy.speed) * runInt
                if runChance >= 10:
                    print('You have run successfully!')
                    player.run = True
                    break
                else:
                    print('You could not run away!')
            elif playerMove == 'i' or playerMove == 'item':
                useItem(player)
                print('Items are currently being worked on.')
            else:
                print('\n\n\nSomething is --seriously-- broken with the attack system!\n\n\n')
                time.sleep(5)
                sys.exit('BROKEN')
        # determines who is faster -- currently if the enemy is faster, the un-updated code is run--
        while player.speed < enemy.speed:
            enemyAttack(enemy)
            # if the player has lower than one health, the player must be dead, no need to 'break' since the while loop
            # will be triggered and automatically (theoretically) break.
            if player.health < 1:
                player.health = player.healthMin
                break
            print('You have {} health left\n'.format(player.health))
            time.sleep(1)
            # ## The player attacks
            playerAttack(enemy)
            # if the enemy has lower than one health, it must be dead, and end the battle
            if enemy.health < 1:
                enemy.health = enemy.healthMin
                break
            print('The enemy has {} health left\n'.format(enemy.health))
            time.sleep(1)

    # breaking from the loop calls this:
    if player.run is True:
        player.run = False
        pass

    elif enemy.health < 1:
        print('The enemy has been defeated.')
        print('--you win!--')
        # determines how much experience the player will receive
        player.exp = enemy.giveExp
        print('You got {} experience from this battle'.format(player.exp))
        # experience cant be higher than the max, instead, it will give you a level and subtract your current from
        # the max. It is a 'while loop' in case you get many levels from one battle, it will check until true.
        while player.exp >= player.expMax:
            player.leftExp = player.exp
            player.leftExp -= player.expMax
            player.playerLevel += 1
            if player.playerLevel + 1:
                # sets which stats to increase and increases them, also prints what your new stat is
                stats.increaseLevel(player)
            player.exp = player.leftExp
            print('Your level is now {}!\n'.format(player.playerLevel))
        # resets the enemies health
        enemy.health = enemy.healthMax
        time.sleep(4)

    # If the loop breaks and the enemy was not defeated, then you must be defeated
    else:
        dead()


# the enemies attack
def enemyAttack(enemy):
    print('The enemy attacks!')
    eAccuracy = random.randint(0, 100) - player.evasiveness
    enemyMainAttack = random.randint(enemy.attackMin, enemy.attackMax)
    if eAccuracy >= 10:
        enemyDamage = (enemy.attack + enemyMainAttack) - player.defense
        if enemyDamage < 0:
            enemyDamage = 0
        player.health -= enemyDamage
        print('The enemy did {} amount of damage to you!'.format(enemyDamage))
        time.sleep(1)
    else:
        print('The enemy missed!')


# the players attack
def playerAttack(enemy):
    print('you attack!')
    pAccuracy = random.randint(0, 100) - enemy.evasiveness
    playerWeaponAttack = random.randint(player.weapon.attackMin, player.weapon.attackMax)
    if pAccuracy >= 10:
        playerDamage = player.attack + playerWeaponAttack - enemy.defense
        if playerDamage < 0:
            playerDamage = 0
        enemy.health -= playerDamage
        print('You did {} damage to the enemy!'.format(playerDamage))
        time.sleep(1)
    else:
        print('You missed!')


def dead():
    print('You have died... The beginning awaits!')
    time.sleep(4)

'''
