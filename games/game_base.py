# games/game_base.py

class GameBase:
    def start(self):
        """Start the game."""
        raise NotImplementedError("You need to implement the start method.")
    
    def get_name(self):
        """Return the name of the game."""
        raise NotImplementedError("You need to implement the get_name method.")
