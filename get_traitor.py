import numpy as np

class GetTraitor:

    def __init__(self, p, r):
        
        self.previous_day = p
        self.recent_day = r
        self.previous_followers_list = []
        self.recent_followers_list = []


    def loadfile(self):

        with open(self.previous_day + "_followers_johncena.txt") as file:
            item_p = file.read().splitlines()

        with open(self.recent_day + "_followers_johncena.txt") as file:
            item_r = file.read().splitlines()

        traitor_list = np.setdiff1d(item_r, item_p)
        print("those guys is not your followers anymore: ", traitor_list)



