import os
import pygame
import constants

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

def death_menu(clock):
    """ Screen appearing after death """
    font_path_title = 'data/coders_crux/coders_crux.ttf'

    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    bg = pygame.Surface(screen.get_size())
    bg = bg.convert()
    bg.fill(constants.BLACK)

    font1 = pygame.font.Font(font_path_title, 52)
    font2 = pygame.font.Font(font_path_title, 38)
    text1 = font1.render("You died.", 1, constants.WHITE)
    text2 = font2.render("You're still not skilled enough...", 1, constants.WHITE)
    text1pos = text1.get_rect()
    text2pos = text2.get_rect()
    text1pos.centerx = constants.SCREEN_WIDTH/2
    text1pos.centery = constants.SCREEN_HEIGHT/2 - 20
    text2pos.centerx = constants.SCREEN_WIDTH/2
    text2pos.centery = constants.SCREEN_HEIGHT/2 + 20

    bg.blit(text1, text1pos)
    bg.blit(text2, text2pos)

    screen.blit(bg, (0,0))
    pygame.display.update()

    pygame.time.delay(2000)


def pause(clock,screen,joystick):
    """ Pausing the game """
    pause_flag = True
    font_path_title = 'data/coders_crux/coders_crux.ttf'
    font1 = pygame.font.Font(font_path_title, 52)
    font2 = pygame.font.Font(font_path_title, 42)
    text1 = font1.render("Paused", 1, constants.WHITE)
    text2 = font2.render("Continue (c) or A or Quit (q) ?", 1, constants.WHITE)
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

            if event.type == pygame.JOYBUTTONDOWN:
                if joystick.get_button(1) == 1:
                    pause_flag = False

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    pause_flag = False
                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()
        #clock.tick(60)
