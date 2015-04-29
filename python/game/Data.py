import pygame
import constants
import routines
import os


class Data():
    file = 'gamedata.txt'
    slot = 'A' #by default
    unlocked_skills = 0
    unlocked_chars = 0
    unlocked_stages = 0
    remaining_lives = 6

    def __init__(self, file, data_init):
        self.file = file
        if os.path.isfile(self.file) == False:
            file = open(self.file, "w+")
            if data_init == "":
                data_init = "A,0,0,6,0\nB,0,0,6,0\nC,0,0,6,0\n"
            '''
            data_init description:
            [0] : slot name
            [1] : number of skills unlocked 0-2
            [2] : number of characters unlocked 0-2
            [3] : number of lives remaining 0-6
            [4] : number of stages unlocked 0-2
            '''
            file.write(data_init)
            file.close


    # def save_data(self,data_to_save):
    #     print os.getcwd()
    #
    #     file = open(self.file, "r")
    #     lines = file.readlines()
    #     dest_save = data_to_save[0]
    #
    #     for i in range(len(lines)):
    #         data = lines[i].split(",")[0]
    #         if data == dest_save:
    #             lines[i] = str(data_to_save[0]) + ',' + str(data_to_save[1]) + ',' + str(data_to_save[2]) + ',' + str(data_to_save[3]) + ',' + str(data_to_save[4]) + '\n'
    #     file.close()
    #
    #     file = open(self.file, "w+")
    #     for i in range(len(lines)):
    #         file.write(str(lines[i]))
    #     file.close()


    def save_data(self):
        # print os.getcwd()

        file = open(self.file, "r")
        lines = file.readlines()

        for i in range(len(lines)):
            data = lines[i].split(",")[0]
            if data == self.slot:
                lines[i] = self.slot + ',' + str(self.unlocked_skills) + ',' + str(self.unlocked_chars) + ',' + str(self.remaining_lives) + ',' + str(self.unlocked_stages) + '\n'
        file.close()

        file = open(self.file, "w+")
        for i in range(len(lines)):
            file.write(str(lines[i]))
        file.close()


    def load_data(self):
        #slot is choosen by the user in the menu

        file = open(self.file, "r")
        lines = file.readlines()

        for i in range(len(lines)):
            data = lines[i].split("\n")[0]
            data = lines[i].split(",")
            if data[0] == self.slot:
                self.unlocked_skills = int(data[1])
                self.unlocked_chars = int(data[2])
                self.remaining_lives = int(data[3])
                self.unlocked_stages = int(data[4])
        file.close()
