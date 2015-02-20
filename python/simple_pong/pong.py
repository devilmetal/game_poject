#!/usr/bin/python
#
# Tom's Pong
# A simple pong game with realistic physics and AI
# http://www.tomchance.uklinux.net/projects/pong.shtml
#
# Released under the GNU General Public License

VERSION = "0.4"
SPEED = 13
WINDOWS_SIZE = (640, 480)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

try:
        import sys
        import random
        import math
        import os
        import getopt
        import pygame
        from socket import *
        from pygame.locals import *
except ImportError, err:
        print "couldn't load module. %s" % (err)
        sys.exit(2)

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

class Ball(pygame.sprite.Sprite):
        """A ball that will move across the screen
        Returns: ball object
        Functions: update, calcnewpos
        Attributes: area, vector"""

        def __init__(self, (xy), vector):
                pygame.sprite.Sprite.__init__(self)
                self.image, self.rect = load_png('ball.png')
                screen = pygame.display.get_surface()
                self.area = screen.get_rect()
                self.vector = vector
                self.hit = 0

        def update(self):
                off_court = False
                newpos = self.calcnewpos(self.rect,self.vector)
                self.rect = newpos
                (angle,z) = self.vector
                if not self.area.contains(newpos):
                    tl = not self.area.collidepoint(newpos.topleft)
                    tr = not self.area.collidepoint(newpos.topright)
                    bl = not self.area.collidepoint(newpos.bottomleft)
                    br = not self.area.collidepoint(newpos.bottomright)
                    if tr and tl or (br and bl):
                        angle = -angle
                    if tl and bl:
                        off_court = True
                        global score
                        score.right += 1
                    if tr and br:
                        off_court = True
                        global score
                        score.left += 1
                else:
        			# Deflate the rectangles so you can't catch a ball behind the bat
        			player1.rect.inflate(-3, -3)
        			player2.rect.inflate(-3, -3)

        			# Do ball and bat collide?
        			# Note I put in an odd rule that sets self.hit to 1 when they collide, and unsets it in the next
        			# iteration. this is to stop odd ball behaviour where it finds a collision *inside* the
        			# bat, the ball reverses, and is still inside the bat, so bounces around inside.
        			# This way, the ball can always escape and bounce away cleanly
        			if self.rect.colliderect(player1.rect) == 1 and not self.hit:
        				angle = math.pi - angle
        				self.hit = not self.hit
        			elif self.rect.colliderect(player2.rect) == 1 and not self.hit:
        				angle = math.pi - angle
        				self.hit = not self.hit
        			elif self.hit:
        				self.hit = not self.hit
                if off_court:
                    self.offcourt()
                else:
                    self.vector = (angle,z)

        def calcnewpos(self,rect,vector):
                (angle,z) = vector
                (dx,dy) = (z*math.cos(angle),z*math.sin(angle))
                return rect.move(dx,dy)

        def offcourt(self):
            self.rect.center = (WINDOWS_SIZE[0]/2,WINDOWS_SIZE[1]/2)
            self.vector = (0,0)
            global score
            score.out = True


        def reset(self):
            score.out = False
            self.rect.center = (WINDOWS_SIZE[0]/2,WINDOWS_SIZE[1]/2)
            rand = ((0.1 * (random.randint(0,8))))
            direction = 1-random.choice([0,2])
            self.vector = (direction*rand,SPEED)

class Bat(pygame.sprite.Sprite):
        """Movable tennis 'bat' with which one hits the ball
        Returns: bat object
        Functions: reinit, update, moveup, movedown
        Attributes: which, speed"""

        def __init__(self, side):
                pygame.sprite.Sprite.__init__(self)
                self.image, self.rect = load_png('bat.png')
                screen = pygame.display.get_surface()
                self.area = screen.get_rect()
                self.side = side
                self.speed = 10
                self.state = "still"
                self.reinit()

        def reinit(self):
                self.state = "still"
                self.movepos = [0,0]
                if self.side == "left":
                        self.rect.midleft = self.area.midleft
                elif self.side == "right":
                        self.rect.midright = self.area.midright

        def update(self):
                newpos = self.rect.move(self.movepos)
                if self.area.contains(newpos):
                        self.rect = newpos
                pygame.event.pump()

        def moveup(self):
            self.movepos[1] = self.movepos[1] - (self.speed)
            self.state = "moveup"

        def movedown(self):
            self.movepos[1] = self.movepos[1] + (self.speed)
            self.state = "movedown"


class Score(pygame.sprite.Sprite):
        """Points counter"""
        def __init__(self):
                pygame.sprite.Sprite.__init__(self)
                self.left = 0
                self.right = 0
                self.out = False
                self.font = pygame.font.Font(None, 48)
                self.text = self.font.render(str(self.left)+' | '+str(self.right), 1, WHITE)
                screen = pygame.display.get_surface()
                self.textRect = self.text.get_rect()
                self.textRect.centerx = screen.get_rect().centerx
                self.textRect.centery = 50


        def update(self):
                if self.out:
                    message = str(self.left)+' | '+str(self.right)
                    #TODO : Display some hints
                else:
                    message = str(self.left)+' | '+str(self.right)
                screen = pygame.display.get_surface()
                self.textRect = self.text.get_rect()
                self.textRect.centerx = screen.get_rect().centerx
                self.textRect.centery = 50
                self.text = self.font.render(message, 1, WHITE)


def main():
    # Initialise screen
    pygame.init()
    screen = pygame.display.set_mode(WINDOWS_SIZE)
    pygame.display.set_caption('Basic Pong')

    # Fill background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill(BLACK)

    # Initialise players
    global player1
    global player2
    player1 = Bat("left")
    player2 = Bat("right")


	# Initialise ball
    speed = SPEED
    rand = ((0.1 * (random.randint(5,8))))
    ball = Ball((0,0),(0.47,speed))

    # Init score display
    global score
    score = Score()

	# Initialise sprites
    playersprites = pygame.sprite.RenderPlain((player1, player2))
    ballsprite = pygame.sprite.RenderPlain(ball)
    scoresprite = pygame.sprite.RenderPlain(score)

    # Blit everything to the screen
    screen.blit(background, (0, 0))
    pygame.display.flip()

    # Initialise clock
    clock = pygame.time.Clock()

    # Event loop
    while 1:
        # Make sure game doesn't run at more than 60 frames per second
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == QUIT:
                return
            elif event.type == KEYDOWN:
                if event.key == K_a:
                    player1.moveup()
                if event.key == K_y:
                    player1.movedown()
                if event.key == K_UP:
                    player2.moveup()
                if event.key == K_DOWN:
                    player2.movedown()
                if event.key == K_SPACE:
                    ball.reset()
            elif event.type == KEYUP:
                if event.key == K_a or event.key == K_y:
                    player1.movepos = [0,0]
                    player1.state = "still"
                if event.key == K_UP or event.key == K_DOWN:
                    player2.movepos = [0,0]
                    player2.state = "still"
        screen.fill(BLACK)
        screen.blit(background, ball.rect, ball.rect)
        screen.blit(background, player1.rect, player1.rect)
        screen.blit(background, player2.rect, player2.rect)
        screen.blit(score.text, score.textRect)
        ballsprite.update()
        playersprites.update()
        scoresprite.update()
        ballsprite.draw(screen)
        playersprites.draw(screen)
        pygame.display.flip()


if __name__ == '__main__': main()
