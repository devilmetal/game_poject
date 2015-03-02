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
def main():
    """ Main Program """
    pygame.init()

    # Set the height and width of the screen
    size = [constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("Animated Platformer")
    main_loop = True
    while main_loop:
        if constants.GAME_STATUS == "level":
            from Player import Player
            from Platform import Platform
            from MovingPlatform import MovingPlatform
            from levels.Level1 import Level_01
            from levels.Level2 import Level_02
            # Create the player
            player = Player()

            # Create all the levels
            level_list = []
            level_list.append(Level_01(player))
            #level_list.append(Level_02(player))

            # Set the current level
            current_level_no = 0
            current_level = level_list[current_level_no]

            active_sprite_list = pygame.sprite.Group()
            player.level = current_level

            player.rect.x = 340
            player.rect.y = constants.SCREEN_HEIGHT - player.rect.height
            active_sprite_list.add(player)

            #Loop until the user clicks the close button.
            done = False

            # Used to manage how fast the screen updates
            clock = pygame.time.Clock()

            # -------- Main Program Loop -----------
            while not done:

                # Update the player.
                active_sprite_list.update()
                # Update items in the level
                current_level.update()

                # If the player gets near the right side, shift the world left (-x)
                if player.rect.right >= 500:
                    diff = player.rect.right - 500
                    player.rect.right = 500
                    current_level.shift_world(-diff)

                # If the player gets near the left side, shift the world right (+x)
                if player.rect.left <= 120:
                    diff = 120 - player.rect.left
                    player.rect.left = 120
                    current_level.shift_world(diff)

                # If the player gets to the end of the level, go to the next level
                current_position = player.rect.x + current_level.world_shift
                if current_position < current_level.level_limit:
                    player.rect.x = 120
                    if current_level_no < len(level_list)-1:
                        current_level_no += 1
                        current_level = level_list[current_level_no]
                        player.level = current_level

                # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
                current_level.draw(screen)
                active_sprite_list.draw(screen)

                # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT

                # Limit to 60 frames per second

                for event in pygame.event.get(): # User did something
                    if event.type == pygame.QUIT: # If user clicked close
                        done = True # Flag that we are done so we exit this loop
                        main_loop = False #exit main program loop

                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_LEFT:
                            player.go_left()
                        if event.key == pygame.K_RIGHT:
                            player.go_right()
                        if event.key == pygame.K_UP:
                            player.jump()

                    if event.type == pygame.KEYUP:
                        if event.key == pygame.K_LEFT and player.change_x < 0:
                            player.stop()
                        if event.key == pygame.K_RIGHT and player.change_x > 0:
                            player.stop()

                clock.tick(60)

                # Go ahead and update the screen with what we've drawn.
                pygame.display.flip()
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
            menu_flag = True
            while menu_flag:
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_UP:
                            menu.draw(-1) #here is the Menu class function
                        if event.key == pygame.K_DOWN:
                            menu.draw(1) #here is the Menu class function
                        if event.key == pygame.K_RETURN:
                            if menu.get_position() == 1:#here is the Menu class function
                                constants.GAME_STATUS="exit"
                                menu_flag = False
                            if menu.get_position() == 0:#here is the Menu class function
                                constants.GAME_STATUS="level"
                                menu_flag = False
                        if event.key == pygame.K_ESCAPE:
                            menu_flag = False
                            main_loop = False
                        pygame.display.update()
                    elif event.type == pygame.QUIT:
                        constants.GAME_STATUS="exit"
                        menu_flag = False
                pygame.time.wait(8)
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
