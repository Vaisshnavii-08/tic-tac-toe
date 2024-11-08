import random

# Initialize the variables
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]
currentPlayer = "X"
winner = None
gameRunning = True

# Printing the game board
def printBoard(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("----------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("----------")
    print(board[6] + " | " + board[7] + " | " + board[8])

# Player input
def playerInput(board):
    while True:
        try:
            inp = int(input("Enter the number (1-9): ")) - 1
            if inp >= 0 and inp <= 8 and board[inp] == "-":
                board[inp] = "X"
                break
            else:
                print("Sorry! This cell is already taken or invalid input.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 9.")

# Computer move
def computerMove(board):
    while True:
        move = random.randint(0, 8)
        if board[move] == "-":
            board[move] = "O"
            break

# Switching player
def switchPlayer():
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "O"
    else:
        currentPlayer = "X"

# Check row for result
def checkRow(board):
    global winner
    if board[0] == board[1] == board[2] and board[2] != "-":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[5] != "-":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[8] != "-":
        winner = board[6]
        return True
    return False

# Check column for result
def checkColumn(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "-":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "-":
        winner = board[2]
        return True
    return False

# Check diagonal for result
def checkDiagonal(board):
    global winner
    if board[0] == board[4] == board[8] and board[8] != "-":
        winner = board[0]
        return True
    elif board[2] == board[5] == board[7] and board[7] != "-":
        winner = board[2]
        return True
    return False

# Check win
def checkWin(board):
    global gameRunning
    if checkRow(board) or checkColumn(board) or checkDiagonal(board):
        printBoard(board)
        print(f"The winner is {winner}")
        gameRunning = False
    elif "-" not in board:
        printBoard(board)
        print("It is a tie!!!")
        gameRunning = False

# Main game loop
while gameRunning:
    printBoard(board)
    if currentPlayer == "X":
        playerInput(board)
    else:
        computerMove(board)
    checkWin(board)
    switchPlayer()