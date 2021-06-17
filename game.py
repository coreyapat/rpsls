from human import Human
from ai import Ai

class Game:
    def __init__(self):
        self.player_one = Human()
        self.player_two = None

    def round_loop(self):
        


    def run_game(self):
        # Intro
        # Choose game type
        # Play rounds
        # Players choose gestures
        # Gestures are compared
        # Points assigned based on the winner
        # Check if there is a game winner - if so, end game, otherwise REPEAT



        print("Welcome To RPSLS!")
        self.choose_game_type()
        self.player_one.the_gesture()
        self.player_two.the_gesture()
        if self.player_one.chosen_gesture == "rock":
            if self.player_two.chosen_gesture == "rock":
                print("Tie")
            elif self.player_two.chosen_gesture == "paper":
                print("Player Two Wins!")
                self.player_two.score+=1
            elif self.player_two.chosen_gesture == "scissor":
                print("Player One Wins!")
                self.player_one.score+=1
            elif self.player_two.chosen_gesture == "lizard":
                print("Player One Wins!")
                self.player_one.score+=1
            elif self.player_two.chosen_gesture == "spock":
                print("Player Two Wins!")
                self.player_two.score+=1

        if self.player_one.chosen_gesture == "paper":
            if self.player_two.chosen_gesture == "rock":
                print("Player One Wins!")
                self.player_one.score+=1
            elif self.player_two.chosen_gesture == "paper":
                print("Tie")
            elif self.player_two.chosen_gesture == "scissor":
                print("Player Two Wins!")
                self.player_two.score+=1
            elif self.player_two.chosen_gesture == "lizard":
                print("Player Two Wins!")
                self.player_two.score+=1
            elif self.player_two.chosen_gesture == "spock":
                print("Player One Wins!")
                self.player_one.score+=1

        if self.player_one.chosen_gesture == "scissor":
            if self.player_two.chosen_gesture == "rock":
                print("Player Two Wins!")
                self.player_two.score+=1
            elif self.player_two.chosen_gesture == "paper":
                print("Player One Wins!")
                self.player_one.score+=1
            elif self.player_two.chosen_gesture == "scissor":
                print("Tie")
            elif self.player_two.chosen_gesture == "lizard":
                print("Player One Wins!")
                self.player_one.score+=1
            elif self.player_two.chosen_gesture == "spock":
                print("Player Two Wins!")
                self.player_two.score+=1

        if self.player_one.chosen_gesture == "lizard":
            if self.player_two.chosen_gesture == "rock":
                print("Player Two Wins!")
                self.player_two.score+=1
            elif self.player_two.chosen_gesture == "paper":
                print("Player One Wins!")
                self.player_one.score+=1
            elif self.player_two.chosen_gesture == "scissor":
                print("Player Two Wins!")
                self.player_two.score+=1
            elif self.player_two.chosen_gesture == "lizard":
                print("Tie")
            elif self.player_two.chosen_gesture == "spock":
                print("Player One Wins!")
                self.player_one.score+=1

        if self.player_one.chosen_gesture == "spock":
            if self.player_two.chosen_gesture == "rock":
                print("Player One Wins!")
                self.player_one.score+=1
            elif self.player_two.chosen_gesture == "paper":
                print("Player Two Wins!")
                self.player_two.score+=1
            elif self.player_two.chosen_gesture == "scissor":
                print("Player One Wins!")
                self.player_one.score+=1
            elif self.player_two.chosen_gesture == "lizard":
                print("Player Two Wins!")
                self.player_two.score+=1
            elif self.player_two.chosen_gesture == "spock":
                print("Tie")


    def choose_game_type(self):
        print("How many players?")
        response = input()
        if response == 2:
            self.player_two = Human()
        else:
            self.player_two = Ai()

