# games/quiz_game.py

from .game_base import GameBase

class QuizGame(GameBase):
    def __init__(self):
        self.questions = [
            {
                "question": "What is the capital of France?",
                "choices": ["a) London", "b) Berlin", "c) Paris", "d) Madrid"],
                "answer": "c"
            },
            {
                "question": "Who wrote 'Hamlet'?",
                "choices": ["a) Charles Dickens", "b) William Shakespeare", "c) Mark Twain", "d) Jane Austen"],
                "answer": "b"
            },
            {
                "question": "What is the smallest prime number?",
                "choices": ["a) 0", "b) 1", "c) 2", "d) 3"],
                "answer": "c"
            }
        ]
        self.score = 0

    def start(self):
        print("Starting Quiz Game")
        for question in self.questions:
            print("\n" + question["question"])
            for choice in question["choices"]:
                print(choice)
            answer = input("Your answer (a/b/c/d): ").strip().lower()
            if answer == question["answer"]:
                print("Correct!")
                self.score += 1
            else:
                print("Wrong. The correct answer is " + question["answer"] + ".")

        print(f"\nYour final score is: {self.score}/{len(self.questions)}")

    def get_name(self):
        return "Quiz Game"
