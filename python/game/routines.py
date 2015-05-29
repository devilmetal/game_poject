import os
import pygame
import constants
import random
from PauseMenu import PauseMenu
def load_png(name):
        """ Load image and return image object"""
        fullname = os.path.join('data', name)
        try:
                image = pygame.image.load(fullname)
                if image.get_alpha is None:
                        image = image.convert()
                else:
                        image = image.convert_alpha()
        except pygame.error, message:
                print 'Cannot load image:', fullname
                raise SystemExit, message
        return image, image.get_rect()


def draw_rectangle(width, height, bg_color):
    bg = pygame.Surface((width, height))
    bg.fill(bg_color)
    bg = bg.convert()

    return bg

def draw_text(text, posx, posy, fsize, font_path, color):
    txt = []
    font = pygame.font.Font(font_path, fsize)
    t = font.render(text, 1, color)
    tpos = t.get_rect()
    tpos.centerx = posx
    tpos.centery = posy

    txt.append(t)
    txt.append(tpos)

    return txt


def death_menu(clock, screen,death_taunt):
    """ Screen appearing after death """
    bg = draw_rectangle(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT, constants.BLACK)

    txt1 = draw_text("You died.", constants.SCREEN_WIDTH/2, constants.SCREEN_HEIGHT/2 - 20, 52, "data/coders_crux/coders_crux.ttf", constants.WHITE)
    txt2 = draw_text(death_taunt, constants.SCREEN_WIDTH/2, constants.SCREEN_HEIGHT/2 + 20, 38, "data/coders_crux/coders_crux.ttf", constants.WHITE)

    bg.blit(txt1[0], txt1[1])
    bg.blit(txt2[0], txt2[1])

    screen.blit(bg, (0,0))
    pygame.display.update()

    pygame.time.delay(2000)


def game_over_screen(clock, screen):
    """ Screen appearing after death """

    bg = draw_rectangle(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT, constants.BLACK)

    txt0 = draw_text("GAME OVER", constants.SCREEN_WIDTH/2, constants.SCREEN_HEIGHT/2 - 100, 68, "data/coders_crux/coders_crux.ttf", constants.WHITE)
    txt1 = draw_text("You died like a noob.", constants.SCREEN_WIDTH/2, constants.SCREEN_HEIGHT/2 - 20, 52, "data/coders_crux/coders_crux.ttf", constants.WHITE)
    txt2 = draw_text("Enemies destroyed all your checkpoints!", constants.SCREEN_WIDTH/2, constants.SCREEN_HEIGHT/2 + 20, 38, "data/coders_crux/coders_crux.ttf", constants.WHITE)

    bg.blit(txt0[0], txt0[1])
    bg.blit(txt1[0], txt1[1])
    bg.blit(txt2[0], txt2[1])

    screen.blit(bg, (0,0))
    pygame.display.update()

    pygame.time.delay(4000)


def pause(clock,screen,joystick, game_loop, lvl_name=None):
    """ Pausing the game """
    pause_flag = True
    font = "data/coders_crux/coders_crux.ttf"
    bgw = constants.SCREEN_WIDTH - 300
    bgh = constants.SCREEN_HEIGHT/2
    bg = draw_rectangle(bgw, bgh, (20, 27, 45))

    screen.blit(bg, (150, constants.SCREEN_HEIGHT/3 + 30))
    menu = PauseMenu()
    menu.lvl_name = lvl_name
    menu.init(['Continue','Back to menu', 'Quit'], screen)
    menu.draw()
    pygame.key.set_repeat(199,69)#(delay,interval)
    pygame.display.update()
    selected = menu.run(joystick)

    if selected == 'c':
        pass
    if selected == 'm':
        game_loop = True
        constants.GAME_STATUS = 'menu'
    if selected == 'q':
        constants.GAME_STATUS = 'exit'
        game_loop = True
        # pygame.quit()
        # quit()
    pygame.display.update()

    return game_loop


    # while pause_flag:
    #     for event in pygame.event.get():
    #
    #         if event.type == pygame.JOYBUTTONDOWN:
    #             if joystick.get_button(1) == 1:#X button
    #                 pause_flag = False
    #             if joystick.get_button(2) == 1:#O button
    #                 pygame.quit()
    #                 quit()
    #
    #         if event.type == pygame.QUIT:
    #             pygame.quit()
    #             quit()
    #         if event.type == pygame.KEYDOWN:
    #             if event.key == pygame.K_c:
    #                 pause_flag = False
    #             elif event.key == pygame.K_q:
    #                 pygame.quit()
    #                 quit()
        #clock.tick(60)
