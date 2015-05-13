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
from CrossFade import CrossFade

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
    pygame.mixer.music.load('data/sound/menu.wav')
    pygame.mixer.music.play(-1)
    pygame.display.set_caption("(Beta) No More Pixies")
    main_loop = True
    first = True
    level_dif = "" #difficulty level chosen
    player = None #character chosen
    level_nbr = 0 #level number chosen
    slot = '' #choix de la sauvegarde
    # nmp_data = Data("gamedata.txt")
    nmp_data = Data("gamedata.noob") #slot A has everything already unlocked for dev purpose
    choices = None #choices for the different menus

    while main_loop:
        if constants.GAME_STATUS == "menuDiff":
            from DifficultyMenu import DifficultyMenu

            #DIFFICULTY SELECTION MENU
            background_image = pygame.image.load("data/back.jpg").convert()
            background_image= pygame.transform.scale(background_image, (constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
            screen.blit(background_image, [0, 0])
            menu = DifficultyMenu()
            choices=[]
            if nmp_data.save[nmp_data.selected_slot]['easy']['unlocked']:
                choices.append('Newborn')
            if nmp_data.save[nmp_data.selected_slot]['medium']['unlocked']:
                choices.append('Little Boy')
            if nmp_data.save[nmp_data.selected_slot]['hard']['unlocked']:
                choices.append('Kickass')

            menu.init(choices, screen)
            menu.draw()
            fade = CrossFade(screen)
            fade.fade(screen, 20)
            pygame.key.set_repeat(199,69)#(delay,interval)
            pygame.display.update()
            level_dif = menu.run(joystick)
            nmp_data.selected_diff = level_dif

        elif constants.GAME_STATUS == "menuChar":
            from characters.Bob import Bob
            from characters.Hulk import Hulk
            from characters.LittleFat import LittleFat
            from CharacterMenu import CharacterMenu

            #CHARACTER SELECTION MENU
            menu = CharacterMenu(screen,nmp_data)
            fade = CrossFade(screen)
            fade.fade(screen, 20)
            selected = menu.run(joystick)
            # player = None
            if selected == 0:
                player = Hulk()
                nmp_data.selected_char = 'hulk'
            elif selected == 1:
                player = Bob()
                nmp_data.selected_char = 'bob'
            elif selected == 2:
                player = LittleFat()
                nmp_data.selected_char = 'little_fat'

        elif constants.GAME_STATUS == "menuLevel":
            #LEVEL SELECTION MENU
            from LevelMenu import LevelMenu
            background_image = pygame.image.load("data/back.jpg").convert()
            background_image= pygame.transform.scale(background_image, (constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
            screen.blit(background_image, [0, 0])
            menu = LevelMenu()

            choices_levels = nmp_data.save[nmp_data.selected_slot][nmp_data.selected_diff][nmp_data.selected_char]['levels']
            choices = []
            for l_choice in choices_levels:
                if l_choice == 0:
                    choices.append('Stage 1')
                if l_choice == 1:
                    choices.append('Stage 2')
                if l_choice == 2:
                    choices.append('Stage 3')
                if l_choice == 3:
                    choices.append('Dragon')
            menu.init(choices, screen)
            menu.draw()
            pygame.key.set_repeat(199,69)#(delay,interval)
            pygame.display.update()
            menu_position = None
            menu_position = menu.run(joystick)
            fade = CrossFade(screen)
            fade.fadeout(screen, 15)
            if not menu_position == None:
                level_nbr = nmp_data.save[nmp_data.selected_slot][nmp_data.selected_diff][nmp_data.selected_char]['levels'][menu_position]

        elif constants.GAME_STATUS == "level":
            from Game import Game
            # Create all the levels
            game = Game(player,level_nbr,level_dif,screen,joystick,nmp_data)
            game.run()

        elif constants.GAME_STATUS == "menuSave":
            from SaveMenu import SaveMenu
            background_image = pygame.image.load("data/back.jpg").convert()
            background_image= pygame.transform.scale(background_image, (constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
            screen.blit(background_image, [0, 0])
            menu = SaveMenu()
            slot_list = []
            for key in ['A','B','C']:
                if not nmp_data.save[key]['used']:
                    slot_list.append("Slot "+key)
                else:
                    slot_list.append("Progress : "+nmp_data.stats(key)+"%")
            #menu.init(['Slot A','Slot B','Slot C'], screen)
            menu.init(slot_list, screen)
            menu.draw()
            fade = CrossFade(screen)
            fade.fade(screen, 20)
            pygame.key.set_repeat(199,69)#(delay,interval)
            pygame.display.update()
            slot = menu.run(joystick)
            if slot != None:#when nothing has been selected (ex: going back in menu)
                nmp_data.selected_slot = slot
                nmp_data.save[slot]['used'] = True
                nmp_data.save_data()

        elif constants.GAME_STATUS == "menu":
            from Menu import Menu
            background_image = pygame.image.load("data/back.jpg").convert()
            background_image= pygame.transform.scale(background_image, (constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
            screen.blit(background_image, [0, 0])
            menu = Menu()
            menu.init(['Start','Quit'], screen)
            menu.draw()
            fade = CrossFade(screen)
            fade.fade(screen, 20)
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
