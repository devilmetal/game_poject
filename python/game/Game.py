import pygame
import constants
import routines
from levels.FirstStage import FirstStage
from levels.SecondStage import SecondStage

HEIGHT = constants.SCREEN_HEIGHT-20

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
    def init_level(self,level_nbr, level_dif):
        if level_nbr == 0:
            if not self.checkpoint:
                self.start_x = 12300
                self.start_y = HEIGHT - 20
            self.level = FirstStage(self.character, level_dif)
        elif level_nbr == 1:
            if not self.checkpoint:
                self.start_x = 350
                self.start_y = HEIGHT - 20
            self.level = SecondStage(self.character, level_dif)

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
            if self.character.dead == True:
                self.character.dead = False
                self.character.hit = False
                self.load_level(self.current_level_nbr, self.level_dif)
                routines.death_menu(clock)

            # If the self.character gets near the right side, shift the world left (-x)
            if self.character.rect.right >= 300:
                diff = self.character.rect.right - 300
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
                    pygame.quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.character.stop()
                        self.character.go_left()
                    if event.key == pygame.K_RIGHT:
                        self.character.stop()
                        self.character.go_right()
                    if event.key == pygame.K_UP:
                        self.character.jump()
                    if event.key == pygame.K_p:
                        routines.pause(clock,self.screen,self.joystick)

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT and self.character.change_x < 0:
                        self.character.stop()
                    if event.key == pygame.K_RIGHT and self.character.change_x > 0:
                        self.character.stop()

            # Limit to 60 frames per second
            clock.tick(60)

            # Go ahead and update the screen with what we've drawn.
            pygame.display.flip()

    def load_level(self,level_pointer, level_dif):
        self.init_level(level_pointer, self.level_dif)
