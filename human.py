from player import Player
class Human(Player):
    def __init__(self):
        self.name = input()



    def  the_gesture(self):
        print ("Hey, make sure you pick 0 for rock,1 for paper, 2 for scissor, 3 for lizard, 4 for spock ")
        choose_gesture = input()
        if choose_gesture == "0":
            self.chosen_gesture = self.gestures[0]
        elif choose_gesture == "1":
            self.chosen_gesture = self.gestures[1]
        elif choose_gesture == "2":
            self.chosen_gesture = self.gestures[2]
        elif choose_gesture == "3":
            self.chosen_gesture = self.gestures[3]
        elif choose_gesture == "4":
            self.chosen_gesture = self.gestures[4]


