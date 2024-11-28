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

        # Create the game board
        self.create_board()

        # Create GUI elements
        self.info_label = tk.Label(root, text="Welcome to Snake and Ladder! Player 1's turn.", font=("Arial", 14))
        self.info_label.pack()

        self.roll_button = tk.Button(root, text="Roll Dice", command=self.roll_dice, font=("Arial", 14))
        self.roll_button.pack()

        self.reset_button = tk.Button(root, text="Reset Game", command=self.reset_game, font=("Arial", 14))
        self.reset_button.pack()

    def create_board(self):
        self.board_canvas = tk.Canvas(self.root, width=400, height=400)
        self.board_canvas.pack()

        # Draw the squares
        for i in range(10):
            for j in range(10):
                square_number = 10 * (9 - i) + (j + 1)
                x1 = j * 40
                y1 = i * 40
                x2 = x1 + 40
                y2 = y1 + 40
                self.board_canvas.create_rectangle(x1, y1, x2, y2, outline="black", fill="white")
                self.board_canvas.create_text(x1 + 20, y1 + 20, text=str(square_number), font=("Arial", 12))

        # Draw snakes and ladders
        for start, end in snakes.items():
            self.draw_snake(start, end)
        for start, end in ladders.items():
            self.draw_ladder(start, end)

    def draw_snake(self, start, end):
        start_x, start_y = self.get_square_position(start)
        end_x, end_y = self.get_square_position(end)
        self.board_canvas.create_line(start_x + 20, start_y + 20, end_x + 20, end_y + 20, fill="red", width=2)

    def draw_ladder(self, start, end):
        start_x, start_y = self.get_square_position(start)
        end_x, end_y = self.get_square_position(end)
        self.board_canvas.create_line(start_x + 20, start_y + 20, end_x + 20, end_y + 20, fill="green", width=2)

    def get_square_position(self, square):
        row = 9 - (square - 1) // 10
        col = (square - 1) % 10
        x = col * 40
        y = row * 40
        return x, y

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
        self.update_player_positions()

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

    def update_player_positions(self):
        self.board_canvas.delete("players")  # Clear previous player markers
        player1_x, player1_y = self.get_square_position(self.player1_pos)
        player2_x, player2_y = self.get_square_position(self.player2_pos)

        self.board_canvas.create_oval(player1_x + 10, player1_y + 10, player1_x + 30, player1_y + 30, fill="blue", tags="players")
        self.board_canvas.create_oval(player2_x + 10, player2_y + 10, player2_x + 10 + 30, player2_y + 10 + 30, fill="orange", tags="players")

    def reset_game(self):
        self.player1_pos = 0
        self.player2_pos = 0
        self.current_player = "Player 1"
        self.info_label.config(text="Welcome to Snake and Ladder! Player 1's turn.")
        self.roll_button.config(state=tk.NORMAL)
        self.update_player_positions()

if __name__ == "__main__":
    root = tk.Tk()
    game = Game(root)
    root.mainloop()
