import pickle
import os

class Data():
    file = 'gamedata.txt'
    save={}
    selected_slot=None
    selected_diff=None
    selected_char=None

    def __init__(self, file):
        self.file = file
        if os.path.isfile(self.file) == False:
            for slot in ['A','B','C']:
                data={}
                for diff in ['easy','medium','hard']:
                    data[diff] = {}
                    data[diff]['unlocked'] = False
                    for c in ['hulk', 'bob', 'little_fat']:
                        data[diff][c]={}
                        data[diff][c]['unlocked'] = False
                        data[diff][c]['levels'] = []
                    #Hulk is available by default
                    data[diff]['hulk']['unlocked'] = True
                    #Hulk has level 0 unlocked
                    data[diff]['hulk']['levels'].append(0)
                self.save[slot] = data
                #'easy' is always unlocked
                self.save[slot]['used'] = False
                data['easy']['unlocked'] = True

            self.save_data()
        else:
            self.load_data()

    def save_data(self):
        pickle.dump(self.save,open(self.file,'wb'))

    def load_data(self):
        self.save = pickle.load(open(self.file,'rb'))

    def stats(self,slot):
        total = 21.0
        unlocked = 0.0
        for diff in ['easy','medium','hard']:
            if self.save[slot][diff]['unlocked']:
                for c in ['hulk', 'bob', 'little_fat']:
                    if self.save[slot][diff][c]['unlocked']:
                        unlocked += len(self.save[slot][diff][c]['levels'])
        percentage = str(int(unlocked/total*100))
        return percentage
'''
STANDARD ACCESS TO DATA SLOT
    FOR SLOT A

    save['A']['easy']['hulk']['unlocked'] => is hulk on easy unlocked ?
    save['A']['easy']['hulk']['levels'] => List of unlocked levels of hulk in easy difficulty
    save['A']['easy']['unlocked'] => Is the difficulty 'easy' unlocked

    ==================================
    GENERAL STRUCTURE OF THE SAVE TREE
    ==================================

    save['A']
    save['B']
    save['C']
        ['used'] #save slot used or free
            'True'|'False'
        ['easy']
            ['unlocked'] # difficulty unlocked
                'True'|'False'
            ['hulk']
                ['unlocked'] # character unlocked or not
                    'True'|'False'
                ['levels']
                    [0,1,2,...]
            ['bob']
            ['little_fat']
        ['medium']
        ['hard']
'''
