from player import Player
class Human(Player):
    def __init__(self):
        self.name = input()



    def  the_gesture(self):
        print ("Hey, make sure you pick 0 for rock, ")
        choose_gesture = input()
        if choose_gesture == "0":
            self.chosen_gesture = self.gestures[0]
        elif choose_gesture == "1":
            self.chosen_gesture = self.gestures[1]

