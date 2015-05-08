import pygame
import constants
import routines
from Menu import Menu

class PauseMenu(Menu):

    def create_structure(self):
        print "pause_menu"
        Menu.create_structure(self, False)
        screen = self.dest_surface
        txt1 = routines.draw_text("Game paused", constants.SCREEN_WIDTH/2, constants.SCREEN_HEIGHT/2 + 20, 50, "data/coders_crux/coders_crux.ttf", constants.WHITE)
        screen.blit(txt1[0], txt1[1])
        pygame.display.update()


    def run(self,joystick):
        menu_flag = True
        selected = ''
        while menu_flag:
            for event in pygame.event.get():

                #Joystick stuff
                if event.type == pygame.JOYHATMOTION:
                    hat = joystick.get_hat(0)
                    if (0, 1) == hat:
                        self.draw(-1)
                        Menu.menu_res['menu_hover'].play()
                    if (0, -1) == hat:
                        self.draw(1)
                        Menu.menu_res['menu_hover'].play()
                    pygame.display.update()
                if event.type == pygame.JOYBUTTONDOWN:
                    if joystick.get_button(1) == 1:#X button
                        if self.get_position() == 0:
                            selected = 'c'#continue
                        if self.get_position() == 1:
                            selected = 'm'#go back to menu
                        if self.get_position() == 2:
                            selected = 'q'#quit the game

                        # constants.GAME_STATUS = "menuDiff"
                        Menu.menu_res['menu_select'].play()
                        return selected

                    if joystick.get_button(2) == 1:#O button
                        constants.GAME_STATUS = "menu"
                        Menu.menu_res['menu_back'].play()
                        menu_flag = False


                #Keyboard stuff
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.draw(-1)
                        Menu.menu_res['menu_hover'].play()
                    if event.key == pygame.K_DOWN:
                        self.draw(1)
                        Menu.menu_res['menu_hover'].play()
                    if event.key == pygame.K_RETURN:
                        if self.get_position() == 0:
                            selected = 'c'#continue
                        if self.get_position() == 1:
                            selected = 'm'#go back to menu
                        if self.get_position() == 2:
                            selected = 'q'#quit the game

                        # constants.GAME_STATUS = "menuDiff"
                        Menu.menu_res['menu_select'].play()
                        return selected

                    if event.key == pygame.K_BACKSPACE:
                        constants.GAME_STATUS = "menu"
                        Menu.menu_res['menu_back'].play()
                        menu_flag = False
                    if event.key == pygame.K_ESCAPE:
                        constants.GAME_STATUS="exit"
                        menu_flag = False
                    pygame.display.update()
                elif event.type == pygame.QUIT:
                    constants.GAME_STATUS="exit"
                    menu_flag = False
            pygame.time.wait(8)
