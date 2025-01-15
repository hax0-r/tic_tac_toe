import random

board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]
currentPlayer = "Player X"
winner = None
gameRunning = True
scores = {"Player X": 0, "Player O": 0, "Ties": 0}
playerSymbols = {"Player X": "X", "Player O": "O"}
computerDifficulty = "Easy"


# game board
def printBoard(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("---------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("---------")
    print(board[6] + " | " + board[7] + " | " + board[8])


# take player input
def playerInput(board):
    while True:
        try:
            inp = int(input(f"{currentPlayer} ({playerSymbols[currentPlayer]}), select a spot 1-9: "))
            if inp < 1 or inp > 9:
                print("You can't enter a number outside of the range 1-9. Please choose a valid spot.")
            elif board[inp - 1] == "-":
                board[inp - 1] = playerSymbols[currentPlayer]
                break
            else:
                print("Oops, that spot is already taken. Please choose another spot.")
        except ValueError:
            print("Invalid input! Please enter a number between 1 and 9.")


# check for win or tie
def checkHorizontal(board):
    global winner
    if board[0] == board[1] == board[2] and board[0] != "-":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "-":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "-":
        winner = board[6]
        return True


def checkVertical(board):
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


def checkDiagonal(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[4] != "-":
        winner = board[2]
        return True


def checkIfWin(board):
    global gameRunning
    if checkHorizontal(board) or checkVertical(board) or checkDiagonal(board):
        printBoard(board)
        print(f"The winner is {winner}!")
        updateScores(winner)
        gameRunning = False


def checkIfTie(board):
    global gameRunning
    if "-" not in board:
        printBoard(board)
        print("It is a tie!")
        updateScores("Tie")
        gameRunning = False


# update scores
def updateScores(winner):
    if winner == playerSymbols["Player X"]:
        scores["Player X"] += 1
    elif winner == playerSymbols["Player O"]:
        scores["Player O"] += 1
    else:
        scores["Ties"] += 1


# switch player
def switchPlayer():
    global currentPlayer
    if currentPlayer == "Player X":
        currentPlayer = "Player O"
    else:
        currentPlayer = "Player X"


# computer move
def computer(board):
    if computerDifficulty == "Easy":
        computerEasy(board)
    elif computerDifficulty == "Medium":
        computerMedium(board)
    elif computerDifficulty == "Hard":
        computerHard(board)


def computerEasy(board):
    while True:
        position = random.randint(0, 8)
        if board[position] == "-":
            board[position] = playerSymbols["Player O"]
            print(f"Computer ({playerSymbols['Player O']}) chooses spot {position + 1}")
            break


def computerMedium(board):
    for i in range(9):
        if board[i] == "-":
            board[i] = playerSymbols["Player O"]
            if checkHorizontal(board) or checkVertical(board) or checkDiagonal(board):
                print(f"Computer ({playerSymbols['Player O']}) chooses spot {i + 1}")
                return
            board[i] = "-"
    computerEasy(board)


def computerHard(board):
    bestScore = -float('inf')
    bestMove = None
    for i in range(9):
        if board[i] == "-":
            board[i] = playerSymbols["Player O"]
            score = minimax(board, 0, False)
            board[i] = "-"
            if score > bestScore:
                bestScore = score
                bestMove = i
    if bestMove is not None:
        board[bestMove] = playerSymbols["Player O"]
        print(f"Computer ({playerSymbols['Player O']}) chooses spot {bestMove + 1}")


def minimax(board, depth, isMaximizing):
    if checkHorizontal(board) or checkVertical(board) or checkDiagonal(board):
        if winner == playerSymbols["Player O"]:
            return 1
        elif winner == playerSymbols["Player X"]:
            return -1
    if "-" not in board:
        return 0

    if isMaximizing:
        bestScore = -float('inf')
        for i in range(9):
            if board[i] == "-":
                board[i] = playerSymbols["Player O"]
                score = minimax(board, depth + 1, False)
                board[i] = "-"
                bestScore = max(score, bestScore)
        return bestScore
    else:
        bestScore = float('inf')
        for i in range(9):
            if board[i] == "-":
                board[i] = playerSymbols["Player X"]
                score = minimax(board, depth + 1, True)
                board[i] = "-"
                bestScore = min(score, bestScore)
        return bestScore


# multiplayer mode
def multiplayer(board):
    global gameRunning, currentPlayer
    while gameRunning:
        printBoard(board)
        print(f"{currentPlayer}'s turn:")
        playerInput(board)
        checkIfWin(board)
        checkIfTie(board)
        if not gameRunning:
            break
        switchPlayer()


# play with computer mode
def playWithComputer(board):
    global gameRunning, currentPlayer, computerDifficulty

    while True:
        print("Select difficulty level:")
        print("1: Easy")
        print("2: Medium")
        print("3: Hard")
        difficultyOption = input("Enter 1, 2, or 3: ")
        if difficultyOption == "1":
            computerDifficulty = "Easy"
            break
        elif difficultyOption == "2":
            computerDifficulty = "Medium"
            break
        elif difficultyOption == "3":
            computerDifficulty = "Hard"
            break
        else:
            print("Invalid option! Please enter 1, 2, or 3.")

    while gameRunning:
        printBoard(board)
        if currentPlayer == "Player X":
            playerInput(board)
            checkIfWin(board)
            checkIfTie(board)
        if not gameRunning:
            break
        switchPlayer()
        computer(board)
        checkIfWin(board)
        checkIfTie(board)
        switchPlayer()


# replay option
def replay():
    global board, gameRunning, currentPlayer
    board = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
    gameRunning = True
    currentPlayer = "Player X"


# main function
def startGame():
    global gameRunning, currentPlayer
    print("Welcome to Tic Tac Toe!")

    # Game mode prompt and loop
    while True:
        print("1: Play with Computer")
        print("2: Play with Friend")
        option = input("Select an option (1 or 2): ")

        if option == "1":
            playWithComputer(board)
            break
        elif option == "2":
            multiplayer(board)
            break
        else:
            print("Invalid option! Please select 1 or 2.")

    # Show final scores and replay option
    print("Final Scores:")
    for player, score in scores.items():
        print(f"{player}: {score}")

    while True:
        replayOption = input("Do you want to play again? (yes/no): ").strip().lower()
        if replayOption == "yes":
            replay()
            startGame()
            break
        elif replayOption == "no":
            print("Thanks for playing Tic Tac Toe!")
            break
        else:
            print("Invalid input! Please enter 'yes' or 'no'.")


startGame()
