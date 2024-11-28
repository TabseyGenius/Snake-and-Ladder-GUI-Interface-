import tkinter as tk
import random

# Snakes and Ladders representation
snakes = {16: 6, 48: 26, 49: 11, 56: 53, 62: 19, 64: 60, 87: 24, 93: 73, 95: 75, 98: 78}
ladders = {1: 38, 4: 14, 9: 31, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 80: 100}

class Game:
    def __init__(self, root):
        self.root = root
        self.root.title("Snake and Ladder Game")
        self.player1_pos = 0
        self.player2_pos = 0
        self.current_player = "Player 1"

        # Create GUI elements
        self.info_label = tk.Label(root, text="Welcome to Snake and Ladder! Player 1's turn.", font=("Arial", 14))
        self.info_label.pack()

        self.roll_button = tk.Button(root, text="Roll Dice", command=self.roll_dice, font=("Arial", 14))
        self.roll_button.pack()

        self.reset_button = tk.Button(root, text="Reset Game", command=self.reset_game, font=("Arial", 14))
        self.reset_button.pack()

    def roll_dice(self):
        dice_value = random.randint(1, 6)
        self.info_label.config(text=f"{self.current_player} rolled a {dice_value}")
        
        if self.current_player == "Player 1":
            self.player1_pos += dice_value
            if self.player1_pos > 100:
                self.player1_pos = 100 - (self.player1_pos - 100)  # Bounce back
            self.player1_pos = self.check_snake_ladder(self.player1_pos)
            if self.player1_pos >= 100:
                self.info_label.config(text="Player 1 wins!")
                self.roll_button.config(state=tk.DISABLED)
        else:
            self.player2_pos += dice_value
            if self.player2_pos > 100:
                self.player2_pos = 100 - (self.player2_pos - 100)  # Bounce back
            self.player2_pos = self.check_snake_ladder(self.player2_pos)
            if self.player2_pos >= 100:
                self.info_label.config(text="Player 2 wins!")
                self.roll_button.config(state=tk.DISABLED)

        self.switch_player()

    def check_snake_ladder(self, position):
        if position in snakes:
            position = snakes[position]
            self.info_label.config(text=f"Oh no! {self.current_player} landed on a snake!")
        elif position in ladders:
            position = ladders[position]
            self.info_label.config(text=f"Yay! {self.current_player} climbed a ladder!")
        return position

    def switch_player(self):
        self.current_player = "Player 2" if self.current_player == "Player 1" else "Player 1"
        self.info_label.config(text=f"It's {self.current_player}'s turn.")

    def reset_game(self):
        self.player1_pos = 0
        self.player2_pos = 0
        self.current_player = "Player 1"
        self.info_label.config(text="Welcome to Snake and Ladder! Player 1's turn.")
        self.roll_button.config(state=tk.NORMAL)

if __name__ == "__main__":
    root = tk.Tk()
    game = Game(root)
    root.mainloop()
