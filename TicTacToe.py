#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random


board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]
currentPlayer = "X"
winner = None
gameRunning = True


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
        inp = int(input(f"Player {currentPlayer}, select a spot 1-9: "))
        if board[inp - 1] == "-":
            board[inp - 1] = currentPlayer
            break
        else:
            print("Oops, that spot is already taken. Please choose another spot.")


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
        gameRunning = False


def checkIfTie(board):
    global gameRunning
    if "-" not in board:
        printBoard(board)
        print("It is a tie!")
        gameRunning = False


# switch player
def switchPlayer():
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "O"
    else:
        currentPlayer = "X"


def computer(board):
    while True:
        position = random.randint(0, 8)
        if board[position] == "-":
            board[position] = "O"
            break  # break after placing the move to prevent endless loop


# Function to handle the multiplayer mode (Friend vs Friend)
def multiplayer(board):
    global gameRunning, currentPlayer
    while gameRunning:
        printBoard(board)
        print(f"Player {currentPlayer}'s turn:")
        playerInput(board)
        checkIfWin(board)
        checkIfTie(board)
        if not gameRunning:
            break  # If the game is over (tie or win), exit the loop
        switchPlayer()


# Main function
def startGame():
    global gameRunning, currentPlayer
    print("Welcome to Tic Tac Toe!")

    # Game mode prompt and loop
    while True:
        print("1: Play with Computer")
        print("2: Play with Friend")
        option = input("Select an option (1 or 2): ")

        if option == "1":
            while gameRunning:
                printBoard(board)
                if currentPlayer == "X":  # Player 1 turn
                    playerInput(board)
                    checkIfWin(board)
                    checkIfTie(board)
                if not gameRunning:
                    break  # If the game is over (tie or win), exit the loop
                switchPlayer()
                computer(board)  # AI turn
                checkIfWin(board)
                checkIfTie(board)
                switchPlayer()
            break  # Exit after the game ends
        elif option == "2":
            multiplayer(board)  # Friend vs Friend
            break  # Exit after the game ends
        else:
            print("Invalid option! Please select 1 or 2.")
            # The prompt will continue to ask for valid input until it's received.


startGame()

