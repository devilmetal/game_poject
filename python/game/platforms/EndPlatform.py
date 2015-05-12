import constants
import pygame
from Platform import Platform
from characters.Bob import Bob
from characters.Hulk import Hulk
from characters.LittleFat import LittleFat

class EndPlatform(Platform):
    """ This is a fancier platform that can actually move. """

    player = None
    change_difficulty = False
    level = None
    character_pointer = None
    level_pointer = None

    def update(self):
        """ Move the platform.
            If the player is in the way, it will shove the player
            out of the way. This does NOT handle what happens if a
            platform shoves a player into another object. Make sure
            moving platforms have clearance to push the player around
            or add code to handle what happens if they don't. """


        #check if the player is on top of a lateral moving platform and make it move with it.
        self.player.rect.y += 2
        hit = pygame.sprite.collide_rect(self.player, self) and not self.player.hit
        self.player.rect.y -= 2

        if hit:
            self.level.game.current_level_nbr = self.level_pointer
            if self.character_pointer == 'hulk':
                player = Hulk()
                self.level.game.nmp_data.selected_char = 'hulk'
            elif self.character_pointer == 'bob':
                player = Bob()
                self.level.game.nmp_data.selected_char = 'bob'
            elif self.character_pointer == 'little_fat':
                player = LittleFat()
                self.level.game.nmp_data.selected_char = 'little_fat'
            player.lives = self.level.game.character.lives
            self.level.game.character = player
            self.level.game.checkpoint=False
            temp_slot = self.level.game.nmp_data.selected_slot
            temp_diff = self.level.game.nmp_data.selected_diff
            temp_char = self.level.game.nmp_data.selected_char

            #Character unlocking
            self.level.game.nmp_data.save[temp_slot][temp_diff][self.character_pointer]['unlocked'] = True
            #Level unlocking
            temp_levels = self.level.game.nmp_data.save[temp_slot][temp_diff][self.character_pointer]['levels']
            if (not self.level_pointer in temp_levels) and not self.change_difficulty:
                self.level.game.nmp_data.save[temp_slot][temp_diff][self.character_pointer]['levels'].append(self.level_pointer)
            #Difficulty change
            if self.change_difficulty:
                if temp_diff == 'easy':
                    self.level.game.nmp_data.save[temp_slot]['medium']['unlocked']=True
                    self.level.game.level_dif = 'medium'
                if temp_diff == 'medium':
                    self.level.game.nmp_data.save[temp_slot]['hard']['unlocked']=True
                    self.level.game.level_dif = 'hard'
            self.level.game.nmp_data.save_data()
            self.level.game.load_level(self.level_pointer, self.level.game.level_dif)
