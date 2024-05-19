# Python Game Engine

This is a simple Python-based game engine that allows users to play various mini-games such as Tic Tac Toe, Number Guessing, and a Quiz Game. The project demonstrates the use of object-oriented programming (OOP) concepts in Python.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Games](#games)
  - [Tic Tac Toe](#tic-tac-toe)
  - [Number Guessing](#number-guessing)
  - [Quiz Game](#quiz-game)
- [Contributing](#contributing)
- [License](#license)

## Features

- Modular game engine design using OOP principles
- Easy addition of new games
- Console-based user interface
- Three different games to play:
  - Tic Tac Toe
  - Number Guessing (with limited tries)
  - Quiz Game



##Project Structure


game_engine/
│
├── games/
│   ├── __init__.py
│   ├── tic_tac_toe.py
│   ├── number_guessing.py
│   ├── quiz_game.py
│   └── rock_paper_scissors.py
│
└── main.py



## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/game_engine.git
    ```
2. Navigate to the project directory:
    ```bash
    cd game_engine
    ```

## Usage

To run the game engine, simply execute the `main.py` file:
```bash
python main.py


Follow the on-screen instructions to select and play a game.

Games
Tic Tac Toe
A two-player game where players take turns marking spaces in a 3×3 grid. The player who succeeds in placing three of their marks in a horizontal, vertical, or diagonal row wins the game.

Number Guessing
A game where the player has to guess a randomly generated number between 1 and 5. The player has three tries to guess the correct number.

Quiz Game
A game that presents multiple-choice questions to the player. The player must select the correct answer from the given options. The final score is displayed at the end of the game.

Contributing
Contributions are welcome! If you have any suggestions or improvements, feel free to open an issue or create a pull request. Please ensure your code follows the project's coding standards and includes appropriate tests.

License
This project is licensed under the MIT License. See the LICENSE file for details.
