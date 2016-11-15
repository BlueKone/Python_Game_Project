# main: EXtring pyo-gen

# This is the main script for the text based game
# this script should be used to 'freeze/compile' the program

# USING: scenes.py

# text based game start
from scenes import *


# for determining where you are in the game, ties directly with the level manager
def main():
    print('======================================\n')
    print('Sara\'i Ishe     version 0.03')
    print('For the manual, press -m-\nFor the list of bugs to avoid, press -b-\n')
    print('To load a game, press -l-\n')
    print('Press anything else to play!')
    print('======================================\n')
    start = input('')
    if start == 'm' or start == 'manual':
        input('========MANUAL========\n\n'
              'As lines are displayed, wait for them to end and press the enter key.\n'
              'More instructions are available as you progress.'
              '==Press enter to exit the manual==')
        main()
    elif start == 'b' or start == 'bugs':
        input('==========BUG-LIST=============\n'
              '====As of version 0.02====\n'
              'In battle, you can use items, but there will be no effect by doing so. Don\'t use them.\n'
              'As the text is displaying, you can enter key strokes. Don\'t do this. Just wait patiently for the text '
              'to finish, then enter a key.\n'
              'In battle, the ally team cannot lose, unknown results will occur if they do. Don\'t lose!\n'
              'Currently, the save may or may not work. You can try loading your game, but try at your own risk!.'
              'Other bugs may be present, further testing is currently underway.\n'
              '==Press enter to exit this menu==\n')
        main()
    elif start == 'l' or start == 'load':
        sceneLoad()
        pass
    else:
        print('=====================\nNEW GAME\n\n')
        pass

    while levelM.scene < 100:
        # this is for testing
        if levelM.scene == -2:
            pass  # add test code here
        elif levelM.scene == 0:
            sceneInitial()
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
        elif levelM.scene == 4:
            sceneFour()
            levelM.scene += 1
        else:
            raise Exception('DEBUG: error; no scene after this exists.')

main()
