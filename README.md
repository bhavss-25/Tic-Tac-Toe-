# Tic Tac Toe Game

## Description
This project is a modern implementation of the classic Tic Tac Toe game using Python and the Tkinter library for the graphical user interface (GUI). The game is designed to provide a fun and engaging user experience with a clean and dark-themed aesthetic. It includes features such as displaying the winner, handling draws, and offering options to restart or exit the game. The game also uses image manipulation to blur the background when displaying results.

## Features
- **Dark Themed Interface**: The game has a visually appealing dark theme.
- **Two-Player Mode**: Players take turns as 'X' and 'O' on a 3x3 grid.
- **Winner Detection**: Automatically detects and announces the winner or a draw.
- **Restart and Exit Options**: Provides buttons to restart the game or exit the application after a match ends.
- **Background Effects**: Blurs the game board when announcing the results.

## How to Play
1. Launch the game by running the script.
2. The first player is 'X', and the second player is 'O'. Players take turns selecting a square on the grid.
3. The game ends when:
   - A player completes a row, column, or diagonal with their symbol (e.g., three 'X's).
   - All squares are filled without a winner, resulting in a draw.
4. Once the game ends, the result is displayed, and you can either restart or exit.

## Requirements
- Python 3.x
- `tkinter` (usually included with Python installations)
- `Pillow` library for image manipulation

## Installation
1. Clone this repository or download the source code.
2. Ensure you have the required libraries installed:
   ```bash
   pip install pillow
   ```

## Running the Game
Run the following command in your terminal or Python IDE:
```bash
python tictac.py
```

## Code Structure
### Main Components
- **`create_board`**: Initializes the game board with buttons for each cell.
- **`play_turn`**: Handles the logic for a player's turn, updating the board and checking for a winner.
- **`check_winner`**: Checks if there's a winner or a draw.
- **`display_winner`**: Displays the result (winner or draw) and provides options to restart or exit.
- **`restart`**: Resets the game board for a new match.

### Aesthetic Features
- **Blurred Background**: Uses the `Pillow` library to create a blurred effect when displaying results.
- **Dark Theme**: Ensures a consistent and modern aesthetic for the game.

## License
This project is licensed under the MIT License. Feel free to use and modify it as needed.

## Future Enhancements
- Adding an AI opponent for single-player mode.
- Implementing additional themes for the game interface.
- Enhancing animations and sound effects.

---
Enjoy playing Tic Tac Toe!

