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

    while main_loop:
        if constants.GAME_STATUS == "level":
            from Game import Game
            from characters.Bob import Bob
            from characters.Hulk import Hulk
            from CharacterMenu import CharacterMenu

            #CHARACTER SELECTION MENU
            menu = CharacterMenu(screen)
            selected = menu.run(joystick)
            player = None
            if selected == 0:
                player = Bob()
            elif selected == 1:
                player = Hulk()

            level_nbr = 0
            # Create all the levels
            game = Game(player,level_nbr,screen,joystick)
            game.run()
        elif constants.GAME_STATUS == "menu":

            from Menu import Menu
            background_image = pygame.image.load("data/back.jpg").convert()
            screen.blit(background_image, [0, 0])
            menu = Menu()#necessary
            #menu.set_colors((255,255,255), (0,0,255), (0,0,0))#optional
            #menu.set_fontsize(64)#optional
            #menu.set_font('data/couree.fon')#optional
            #menu.move_menu(100, 99)#optional
            menu.init(['Start','Quit'], screen)#necessary
            #menu.move_menu(0, 0)#optional
            menu.draw()#necessary
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
