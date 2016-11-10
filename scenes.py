# scenes.py

# USED BY: main.py

import time
# import threading  # for testing, not implemented yet
import shelve  # for saving and loading
import sys
import os
import winsound
from player import *
from enemy import *
from battle import battleStart
from colorama import init, Fore, Back, Style
# Initialize colorama
init(convert=False, strip=False)

# <editor-fold desc="--How to use colorama--">
'''
Fore: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
Back: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
Style: DIM, NORMAL, BRIGHT, RESET_ALL
'''
# </editor-fold>


# defines what level the player is on
class LevelManager:
    scene = 0
    sceneOneRoomManager = 0
    sceneTwoRoomManager = 0
levelM = LevelManager()


# <editor-fold desc="--Names for dialogue--">
# master class of names, all names should be a new class
class Names:
    def __init__(self, name):
        self.name = name


# keep for testing purposes
class Test(Names):
    def __init__(self):
        super().__init__(name='test')
test = Test().name


class Sys(Names):
    def __init__(self):
        super().__init__(name='system')
system = Sys().name


class Heiku(Names):
    def __init__(self):
        super().__init__(name='heiku')
heiku = Heiku().name


class Player(Names):
    def __init__(self):
        super().__init__(name=player.name)
xplayer = Player().name


class Elder(Names):
    def __init__(self):
        super().__init__(name='elder')
elder = Elder().name

# </editor-fold>

# set 'nl', etc. to a string to be passed to xprint() for easy writability
pr = str('[pr]')
nl = str('[nl]')
ss = str('[ss]')
sp = str('[sp]')
clr = str('[clr]')


def sceneLoad():
    xload()


# <editor-fold desc="--Scene Initial--">
def sceneInitial():
    parseText('text\sceneInitial.txt')
# </editor-fold>


# <editor-fold desc="--Scene Zero Function--">
def sceneZero():
    parseText('text/sceneZero.txt')
# </editor-fold>


# <editor-fold desc="--Scene One Function--">
def sceneOne():
    xsave()
    xprint(system, 'You arrive at the council chamber, no one else has arrived yet.', nl)
    # local variables
    look = 0
    search = 0
    global sword
    sword = 0

    while True:
        xprint(system, 'What will you do?', pr)
        xprint(system, '-look--search--wait-', pr)
        imp = input('')
        # decisions that can be made, the outcome changes whether you have done the action already
        if (imp == 'l' or imp == 'look') and look == 0:
            xprint(system, 'You look around the building. You are in a large stone building with stone pillars '
                           'supporting the ceiling. There is a round wooden table in the center with engraved '
                           'mohogany chairs surrounding it.', nl)
            look += 1
        elif (imp == 'l' or imp == 'look') and look > 0:
            xprint(system, 'You are in a large stone building.', nl)
        elif (imp == 's' or imp == 'search') and search == 0:
            xprint(system, 'You search the room. There are a lot of ornamental swords hanging on the wall and gold '
                           'coins scattered on the table. There is a small chest in the corner of the room.', nl)
            xprint(system, 'will you open it? -yes--no-', pr)
            sceneOneSearch = input(''.lower())
            if sceneOneSearch == 'y' or sceneOneSearch == 'yes':
                xprint(system, 'You walk towards the chest and open the heavy lid. Inside you find a fine sword. '
                               'You pick up its sheath and strap it to your back.', nl)
                sword += 1
                search += 1
            else:
                xprint(system, 'You decide not to open the chest.', nl)
                search += 1
        elif (imp == 's' or imp == 'search') and search > 0 and sword == 0:
            xprint(system, 'Will you open the chest?', pr)
            sceneOnesearch = input(''.lower())
            if sceneOnesearch == 'y' or sceneOnesearch == 'yes':
                xprint(system, 'You walk towards the chest and open the heavy lid. Inside you find a decorated sword. '
                               'You pick up its sheath and strap it to your back.', nl)
                # adds teh sword to the players inventory
                itemGet(player, ceremonial_sword)
                # equips it automatically
                player.weapon = ceremonial_sword
                # for manager
                sword += 1
            else:
                xprint(system, 'You decide not to open the chest.', nl)
        elif (imp == 's' or imp == 'search') and sword > 0:
            xprint(system, 'You have searched here already.', nl)
        elif imp == 'w' or imp == 'wait':
            xprint(system, 'You decide to wait for the elders to arrive.', nl)
            # breaks out back to main with the scene increasing
            break
        else:
            xprint(system, 'Did you type that right?', nl)
            continue

# </editor-fold>


def sceneTwo():
    global sword
    parseText('text/sceneTwoBeginning.txt')
    # only the sword has a max attack of over 10 at this point ----broken-----
    if sword >= 1:
        xprint(system, 'You are glad you found the sword in the chest as you march out for battle', nl)
    else:
        xprint(system, 'You find a large rock on the ground and equip yourself.', nl)
    battleStart(shadow, True)  # battle start, enemy is shadow, its a special battle(no running)
    time.sleep(2)
    parseText('text/sceneTwoFinish.txt')


def sceneThree():
    pass


# <editor-fold desc="--dead()--">
# local version of dead, if dead without battle
def dead():
    print('You died')
    time.sleep(2)
    sys.exit('exiting')
# </editor-fold>


# <editor-fold desc="--Text parser--">
# parses the text file, reads the number of lines, splits it into parts of a list, and passes them into xprint()
# may only be useful for long dialogues
# --> could be set up to check for other features in the text that would signal it to stop, skip, etc.
def parseText(text):

    # calculates how many lines there are in the text
    def fileLen(text):
        lines = 0
        for line in open(text):
            lines += 1
        # returned as value of lineNum
        return lines

    data = open(text)
    # value from fileLen(text)
    lineNum = fileLen(text)
    # starting on line 0
    lineOn = 0
    # takes a line and splits it into parts of a list and passes them into xprint()
    for line in data:
        if lineOn >= lineNum:
            break
        time.sleep(0.1)
        x = line.split('; ')
        # splitting the string will give the last item in the list '\n', this gets rid of any '\n's
        x = [w.replace('\n', '') for w in x]
        # this is where it is actually printed to the screen:
        xprint(str(x[0]), str(x[1]), str(x[2]), lineOn, text)
        lineOn += 1
    data.close()
    return
# </editor-fold>


# <editor-fold desc="--xprint(names, lines, inp) function--">
# modified print statement with colour
def xprint(name, lines, inp, textLine=0, sourceScript='scenes.py'):
    PRINT_SPEED = 0.03
    # used to make sure that the coloured print is completed before continuing
    PAUSE = 0.01
    LINE_SLEEP = 2

    '''Checks to see if a name is valid and gives its assigned colours'''

    # determines the colour based the name input, if no name of that type, an error is raised
    def choseColour():
        if name == 'false':
            return None
        elif name == 'test':
            return Back.WHITE
        elif name == 'system':
            return Back.GREEN
        elif name == 'heiku':
            return Back.CYAN
        elif name == 'player':
            return Back.BLUE
        elif name == 'elder':
            return Back.YELLOW
        else:
            # raises an error if the name in teh text does not exist and tells which line the name was found in the text
            # makes it easy to debug miss-spelled names or names that were not properly defined first.
            raise Exception('DEBUG: error; no character defined with name -{}- in xprint in text line: {}'
                            ' in {}'.format(name, textLine+1, sourceScript))

    def colourMain():
        colour = choseColour()
        # if returned 'None', then no name is defined and there is no colour to put onto it
        if colour is None:
            pass
        # takes in the return of choseColour() and adds it to the colour script as well aas the name
        # the name is taken from this instance of xprint()
        else:
            print(colour + name + Style.RESET_ALL + ': ', end='')
            time.sleep(PAUSE)
    # starts the coloured name functions
    colourMain()

    '''used to determine how to display "lines" from the text'''

    # currently not working, needs to do two things at once:
    # check for input and return, OR wait for the timer and continue --- threading---
    # def waitPrint():
    #     xInput = True
    #     timeLimitMax = 0.001
    #     while xInput is True:
    #         timeLimit = time.sleep(0.0001)
    #         if timeLimit >= timeLimitMax:
    #             break
    #         x = input('')

    # currently only 'nl' and 'sp' works properly (?)
    if inp == '[nl]':
        for letter in lines:
            sys.stdout.write(letter)
            sys.stdout.flush()
            time.sleep(PRINT_SPEED)
        input()
        # plays a sound when a key is pressed
        winsound.PlaySound('sound/dialogue1.wav', winsound.SND_ASYNC)
    # regular print
    elif inp == '[pr]':
        print(lines)
    # sleep skip
    elif inp == '[ss]':
        for letter in lines:
            sys.stdout.write(letter)
            sys.stdout.flush()
            time.sleep(PRINT_SPEED)
        print('\n\n\n')
        time.sleep(LINE_SLEEP)
        input()
    # sleep print
    elif inp == '[sp]':
        for letter in lines:
            sys.stdout.write(letter)
            sys.stdout.flush()
            time.sleep(PRINT_SPEED)
    # clears only the line that was supposed to be printed
    # wanted it to clear the screen then print the current line
    elif inp == '[clr]':
        os.system('cls')
    else:
        pass
        raise Exception('DEBUG: error; no inp of {} in xprint'.format(inp))
# </editor-fold>


# FIXED save system currently is now working, old error below:
# Error::: AttributeError: 'str' object has no attribute 'name'
# seems that it is treating 'player' as a string and not a class name
# FIXED 'player' was calling the class name of player used in dialogue! changed its name to 'xplayer' :D
def xsave():
    try:
        # save player values
        shelfFile = shelve.open('save/saveFile1')
        shelfFile['pName'] = player.name
        shelfFile['pHealth'] = player.health
        shelfFile['pHealthMax'] = player.healthMax
        shelfFile['pAttack'] = player.attack
        shelfFile['pWeaponEquip'] = player.weapon
        shelfFile['pDefense'] = player.defense
        shelfFile['pSpeed'] = player.speed
        shelfFile['pLevel'] = player.playerLevel
        shelfFile['pExp'] = player.exp
        shelfFile['pMoney'] = player.money
        shelfFile['pEvasion'] = player.evasiveness
        shelfFile['pCurrentInventory'] = player.inventory
        shelfFile['pCurrentSpecial'] = player.special
        # save level values
        shelfFile['lSceneMain'] = LevelManager.scene
        shelfFile['lSceneOneRoomM'] = LevelManager.sceneOneRoomManager
        shelfFile['lSceneTwoRoomM'] = LevelManager.sceneTwoRoomManager
        shelfFile.close()

        # print success message
        xprint(system, '--Your game was successfully saved!--', pr)

    # if error on saving the game, this will be displayed
    except:
        xprint(system, '--DEBUG: error; could not save game!--', pr)


def xload():
    try:
        # load player values
        shelfFile = shelve.open('save/saveFile1')
        player.name = shelfFile['pName']
        player.health = shelfFile['pHealth']
        player.healthMax = shelfFile['pHealthMax']
        player.attack = shelfFile['pAttack']
        player.weapon = shelfFile['pWeaponEquip']
        player.defense = shelfFile['pDefense']
        player.speed = shelfFile['pSpeed']
        player.playerLevel = shelfFile['pLevel']
        player.exp = shelfFile['pExp']
        player.money = shelfFile['pMoney']
        player.evasiveness = shelfFile['pEvasion']
        player.inventory = shelfFile['pCurrentInventory']
        player.special = shelfFile['pCurrentSpecial']
        # load level values
        LevelManager.scene = shelfFile['lSceneMain']
        LevelManager.sceneOneRoomManager = shelfFile['lSceneOneRoomM']
        LevelManager.sceneTwoRoomManager = shelfFile['lSceneTwoRoomM']
        shelfFile.close()

        # print success message
        xprint(system, '--Your game was loaded successfully!--', pr)

    # if error loading the game, will crash it giving this error:
    except:
        raise Exception('DEBUG: error; Could not load file!')
