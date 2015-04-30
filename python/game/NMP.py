"""
Sample Python/Pygame Programs
Simpson College Computer Science
http://programarcadegames.com/
http://simpson.edu/computer-science/

From:
http://programarcadegames.com/python_examples/f.php?file=platform_scroller.py

Explanation video: http://youtu.be/QplXBw_NK5Y

Part of a series:
http://programarcadegames.com/python_examples/f.php?file=move_with_walls_example.py
http://programarcadegames.com/python_examples/f.php?file=maze_runner.py
http://programarcadegames.com/python_examples/f.php?file=platform_jumper.py
http://programarcadegames.com/python_examples/f.php?file=platform_scroller.py
http://programarcadegames.com/python_examples/f.php?file=platform_moving.py
http://programarcadegames.com/python_examples/sprite_sheets/

"""

import pygame
import os
import constants
import sys
from Data import Data

constants.GAME_STATUS = "menu" #menu, char_select, level_selct, level
pygame.joystick.init()
joystick=None
if pygame.joystick.get_count() >0:
    joystick=pygame.joystick.Joystick(0)
    joystick.init()
    print "Joystick "+joystick.get_name()+" ready to use"



def main():
    """ Main Program """
    pygame.init()

    # Set the height and width of the screen
    size = [constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("(Alpha) No More Pixies")
    main_loop = True
    first = True
    level_dif = "" #difficulty level chosen
    player = None #character chosen
    level_nbr = 0 #level number chosen
    slot = '' #choix de la sauvegarde
    # nmp_data = Data("gamedata.txt")
    nmp_data = Data("gamedata_dev.txt", "A,0,2,6,2\nB,0,0,6,0\nC,1,1,6,1\n") #slot A has everything already unlocked for dev purpose
    choices = None #choices for the different menus

    while main_loop:
        if constants.GAME_STATUS == "menuDiff":
            from DifficultyMenu import DifficultyMenu

            #DIFFICULTY SELECTION MENU
            background_image = pygame.image.load("data/back.jpg").convert()
            screen.blit(background_image, [0, 0])
            menu = DifficultyMenu()

            if nmp_data.unlocked_skills == 0:
                choices = ['Newborn']
            elif nmp_data.unlocked_skills == 1:
                choices = ['Newborn','Little Boy']
            else:
                choices = ['Newborn','Little Boy','Kick Ass']

            menu.init(choices, screen)
            menu.draw()
            pygame.key.set_repeat(199,69)#(delay,interval)
            pygame.display.update()
            level_dif = menu.run(joystick)

        elif constants.GAME_STATUS == "menuChar":
            from characters.Bob import Bob
            from characters.Hulk import Hulk
            from characters.LittleFat import LittleFat
            from CharacterMenu import CharacterMenu

            #CHARACTER SELECTION MENU
            menu = CharacterMenu(screen,nmp_data.unlocked_chars)
            selected = menu.run(joystick)
            # player = None
            if selected == 0:
                player = Hulk()
            elif selected == 1:
                player = Bob()
            elif selected == 2:
                player = LittleFat()

            if player != None:
                player.lives = nmp_data.remaining_lives

        elif constants.GAME_STATUS == "menuLevel":
            #LEVEL SELECTION MENU
            from LevelMenu import LevelMenu
            background_image = pygame.image.load("data/back.jpg").convert()
            screen.blit(background_image, [0, 0])
            menu = LevelMenu()

            if nmp_data.unlocked_stages == 0:
                choices = ['Level 1']
            elif nmp_data.unlocked_stages == 1:
                choices = ['Level 1','Level 2']
            else:
                choices = ['Level 1','Level 2','Level 3']

            menu.init(choices, screen)
            menu.draw()
            pygame.key.set_repeat(199,69)#(delay,interval)
            pygame.display.update()
            level_nbr = menu.run(joystick)

        elif constants.GAME_STATUS == "level":
            from Game import Game
            # Create all the levels
            game = Game(player,level_nbr,level_dif,screen,joystick,nmp_data)
            game.run()

        elif constants.GAME_STATUS == "menuSave":
            from SaveMenu import SaveMenu
            background_image = pygame.image.load("data/back.jpg").convert()
            screen.blit(background_image, [0, 0])
            menu = SaveMenu()
            menu.init(['Slot A','Slot B','Slot C'], screen)
            menu.draw()
            pygame.key.set_repeat(199,69)#(delay,interval)
            pygame.display.update()
            slot = menu.run(joystick)
            nmp_data.slot = slot
            nmp_data.load_data()#prepare the data to load for other menus

        elif constants.GAME_STATUS == "menu":
            from Menu import Menu
            background_image = pygame.image.load("data/back.jpg").convert()
            screen.blit(background_image, [0, 0])
            menu = Menu()
            menu.init(['Start','Quit'], screen)
            menu.draw()
            pygame.key.set_repeat(199,69)#(delay,interval)
            pygame.display.update()
            menu.run(joystick)
        # Be IDLE friendly. If you forget this line, the program will 'hang'
        # on exit.
        #can pass when GAME_STATUS is f.e set to "exit"
        else:
            main_loop = False

    #Friendly Goodbye message + credits
    print " "
    print "Goodbye fellow user !"
    print "We hope you had fun."
    print " "
    print "\tCredits"
    print "\t======="
    print " "
    print "\tMain developpers:"
    print "\t-----------------"
    print ""
    print "\tAebischer Nadia"
    print '\tChammartin Jerome'
    print "\tLuyet Gil"
    print " "
    print "This software make use of a huge number of open-source part of code/assets."
    print "We would like to thanks all the person that had ever contributed to the open-source world."
    pygame.quit()

if __name__ == "__main__":
    main()
