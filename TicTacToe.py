#FinalProject
#Tic-Tac-Toe
#Andrea and Uzair
#trial
import random

from time import sleep
import sys

#Public constants
player1_sign = ""
player2_sign = ""
global against
#Initialized board with spaces
newBoard = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

def draw(newBoard):

    #Textual Presentation of the board
    print('   |   |')
    print(' ' + newBoard[7] + ' | ' + newBoard[8] + ' | ' + newBoard[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + newBoard[4] + ' | ' + newBoard[5] + ' | ' + newBoard[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + newBoard[1] + ' | ' + newBoard[2] + ' | ' + newBoard[3])
    print('   |   |')

def sign_select():

    p1_sign = input("Choose between X and O: ")
    p2_sign = ''
    while not (p1_sign.upper() == 'X' or p1_sign.upper() == 'O'):
        print("Please enter the correct input. X or O. Try again!")
        p1_sign = input("Choose between X and O: ")
    p1_sign = p1_sign.upper()
    p2_sign = p2_sign.upper()

    if p1_sign.upper() == "X":
        p2_sign = 'O'
        player1_sign = p1_sign
        player2_sign = p2_sign
    else:
        p2_sign = 'X'
        player1_sign = p1_sign
        player2_sign = p2_sign

    print("You are: " + str(player1_sign))
    print("Player2 is : " + str(player2_sign))
    print("Let's begin! ")
    toss(player1_sign, player2_sign)


def toss(p1,p2):
    print("We will have a toss for who will go first.")

    HorT = input("You can choose; Head or Tails? Please type in 'H' or 'T': ")

    #UpperCase
    HorT = HorT.upper()

    while not (HorT.upper() == 'H' or HorT.upper() == 'T'):
        print("Please enter the correct input, H or T. Try again!")
        HorT = input("You can choose; Head or Tails? Please type in 'H' or 'T': ")

    random_int = random.randint(1,2)
    #random_int = 2
    heads = 1
    tails = 2

    #for testing purposes
    print("The random number is: " + str(random_int))

    if HorT.upper() == "H":
        if random_int == heads:
            print("Congratulations. You have won the toss and you will make the first move. ")
            print("Generating table for you..")
            print_slowly("LOADING")
            draw(newBoard)

            print(str(against))

            if against.upper() == "C":
                ai(p1)
            elif against.upper() == "O":
                move(p1)


        elif random_int == tails:
            print("Ops! You lost the toss. Player 2 will make the first move!")
            print("Generating table for you..")
            print_slowly("LOADING")
            draw(newBoard)

            print(str(against))
            if against.upper() == "C":
                ai_computerfirst(p2)
            elif against.upper() == "O":
                move(p2)



    elif HorT.upper() == "T":
        if random_int == tails:
            print("Congratulations. You have won the toss and you will make the first move. ")
            print("Generating table for you..")
            print_slowly("LOADING")
            draw(newBoard)

            print(str(against))
            if against.upper() == "C":
                ai(p1)
            elif against.upper() == "O":
                move(p1)

        else:
            print("Ops! You lost the toss. Player 2 will make the first move!")
            print("Generating table for you..")
            print_slowly("LOADING")
            draw(newBoard)

            print(str(against))
            if against.upper() == "C":
                ai_computerfirst(p2)
            elif against.upper() == "O":
                move(p2)


def print_slowly(text):
    for c in text:
        print(str(c)),
        sys.stdout.flush()
        sleep(0.5)

def play_against():
    against = input("Do you want to play against the computer or another opponent? type 'C' or 'O': ")
    #for error inputs
    while not (against.upper() == 'C' or against.upper() == 'O'):
        print("Incorrect input. Please Try again!")
        against = input("Do you want to play against the computer or another opponent? type 'C' or 'O': ")

    against = against.upper()



    if against.upper() == 'O':
        sign_select()
    elif against.upper() == 'C':
        sign_select()

        #implement AI against the computer imposible to win level of difficulty har



#ToDo possibilities of win
def win(sign):
    #all win possibilities
    if newBoard[7] == sign and newBoard[8] == sign and newBoard[9] == sign:
        #win
        print("Congratulations, " + str(sign) + " won!")
        play_again()
    elif newBoard[7] == sign and newBoard[5] == sign and newBoard[3] == sign:
        print("Congratulations, " + str(sign) + " won!")
        play_again()

    elif newBoard[7] == sign and newBoard[4] == sign and newBoard[1] == sign:
        print("Congratulations, " + str(sign) + " won!")
        play_again()

    elif newBoard[7] == sign and newBoard[5] == sign and newBoard[3] == sign:
        print("Congratulations, " + str(sign) + " won!")
        play_again()

    elif newBoard[4] == sign and newBoard[5] == sign and newBoard[6] == sign:
        print("Congratulations, " + str(sign) + " won!")
        play_again()

    elif newBoard[7] == sign and newBoard[5] == sign and newBoard[3] == sign:
        print("Congratulations, " + str(sign) + " won!")
        play_again()

    elif newBoard[1] == sign and newBoard[5] == sign and newBoard[9] == sign:
        print("Congratulations, " + str(sign) + " won!")
        play_again()

    elif newBoard[1] == sign and newBoard[2] == sign and newBoard[3] == sign:
        print("Congratulations, " + str(sign) + " won!")
        play_again()

    elif newBoard[9] == player1_sign and newBoard[6] == player1_sign and newBoard[3] == player1_sign:
        print("Congratulations, " + str(sign) + " won!")
        play_again()

def play_again():
    again = input('Do you want to play again?(Yes or No):')
    while not (again.lower() == 'yes' or again.lower() == 'no'):
        print('wrong input, please try again!')
        again = input('Do you want to play again?(Yes or No)')



    if again.lower() == 'no':
       print('Thanks for playing!')
    else:
        return main()

# Generic Move function, can work for either sign
def move(s):
    while not (win("X") or win("O")):

        if not (win("X") or win("O")):
            placement = int(input("Where do you want to put your sign? (input from 1-9)"))

            print("placement pass")

            #ToDo also put in the while loop is that stop is already taken by X or O
            #while placement not in '1 2 3 4 5 6 7 8 9'.split():
             #print("That number is not in the range or that spot is already taken. Try again!")
                    #lacement = int(input("Where do you want to put your sign? (input from 1-9)"))



            newBoard[placement] = s
            print("The move sign is " + str(s))
            print("The final list is:" + str(newBoard))
            # newBoard[placement] == "X"
            draw(newBoard)

            if s == "X":
                s = "O"
            elif s == "O":
                s = "X"
    print("this is a draw!!!!!!!")

def ai(s):
    while not (win("X") or win("O")):
        placement = int(input("Where do you want to put your sign? (input from 1-9)"))
        print("placement pass")

        #Error
        while not isAvailable(newBoard, placement):
            print("This spot is already taken, please try another spot!")
            placement = int(input("Where do you want to put your sign? (input from 1-9)"))

        newBoard[placement] = s
        print("The move sign is " + str(s))
        print("The final list is:" + str(newBoard))
        # newBoard[placement] == "X"
        draw(newBoard)

        #sign flipping
        if s == "X":
            s = "O"
        elif s == "O":
            s = "X"

        #Printing AI
        print("Now, computer is going to make a move!")
        print_slowly("WAIT..")
        compmove = getComputerMove(newBoard)
        newBoard[compmove] = s
        draw(newBoard)

        #sign flipping
        if s == "X":
            s = "O"
        elif s == "O":
            s = "X"

def ai_computerfirst(s):
    while not (win("X") or win("O")):

        #Printing AI
        print("Now, computer is going to make a move!")
        print_slowly("WAIT..")
        compmove = getComputerMove(newBoard)
        newBoard[compmove] = s
        draw(newBoard)

        #sign flipping
        if s == "X":
            s = "O"
        elif s == "O":
            s = "X"


        placement = int(input("Where do you want to put your sign? (input from 1-9)"))
        print("placement pass")

        #Error
        while not isAvailable(newBoard, placement):
            print("This spot is already taken, please try another spot!")
            placement = int(input("Where do you want to put your sign? (input from 1-9)"))

        newBoard[placement] = s
        print("The move sign is " + str(s))
        print("The final list is:" + str(newBoard))
        # newBoard[placement] == "X"
        draw(newBoard)

        #sign flipping
        if s == "X":
            s = "O"
        elif s == "O":
            s = "X"



#copied functions

def checkDraw(b):
    return ' ' not in b

def getBoardCopy(b):
    # Make a duplicate of the board. When testing moves we don't want to
    # change the actual board
    dupeBoard = []
    for j in b:
        dupeBoard.append(j)
    return dupeBoard

def testWinMove(b, mark, i):
    # b = the board
    # mark = 0 or X
    # i = the square to check if makes a win
    bCopy = getBoardCopy(b)
    bCopy[i] = mark
    return win(mark)

def randomComputerMove(b):
    #randomizer
    for i in range(0, 9):
        if b[i] == ' ':
            return i


def getComputerMove(b):
    # Check computer win moves
    for i in range(0, 9):
        if b[i] == ' ' and testWinMove(b, 'X', i):
            return i
    # Check player win moves
    for i in range(0, 9):
        if b[i] == ' ' and testWinMove(b, '0', i):
            return i
    # Play a corner
    for i in [7, 9, 1, 3]:
        if b[i] == ' ':
            return i
    # Play center
    if b[5] == ' ':
        return 5
    #Play a side
    for i in [4, 8, 6, 2]:
        if b[i] == ' ':
            return i


def isAvailable(board, placement):
    if newBoard[placement] == " ":
        return True
    else:
        return False

def main():

    print("Welcome to Textual Tic-Tac-Toe!")
    print("You can either play with a friend, or you can play against the computer!")
    play_against()

main()


