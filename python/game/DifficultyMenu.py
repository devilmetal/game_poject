import pygame
import constants
from Menu import Menu

class DifficultyMenu(Menu):

    def create_structure(self):
        Menu.create_structure(self)

        font_size_title = 50
        font_path_title = 'data/coders_crux/coders_crux.ttf'
        font_title = pygame.font.Font(font_path_title, font_size_title)
        title = "Choose your skill level"
        text = font_title.render(title, 1, constants.RED)
        screen = self.dest_surface
        textRect = text.get_rect()
        textRect.centerx = 420
        textRect.centery = 280
        screen.blit(text,textRect)


    def run(self,joystick):
        menu_flag = True
        while menu_flag:
            for event in pygame.event.get():

                #Joystick stuff
                if event.type == pygame.JOYHATMOTION:
                    hat = joystick.get_hat(0)
                    if (0, 1) == hat:
                        self.draw(-1)
                    if (0, -1) == hat:
                        self.draw(1)
                    pygame.display.update()
                if event.type == pygame.JOYBUTTONDOWN:
                    if joystick.get_button(1) == 1:
                        if self.get_position() == 2:
                            menu_flag = False
                            return "hard"
                        if self.get_position() == 1:#here is the Menu class function
                            menu_flag = False
                            return "medium"
                        if self.get_position() == 0:#here is the Menu class function
                            menu_flag = False
                            return "easy"


                #Keyboard stuff
                if event.type == pygame.KEYDOWN: # or event.type == pygame.JOYHATMOTION or event.type == pygame.JOYBUTTONDOWN:
                    if event.key == pygame.K_UP:# or joystick.get_hat()==(0,1):
                        self.draw(-1) #here is the Menu class function
                    if event.key == pygame.K_DOWN:# or joystick.get_hat()==(0,-1):
                        self.draw(1) #here is the Menu class function
                    if event.key == pygame.K_RETURN:
                        if self.get_position() == 2:
                            menu_flag = False
                            return "hard"
                        if self.get_position() == 1:#here is the Menu class function
                            menu_flag = False
                            return "medium"
                        if self.get_position() == 0:#here is the Menu class function
                            menu_flag = False
                            return "easy"
                    if event.key == pygame.K_ESCAPE:
                        menu_flag = False
                        main_loop = False
                    pygame.display.update()
                elif event.type == pygame.QUIT:
                    constants.GAME_STATUS="exit"
                    menu_flag = False
            pygame.time.wait(8)