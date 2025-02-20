
# global variable list to make the tic toc toe board
board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

# set winner to false so while loop should work till winner is True
winner = False

# function to display board nicely in console 
def current_board(board):
    print(f" {board[0][0]} | {board[0][1]} | {board[0][2]} ")
    print("---|---|---")
    print(f" {board[1][0]} | {board[1][1]} | {board[1][2]} ")
    print("---|---|---")
    print(f" {board[2][0]} | {board[2][1]} | {board[2][2]} ")

# function to get whatever position the user wants to go in
def player_input():
    position = input("Enter position (1 - 9) ")
    if position == "exit":
        quit()
    return int(position)

# letting player x go and update the board lists to where the player went 
def player_turn(player):
    
    #receiving position that the user selected 
    # print("X's turn:")
    position = player_input()
    if position in (1, 2, 3, 4, 5, 6, 7, 8, 9):
    # based off the position update list 
        if position in [1, 2, 3]:
            if board[0][position -1] == " ":
                board[0][position - 1] = player
            else:
                print("Square taken. Try again")
                player_turn(player)
        elif position in [4, 5, 6]:
            if board[1][position -4] == " ":
                board[1][position - 4] = player
            else:
                print("Square taken. Try again")
                player_turn(player)
        elif position in [7, 8, 9]:
            if board[2][position - 7] == " ":
                board[2][position - 7] = player
            else:
                print("Square taken. Try again")
                player_turn(player)
    else:
        print("Only enter numbers from 1 -9 (including 9)")
        player_turn(player)

# transposing board to make the columns rows to be able to check for winner in the columns
def transpose_board():
    return [[board[j][i] for j in range(len(board))] for i in range(len(board[0]))]


#check if there is a winner 
def check_winner():
    # checking each row if all are x or o to determine winner 
    try:
        for row in board:
            for player in ("x", "o"):
                if all(cells == player for cells in row):
                    return f"Player {player} wins!!", True

        # checking columns by first transposing board with the transpose_board function and making the code more condensed
        for rows in transpose_board():
            for player in ("x", "o"):
                if all(cells == player for cells in rows):
                    return f"Player {player} wins!!", True

        # check if diagnole lines match all x's or all o's
        diagnole = []
        diagnole2 = []
        for rows in range(len(board)):
            diagnole.append(board[rows][rows])
            diagnole2.append(board[rows][-(rows + 1)])

        for player in ("x", "o"):
            if all(cell == player for cell in diagnole):
                return f"Player {player} wins!!", True
            elif all(cell == player for cell in diagnole2):
                return f"Player {player} wins!!", True

        # check if it's a tie 
        allBoardElements = [cell for row in board for cell in row]
        if all(cell != " " for cell in allBoardElements):
            return "It's a tie", True
    except Exception as e:
        print(f"There was a problem checking results {e}")

def play_game():
    try:
        print("X's turn:")
        player_turn("x")
        current_board(board)
        result = check_winner()
        if result != None:
            return result
        
        print("O's turn:")
        player_turn("o")
        current_board(board)
        result = check_winner()
        if result != None:
            return result
        
        return ()
    except Exception as e:
        print(f"There was an error in play_game() {e}")

current_board(board)
while winner == False:
    result = play_game()
    if True in result:
        print(result[0])
        winner = True