import pygame
import constants

class Menu:
    liste = []
    position = []
    font_size = 32
    font_path = 'data/coders_crux/coders_crux.ttf'
    font = pygame.font.Font
    dest_surface = pygame.Surface
    index_pos = 0
    back_color = (20, 27, 45)
    font_color =  (255,255,255)
    select_color = (126, 174, 193)
    pos_selection = 0
    pos_rect = (0,0)
    menu_width = 0
    menu_height = 0
    menu_res = {}
    menu_res['menu_hover'] = pygame.mixer.Sound('data/sound/menu-hover.wav')
    menu_res['menu_back'] = pygame.mixer.Sound('data/sound/menu-back.wav')
    menu_res['menu_select'] = pygame.mixer.Sound('data/sound/menu-select.wav')

    class Pole:
        tekst = ''
        pole = pygame.Surface
        pole_rect = pygame.Rect
        select_rect = pygame.Rect

    def move_menu(self, top, left):
        self.pos_rect = (top,left)

    def set_colors(self, text, selection, background):
        self.back_color = background
        self.font_color =  text
        self.select_color = selection

    def set_fontsize(self,font_size):
        self.font_size = font_size

    def set_font(self, path):
        self.font_path = path

    def get_position(self):
        return self.pos_selection

    def init(self, liste, dest_surface):
        self.liste = liste
        self.dest_surface = dest_surface
        self.index_pos = len(self.liste)
        self.create_structure()

    def draw(self,actual_pos=0):
        if actual_pos:
            self.pos_selection += actual_pos
            if self.pos_selection == -1:
                self.pos_selection = self.index_pos - 1
            self.pos_selection %= self.index_pos
        menu = pygame.Surface((self.menu_width, self.menu_height))
        #no back color at the moment. Transparent stuff !
        menu.fill(self.back_color)
        select_rect = self.position[self.pos_selection].select_rect
        pygame.draw.rect(menu,self.select_color,select_rect)

        for i in xrange(self.index_pos):
            menu.blit(self.position[i].pole,self.position[i].pole_rect)
        self.dest_surface.blit(menu,self.pos_rect)
        return self.pos_selection

    def create_structure(self, default=True):
        if default:
            #make title "No More Pixies"
            font_size_title = 82
            font_path_title = 'data/coders_crux/coders_crux.ttf'
            font_title = pygame.font.Font(font_path_title, font_size_title)
            title = "No More Pixies"
            text = font_title.render(title, 1, constants.WHITE)
            # screen = self.dest_surface
            textRect = text.get_rect()
            textRect.centerx = 400
            textRect.centery = 150
            self.dest_surface.blit(text,textRect)
        actual_posiecie = 0
        self.menu_height = 0
        self.font = pygame.font.Font(self.font_path, self.font_size)
        for i in xrange(self.index_pos):
            self.position.append(self.Pole())
            self.position[i].tekst = self.liste[i]
            self.position[i].pole = self.font.render(self.position[i].tekst, 1, self.font_color)

            self.position[i].pole_rect = self.position[i].pole.get_rect()
            actual_posiecie = int(self.font_size * 0.2)

            height = self.position[i].pole_rect.height
            self.position[i].pole_rect.left = actual_posiecie
            self.position[i].pole_rect.top = actual_posiecie+(actual_posiecie*2+height)*i

            width = self.position[i].pole_rect.width+actual_posiecie*2
            height = self.position[i].pole_rect.height+actual_posiecie*2
            left = self.position[i].pole_rect.left-actual_posiecie
            top = self.position[i].pole_rect.top-actual_posiecie

            self.position[i].select_rect = (left,top ,width, height)
            if width > self.menu_width:
                    self.menu_width = width
            self.menu_height += height
        x = self.dest_surface.get_rect().centerx - self.menu_width / 2
        y = self.dest_surface.get_rect().centery + 100 - self.menu_height / 2
        mx, my = self.pos_rect
        self.pos_rect = (x+mx, y+my)

    def run(self,joystick):
        menu_flag = True
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
                    if joystick.get_button(1) == 1:
                        if self.get_position() == 1:#here is the Menu class function
                            constants.GAME_STATUS="exit"
                            menu_flag = False
                        if self.get_position() == 0:#here is the Menu class function
                            constants.GAME_STATUS="menuSave"
                            Menu.menu_res['menu_select'].play()
                            menu_flag = False


                #Keyboard stuff
                if event.type == pygame.KEYDOWN: # or event.type == pygame.JOYHATMOTION or event.type == pygame.JOYBUTTONDOWN:
                    if event.key == pygame.K_UP:# or joystick.get_hat()==(0,1):
                        self.draw(-1) #here is the Menu class function
                        Menu.menu_res['menu_hover'].play()
                    if event.key == pygame.K_DOWN:# or joystick.get_hat()==(0,-1):
                        self.draw(1) #here is the Menu class function
                        Menu.menu_res['menu_hover'].play()
                    if event.key == pygame.K_RETURN:
                        if self.get_position() == 1:#here is the Menu class function
                            constants.GAME_STATUS="exit"
                            menu_flag = False
                        if self.get_position() == 0:#here is the Menu class function
                            constants.GAME_STATUS="menuSave"
                            Menu.menu_res['menu_select'].play()
                            menu_flag = False
                    if event.key == pygame.K_ESCAPE:
                        constants.GAME_STATUS="exit"
                        menu_flag = False
                    pygame.display.update()
                elif event.type == pygame.QUIT:
                    constants.GAME_STATUS="exit"
                    menu_flag = False
            pygame.time.wait(8)
