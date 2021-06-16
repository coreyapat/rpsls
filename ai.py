from player import Player
import random

class Ai(Player):

    def __init__(self):
        self.score = 0
        self.name = ""
        self.chosen_gesture = ""

    def the_gesture(self):
        number = random.randint(0, 5)
        self.chosen_gesture = self.gestures[number]



