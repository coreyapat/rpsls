from game import Game
class Operation:
    def __init__(self):
        self.game = Game()
        self.game.run_game()
        self.game.choose_game_type()
