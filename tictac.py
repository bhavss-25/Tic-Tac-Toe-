import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk, ImageFilter

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.root.geometry("400x450")
        self.root.configure(bg="#282c34")
        
        self.current_player = "X"
        self.board = [""] * 9
        self.buttons = []
        self.result_frame = None  
        self.create_board()
        
    def create_board(self):
        title = tk.Label(self.root, text="Tic Tac Toe", font=("Arial", 24, "bold"), fg="#61afef", bg="#282c34")
        title.pack(pady=10)

        frame = tk.Frame(self.root, bg="#282c34")
        frame.pack()

        for i in range(9):
            btn = tk.Button(
                frame, text="", font=("Arial", 20, "bold"), width=5, height=2,
                command=lambda i=i: self.play_turn(i), bg="#98c379", fg="#282c34"
            )
            btn.grid(row=i//3, column=i%3, padx=5, pady=5)
            self.buttons.append(btn)
        
    def play_turn(self, index):
        if self.board[index] == "" and self.check_winner() is None:
            self.board[index] = self.current_player
            self.buttons[index].config(text=self.current_player)
            winner = self.check_winner()
            if winner:
                self.display_winner(winner)
            elif "" not in self.board:
                self.display_winner("Draw")
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
    
    def check_winner(self):
        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8], # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8], # Columns
            [0, 4, 8], [2, 4, 6]             # Diagonals
        ]
        for combo in winning_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != "":
                return self.board[combo[0]]
        return None
    
    def display_winner(self, winner):
        # Disable all buttons
        for button in self.buttons:
            button.config(state="disabled")
        
        # Blur the background by taking a screenshot and blurring it
        screenshot = Image.new("RGB", (400, 450), "#282c34")
        blurred = screenshot.filter(ImageFilter.GaussianBlur(15))
        self.blurred_img = ImageTk.PhotoImage(blurred)
        self.background_label = tk.Label(self.root, image=self.blurred_img)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
        
        # Winner display frame
        self.result_frame = tk.Frame(self.root, bg="#282c34")
        self.result_frame.place(relx=0.5, rely=0.5, anchor="center")
        
        if winner == "Draw":
            message = "It's a Draw!"
        else:
            message = f"{winner} Wins!"
        
        label = tk.Label(self.result_frame, text=message, font=("Arial", 18, "bold"), fg="#e06c75", bg="#282c34")
        label.pack(pady=10)
        
        # Buttons for restart and exit
        restart_btn = tk.Button(self.result_frame, text="Restart", font=("Arial", 14), bg="#98c379", fg="#282c34", command=self.restart)
        restart_btn.pack(side="left", padx=10)
        
        exit_btn = tk.Button(self.result_frame, text="Exit", font=("Arial", 14), bg="#e06c75", fg="#282c34", command=self.root.quit)
        exit_btn.pack(side="right", padx=10)
    
    def restart(self):
        self.board = [""] * 9
        self.current_player = "X"
        for button in self.buttons:
            button.config(text="", state="normal")
        
        # Remove the blurred background and reset layout
        self.background_label.place_forget()
        
        # Destroy the result frame with restart/exit buttons
        if self.result_frame:
            self.result_frame.destroy()
            self.result_frame = None

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()


