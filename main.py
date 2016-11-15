# This is the main script for a simple text based game
# this script should be used to 'freeze/compile' the program

# USING: battle, scene, enemy

# currently, there is in the program:
# - a simple battle system.
# - a level manager that records which level the player is on.
# - a main() function that holds all the level calling data


# text based game
from scenes import *


# for determining where you are in the game, ties directly with the level manager
def main():
    print('======================================')
    print('Sera\'i Ishe     version 0.02')
    print('For the manual, press -m-\nFor the list of bugs to avoid, press -b-\n')
    print('To load a game, press -l-\n')
    print('Press anything else to play!')
    print('======================================')
    start = input('')
    if start == 'm' or start == 'manual':
        input('========MANUAL========\n\n'
              'As lines are displayed, wait for them to end and press any key.\n'
              'More instructions are available as you progress.'
              '==Press any key to exit the manual==')
        main()
    elif start == 'b' or start == 'bugs':
        input('==========BUG-LIST============='
              '====As of version 0.02====\n'
              'In battle, you can use items, but there will be no effect by doing so. Don\'t use them.\n'
              'As the text is displaying, you can enter key strokes. Don\'t do this. Just wait patiently for the text '
              'to finish, then enter a key.\n'
              'other bugs may be present, further testing is currently underway.\n'
              '==Press any key to exit this menu==')
        main()
    elif start == 'l' or start == 'load':
        sceneLoad()
        pass
    else:
        pass
    while levelM.scene < 100:
        # this is for testing
        if levelM.scene == -2:
            pass  # add test code here
        elif levelM.scene == -1:
            sceneInitial()
            levelM.scene += 1
        elif levelM.scene == 0:
            sceneZero()
            levelM.scene += 1
        elif levelM.scene == 1:
            sceneOne()
            levelM.scene += 1
        elif levelM.scene == 2:
            sceneTwo()
            levelM.scene += 1
        elif levelM.scene == 3:
            sceneThree()
            levelM.scene += 1
        else:
            raise Exception('DEBUG: error; no scene after this exists.')

main()
