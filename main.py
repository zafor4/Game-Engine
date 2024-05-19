# main.py

from games.tic_tac_toe import TicTacToe
from games.number_guessing import NumberGuessing
from games.quiz_game import QuizGame
# Import other games here

class GameEngine:
    def __init__(self):
        self.games = {
            1: TicTacToe(),
            2: NumberGuessing(),
            3: QuizGame(),
            # Add other games here with their respective numbers
        }
        self.game_names = {
            1: "Tic Tac Toe",
            2: "Number Guessing",
            3: "Quiz Game",
            # Add other game names here
        }

    def list_games(self):
        print("Available games:")
        for number, name in self.game_names.items():
            print(f"{number}. {name}")

    def run(self):
        self.list_games()
        choice = input("Enter the number of the game you would like to play: ").strip()
        if choice.isdigit() and int(choice) in self.games:
            game = self.games[int(choice)]
            game.start()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    engine = GameEngine()
    engine.run()
