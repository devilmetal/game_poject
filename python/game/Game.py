import pygame
import constants
import routines
import random
from levels.FirstStage import FirstStage
from levels.SecondStage import SecondStage
from levels.Boss1 import Boss1
HEIGHT = constants.SCREEN_HEIGHT-20
TAUNTS = ["You're still not skilled enough...","Try again, noob !","Come on !","Do you want to have a rest ?","You may need to lower the difficulty... noob !","Even my grandmother is more skilled than you !","What the f**k did you do ?","You know... Maybe you should give up...","You are more dying than playing bro !","Hahahahahaha ! XD","So close... but so far !","Man... seriously ?"]
class Game():
    # Lists of sprites used in all levels. Add or remove
    # lists as needed for your game.
    character = None
    level = None
    active_sprite_list = pygame.sprite.Group()
    screen = None
    start_x = 0
    start_y = 0
    current_level_nbr = 0
    level_dif = 0
    done = False
    checkpoint = False
    joystick=None
    level_dif = "easy"

    def __init__(self, character, level_nbr, level_dif, screen, joystick):
        self.screen = screen
        self.character = character
        self.level_dif = level_dif
        self.init_level(level_nbr, level_dif)
        self.current_level_nbr = level_nbr
        self.joystick = joystick
        self.taunts = TAUNTS
    def init_level(self, level_nbr, level_dif):
        if level_nbr == 0:
            if not self.checkpoint:
                self.start_x = 350
                self.start_y = HEIGHT - self.character.rect.height
            self.level = FirstStage(self.character, level_dif)
        elif level_nbr == 1:
            if not self.checkpoint:
                self.start_x = 8000
                self.start_y = HEIGHT - self.character.rect.height
            self.level = SecondStage(self.character, level_dif)

        elif level_nbr == 2:
            print "initiate level boss"
            if not self.checkpoint:
                self.start_x = 500
                self.start_y = HEIGHT - self.character.rect.height
            self.level = Boss1(self.character, level_dif)

        self.level.start_x = self.start_x
        self.level.start_y = self.start_y

        self.level.game = self

        self.active_sprite_list = pygame.sprite.Group()

        self.character.level = self.level
        self.character.rect.x = self.level.start_x
        self.character.rect.y = self.level.start_y
        self.active_sprite_list.add(self.character)


    def run(self):
        #Loop until the user clicks the close button.
        # Used to manage how fast the screen updates
        clock = pygame.time.Clock()
        #Play audio stuff
        #pygame.mixer.music.load('data/sound/test.wav')
        #pygame.mixer.music.play(-1)
        # -------- Main Program Loop -----------
        while not self.done:

            # Update the self.character.
            self.active_sprite_list.update()
            # Update items in the level
            self.level.update()
            #if the self.character reach the end
            if self.level.end_level:
                self.done = True
                #self.level.world_shift = 0

            #if the self.character is dead
            if self.character.dead == True and self.character.game_over == False:
                self.character.dead = False
                self.character.hit = False
                self.load_level(self.current_level_nbr, self.level_dif)
                taunt = random.choice(self.taunts)
                if len(self.taunts)==1:
                    self.taunts = TAUNTS
                taunt = self.taunts.pop(self.taunts.index(taunt))
                routines.death_menu(clock, self.screen,taunt)

            # If the self.character gets near the right side, shift the world left (-x)
            if self.character.rect.right >= 300:
                diff = self.character.rect.right - 300
                txt1 = routines.draw_text("Select your Badass", 20, 20, 20, "data/coders_crux/coders_crux.ttf", constants.WHITE)
                self.character.rect.right = 300
                self.level.shift_world(-diff)

            # If the self.character gets near the left side, shift the world right (+x)
            if self.character.rect.left <= 300:
                diff = 300 - self.character.rect.left
                self.character.rect.left = 300
                self.level.shift_world(diff)

            #SHIFT THE WORLD
            current_position = self.character.rect.x + self.level.world_shift

            # If the self.character gets to the end of the level, go to the menu title
            if current_position < self.level.level_limit:
                constants.GAME_STATUS = "menu"
                self.done = True
                print constants.GAME_STATUS

            if self.character.game_over:
                routines.game_over_screen(clock, self.screen)
                constants.GAME_STATUS = "menu"
                self.done = True
                print "game over"
                #TODO: show a game over screen
                print constants.GAME_STATUS



            # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
            self.level.draw(self.screen)
            self.active_sprite_list.draw(self.screen)

            # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT


            for event in pygame.event.get(): # User did something

                #Joystick stuff

                if event.type == pygame.JOYBUTTONDOWN:
                    if self.joystick.get_button(1) == 1:
                        self.character.jump()
                    if self.joystick.get_button(9) == 1:
                        routines.pause(clock,self.screen,self.joystick)

                if event.type == pygame.JOYHATMOTION:
                    hat = self.joystick.get_hat(0)
                    if (-1, 0) ==  hat:
                        self.character.stop()
                        self.character.go_left()
                    if (1, 0) == hat:
                        self.character.stop()
                        self.character.go_right()
                    if (0, 0) == hat and self.character.change_x != 0:
                        self.character.stop()



                #Keyboard stuff
                if event.type == pygame.QUIT: # If user clicked close
                    constants.GAME_STATUS = "exit"
                    self.done = True
                    # pygame.quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                        self.character.stop()
                        self.character.go_left()
                    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        self.character.stop()
                        self.character.go_right()
                    if event.key == pygame.K_UP or event.key == pygame.K_w or event.key == pygame.K_SPACE:
                        self.character.jump()
                    if event.key == pygame.K_p:
                        routines.pause(clock,self.screen,self.joystick)

                if event.type == pygame.KEYUP:
                    if (event.key == pygame.K_LEFT or event.key == pygame.K_a) and self.character.change_x < 0:
                        self.character.stop()
                    if (event.key == pygame.K_RIGHT or event.key == pygame.K_d) and self.character.change_x > 0:
                        self.character.stop()

            # Limit to 60 frames per second
            clock.tick(60)

            # Go ahead and update the screen with what we've drawn.
            pygame.display.flip()

    def load_level(self, level_pointer, level_dif):
        self.init_level(level_pointer, self.level_dif)


    def save_data(data_to_save):
        print os.getcwd()
        #initialize file if not existent
        if os.path.isfile("gamedata.txt") == False:
            file = open("gamedata.txt", "w+")
            data_init = "A,0,0,0,0\nB,0,0,0,0\nC,0,0,0,0\n"
            file.write(data_init)
            file.close

        file = open("gamedata.txt", "r")
        lines = file.readlines()
        dest_save = data_to_save[0]

        for i in range(len(lines)):
            data = lines[i].split(",")[0]
            if data == dest_save:
                lines[i] = str(data_to_save[0]) + ',' + str(data_to_save[1]) + ',' + str(data_to_save[2]) + ',' + str(data_to_save[3]) + ',' + str(data_to_save[4]) + '\n'
        file.close()

        file = open("gamedata.txt", "w+")
        for i in range(len(lines)):
            file.write(str(lines[i]))
        file.close()
