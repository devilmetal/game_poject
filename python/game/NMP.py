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


def pause(clock,screen):
    """ Pausing the game """
    pause_flag = True
    font_path_title = 'data/coders_crux/coders_crux.ttf'
    font1 = pygame.font.Font(font_path_title, 52)
    font2 = pygame.font.Font(font_path_title, 42)
    text1 = font1.render("Paused", 1, constants.WHITE)
    text2 = font2.render("Continue (c) or Quit (q) ?", 1, constants.WHITE)
    text1pos = text1.get_rect()
    text2pos = text2.get_rect()
    text1pos.centerx = constants.SCREEN_WIDTH/2
    text1pos.centery = constants.SCREEN_HEIGHT/2 - 20
    text2pos.centerx = constants.SCREEN_WIDTH/2
    text2pos.centery = constants.SCREEN_HEIGHT/2 + 20

    screen.blit(text1, text1pos)
    screen.blit(text2, text2pos)

    screen.blit(screen, (0,0))
    pygame.display.update()
    while pause_flag:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    pause_flag = False
                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()
        clock.tick(60)


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
            from characters.Bob import Bob
            from platforms.Platform import Platform
            from platforms.MovingPlatform import MovingPlatform
            from levels.Level1 import Level_01
            #from levels.Level2 import Level_02
            from levels.FirstStage import FirstStage

            # Create the player
            player = Bob()

            # Create all the levels
            level_list = []
            level_list.append(FirstStage(player))
            #level_list.append(Level_02(player))

            # Set the current level
            current_level_no = 0
            current_level = level_list[current_level_no]

            active_sprite_list = pygame.sprite.Group()
            player.level = current_level

            player.rect.x = current_level.start_x
            player.rect.y = current_level.start_y
            active_sprite_list.add(player)

            #Loop until the user clicks the close button.
            done = False

            # Used to manage how fast the screen updates
            clock = pygame.time.Clock()
            #Play audio stuff
            pygame.mixer.music.load('data/sound/test.wav')
            pygame.mixer.music.play(-1)
            # -------- Main Program Loop -----------
            while not done:

                # Update the player.
                active_sprite_list.update()
                # Update items in the level
                current_level.update()
                #if the player is dead
                if player.dead == True:
                    done = True
                # If the player gets near the right side, shift the world left (-x)
                if player.rect.right >= 300:
                    diff = player.rect.right - 300
                    player.rect.right = 300
                    current_level.shift_world(-diff)

                # If the player gets near the left side, shift the world right (+x)
                if player.rect.left <= 300:
                    diff = 300 - player.rect.left
                    player.rect.left = 300
                    current_level.shift_world(diff)

                #SHIFT THE WORLD
                current_position = player.rect.x + current_level.world_shift

                # If the player gets to the end of the level, go to the menu title
                if current_position < current_level.level_limit:
                    constants.GAME_STATUS = "menu"
                    done = True
                    print constants.GAME_STATUS



                # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
                current_level.draw(screen)
                active_sprite_list.draw(screen)

                # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT


                for event in pygame.event.get(): # User did something

                    #Joystick stuff
                    if event.type == pygame.JOYHATMOTION:
                        hat = str(joystick.get_hat(0))
                        if "(-1, 0)" in hat:
                            player.go_left()
                        if "(1, 0)" in hat:
                            player.go_right()
                        if "(0, 0)" in hat and player.change_x != 0:
                            player.stop()

                    if event.type == pygame.JOYBUTTONDOWN:
                        if joystick.get_button(0) == 1:
                            player.jump()

                    #Keyboard stuff
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
                        if event.key == pygame.K_p:
                            pause(clock,screen)

                    if event.type == pygame.KEYUP:
                        if event.key == pygame.K_LEFT and player.change_x < 0:
                            player.stop()
                        if event.key == pygame.K_RIGHT and player.change_x > 0:
                            player.stop()

                # Limit to 60 frames per second
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

                    #Joystick stuff
                    if event.type == pygame.JOYHATMOTION:
                        hat = str(joystick.get_hat(0))
                        if "(0, 1)" in hat:
                            menu.draw(-1)
                        if "(0, -1)"in hat:
                            menu.draw(1)
                        pygame.display.update()
                    if event.type == pygame.JOYBUTTONDOWN:
                        if joystick.get_button(0) == 1:
                            if menu.get_position() == 1:#here is the Menu class function
                                constants.GAME_STATUS="exit"
                                menu_flag = False
                            if menu.get_position() == 0:#here is the Menu class function
                                constants.GAME_STATUS="level"
                                menu_flag = False


                    #Keyboard stuff
                    if event.type == pygame.KEYDOWN: # or event.type == pygame.JOYHATMOTION or event.type == pygame.JOYBUTTONDOWN:
                        if event.key == pygame.K_UP:# or joystick.get_hat()==(0,1):
                            menu.draw(-1) #here is the Menu class function
                        if event.key == pygame.K_DOWN:# or joystick.get_hat()==(0,-1):
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
