from human import Human
from ai import Ai

class Game:
    def __init__(self):
        self.player_one = Human()
        self.player_two = None



    def run_game(self):
        # Intro
        print("Welcome To RPSLS!")
        self.choose_game_type()
        self.player_one.the_gesture()
        self.player_two.the_gesture()
        if self.player_one.chosen_gesture == "rock":
            if self.player_two.chosen_gesture == "rock":
                print("Tie")
            elif self.player_two.chosen_gesture == "paper":
                print("Player Two Wins!")
                self.player_two ++ self.score
            elif self.player_two.chosen_gesture == "scissor":
                print("Player One Wins!")
                self.player_one ++ self.score
            elif self.player_two.chosen_gesture == "lizard":
                print("Player One Wins!")
                self.player_one ++ self.score
            elif self.player_two.chosen_gesture == "spock":
                print("Player Two Wins!")
                self.player_two ++ self.score

            if self.player_one.chosen_gesture == "paper":
                if self.player_two.chosen_gesture == "rock":
                    print("Player One Wins!")
                    self.player_one ++ self.score
                elif self.player_two.chosen_gesture == "paper":
                    print("Tie")
                elif self.player_two.chosen_gesture == "scissor":
                    print("Player Two Wins!")
                    self.player_two ++ self.score
                elif self.player_two.chosen_gesture == "lizard":
                    print("Player Two Wins!")
                    self.player_two ++ self.score
                elif self.player_two.chosen_gesture == "spock":
                    print("Player One Wins!")
                    self.player_one ++ self.score

            if self.player_one.chosen_gesture == "scissor":
                if self.player_two.chosen_gesture == "rock":
                    print("Player Two Wins!")
                    self.player_two ++ self.score
                elif self.player_two.chosen_gesture == "paper":
                    print("Player One Wins!")
                    self.player_one ++ self.score
                elif self.player_two.chosen_gesture == "scissor":
                    print("Tie")
                elif self.player_two.chosen_gesture == "lizard":
                    print("Player One Wins!")
                    self.player_one ++ self.score
                elif self.player_two.chosen_gesture == "spock":
                    print("Player Two Wins!")
                    self.player_two ++ self.score

            if self.player_one.chosen_gesture == "lizard":
                if self.player_two.chosen_gesture == "rock":
                    print("Player Two Wins!")
                    self.player_two ++ self.score
                elif self.player_two.chosen_gesture == "paper":
                    print("Player One Wins!")
                    self.player_one ++ self.score
                elif self.player_two.chosen_gesture == "scissor":
                    print("Player Two Wins!")
                    self.player_two ++ self.score
                elif self.player_two.chosen_gesture == "lizard":
                    print("Tie")
                elif self.player_two.chosen_gesture == "spock":
                    print("Player One Wins!")
                    self.player_one ++ self.score

            if self.player_one.chosen_gesture == "spock":
                if self.player_two.chosen_gesture == "rock":
                    print("Player One Wins!")
                    self.player_one ++ self.score
                elif self.player_two.chosen_gesture == "paper":
                    print("Player Two Wins!")
                    self.player_two ++ self.score
                elif self.player_two.chosen_gesture == "scissor":
                    print("Player One Wins!")
                    self.player_one ++ self.score
                elif self.player_two.chosen_gesture == "lizard":
                    print("Player Two Wins!")
                    self.player_two ++ self.score
                elif self.player_two.chosen_gesture == "spock":
                    print("Tie")


    def choose_game_type(self):
        print("How many players?")
        response = input()
        if response == 2:
            self.player_two = Human()
        else:
            self.player_two = Ai()

