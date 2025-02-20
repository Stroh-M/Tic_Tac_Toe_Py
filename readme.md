
# Tic-Tac-Toe Game

This is a simple console-based Tic-Tac-Toe game where two players (Player X and Player O) can take turns and play until there is a winner or a tie.

## Features

- Two-player gameplay (Player X vs Player O)
- Input validation (only allows positions between 1 and 9)
- Winner detection (checks rows, columns, and diagonals)
- Tie detection (when all cells are filled and no winner is found)
- Error handling for invalid moves and positions

## Installation

No installation required. Just clone or download the repository, and run the Python file.

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/tic-tac-toe.git
   ```

2. Navigate to the directory containing the game:
   ```bash
   cd tic-tac-toe
   ```

3. Run the game:
   ```bash
   python tic_tac_toe.py
   ```

## How to Play

1. The game is played on a 3x3 board.
2. Player X and Player O take turns to mark a spot on the board.
3. To make a move, enter the number corresponding to the position on the board (1 to 9):
   ```
   1 | 2 | 3
   ---|---|---
   4 | 5 | 6
   ---|---|---
   7 | 8 | 9
   ```

4. The game will check for a winner after each move and declare the winner when a player completes a row, column, or diagonal.
5. If all spots are filled and there’s no winner, it’s a tie.

### Example Game Flow

```
Enter position (1 - 9): 5
X's turn:
Enter position (1 - 9): 3
O's turn:
Enter position (1 - 9): 1
X's turn:
Enter position (1 - 9): 9
O's turn:
...
```

## Contributing

Feel free to fork the repository and submit pull requests for any improvements or fixes.  
