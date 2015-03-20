import pygame
import constants
import routines

class CharacterMenu:
    selected = 0
    font_size = 32
    font_path = 'data/coders_crux/coders_crux.ttf'
    font = pygame.font.Font
    screen = None
    characters = None
    def __init__(self,screen):
        #Init the menu
        #Draw with position = 1
        self.screen=screen
        bob = routines.load_png('hero/idle_l.png')
        hulk = routines.load_png('hero_1/idle_l.png')
        hulk1 = routines.load_png('hero_1/idle_l.png')
        bob2 = routines.load_png('hero/idle_l.png')


        #self.characters = [bob,hulk]
        self.characters = [bob,hulk,hulk1,bob2]
        self.draw(0)

    def fib(self,n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return self.fib(n-1) + self.fib(n-2)

    #Used inside the run() function with events.
    def draw_by_hop(self,menu_hop):
        # menu_hop = +1/-1
        #Compute new_position according to menu_hop and self.char_list
        modulo = len(self.characters)
        new_position = (self.selected+menu_hop) % modulo
        self.selected = new_position
        #Draw the menu at new position
        self.draw(new_position)


    def draw(self,position):
        #Set the new selected character according to position
        self.selected = position
        #Draw the next position of menu
        #Draw background
        bg = pygame.Surface(self.screen.get_size())
        bg = bg.convert()
        bg.fill(constants.BLACK)
        self.screen.blit(bg, (0,0))
        #Draw funky text
        font1 = pygame.font.Font(self.font_path, 52)
        font2 = pygame.font.Font(self.font_path, 38)
        text1 = font1.render("Select your Badass", 1, constants.WHITE)
        text2 = font2.render('and go kick some asses !', 1, constants.WHITE)
        text1pos = text1.get_rect()
        text2pos = text2.get_rect()
        text1pos.centerx = constants.SCREEN_WIDTH/2
        text1pos.centery = constants.SCREEN_HEIGHT/5 - 20
        text2pos.centerx = constants.SCREEN_WIDTH/2
        text2pos.centery = constants.SCREEN_HEIGHT/5 + 20
        self.screen.blit(text1, text1pos)
        self.screen.blit(text2, text2pos)
        #Create layout of character display according to lenght of self.char_list
        #standard width of character frame
        image_width=40
        x_deviation = int(constants.SCREEN_WIDTH/(len(self.characters)+1))
        y_position = constants.SCREEN_HEIGHT/2
        scale_tail = self.fib(len((self.characters)))
        #Draw all figures
        for character in self.characters:
            #Compute position
            position = self.characters.index(character)
            x_position = x_deviation * (position+1) - image_width/2
            character[1].x = x_position
            character[1].y = y_position
            #Rescale image
            character_scale = pygame.transform.scale(character[0], (int(float(character[1].width)*float(2.0/scale_tail)), int(float(character[1].height)*float(2.0/scale_tail))))
            #Draw background rect of selected figure according to self.selected
            if position == self.selected:
                back = pygame.Surface([int(float(character[1].width)*float(2.0/scale_tail))+40, int(float(character[1].height)*float(2.0/scale_tail))+40])
                back.fill((153,102,255))
                back_rect = character[1].copy()
                back_rect.x-=20
                back_rect.y-=20
                self.screen.blit(back, back_rect)
            #Blit
            self.screen.blit(character_scale, character[1])
            #Draw figure
        #Update the stuff
        pygame.display.update()

    def run(self,joystick):
        #Run the menu selection
        done = False
        while not done:
            #Catch events
            #If ok press => return character selected (aka this.selected)
            for event in pygame.event.get():

                #Joystick stuff
                if event.type == pygame.JOYHATMOTION:
                    hat = joystick.get_hat(0)
                    if (1, 0) == hat:
                        self.draw_by_hop(1)
                    if (-1, 0) == hat:
                        self.draw_by_hop(-1)
                if event.type == pygame.JOYBUTTONDOWN:
                    if joystick.get_button(1) == 1:
                        return self.selected
                #Keyboard stuff
                if event.type == pygame.KEYDOWN: # or event.type == pygame.JOYHATMOTION or event.type == pygame.JOYBUTTONDOWN:
                    if event.key == pygame.K_RIGHT:# or joystick.get_hat()==(0,1):
                        self.draw_by_hop(1) #here is the Menu class function
                    if event.key == pygame.K_LEFT:# or joystick.get_hat()==(0,-1):
                        self.draw_by_hop(-1) #here is the Menu class function
                    if event.key == pygame.K_RETURN:
                        return self.selected
                elif event.type == pygame.QUIT:
                    constants.GAME_STATUS="exit"
                    menu_flag = False
