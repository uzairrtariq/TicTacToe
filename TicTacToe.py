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
against = ""


#Initialized board with spaces
newBoard = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

def draw(newBoard):

    #Textual Presentation of the board
    print('   |   |')
    print(' ' + newBoard[6] + ' | ' + newBoard[7] + ' | ' + newBoard[8])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + newBoard[3] + ' | ' + newBoard[4] + ' | ' + newBoard[5])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + newBoard[0] + ' | ' + newBoard[1] + ' | ' + newBoard[2])
    print('   |   |')

def sign_select():

    p1_sign = input("Choose between X and O: ")
    p2_sign = ''

    #error
    while not (p1_sign.upper() == 'X' or p1_sign.upper() == 'O'):
        print("Please enter the correct input. X or O. Try again!")
        p1_sign = input("Choose between X and O: ")
    p1_sign = p1_sign.upper()
    p2_sign = p2_sign.upper()

    #assign player 2 sign upon player 1's
    if p1_sign.upper() == "X":
        p2_sign = 'O'
        player1_sign = p1_sign
        player2_sign = p2_sign
    else:
        p2_sign = 'X'
        player1_sign = p1_sign
        player2_sign = p2_sign

    #print basics for User's help
    print("You are: " + str(player1_sign))
    print("Player2 is : " + str(player2_sign))
    print("Let's begin! ")
    toss(player1_sign, player2_sign)

#Toss for first move
def toss(p1,p2):
    print("We will have a toss for who will go first.")
    HorT = input("You can choose; Head or Tails? Please type in 'H' or 'T': ")
    #UpperCase
    HorT = HorT.upper()

    #error
    while not (HorT.upper() == 'H' or HorT.upper() == 'T'):
        print("Please enter the correct input, H or T. Try again!")
        HorT = input("You can choose; Head or Tails? Please type in 'H' or 'T': ")

    #random_int = random.randint(1,2)
    random_int = 2
    heads = 1
    tails = 2

    #for testing purposes
    print("The random number is: " + str(random_int))

    #all possibilities of the toss
    if HorT.upper() == "H":
        if random_int == heads:
            print("Congratulations. You have won the toss and you will make the first move. ")
            print("Generating table for you..")
            print_slowly("LOADING")
            draw(newBoard)

            #print(str(against))

            if against.upper() == "HARD":
                ai(p1)
            elif against.upper() == "O":
                move(p1)
            elif against.upper() == "EASY":
                badAI(p1)


        elif random_int == tails:
            print("Ops! You lost the toss. Player 2 will make the first move!")
            print("Generating table for you..")
            print_slowly("LOADING")
            draw(newBoard)

            #print(str(against))
            if against.upper() == "HARD":
                ai_computerfirst(p2)
            elif against.upper() == "O":
                move(p2)
            elif against.upper() == "EASY":
                badAI_computerfirst(p2)



    elif HorT.upper() == "T":
        if random_int == tails:
            print("Congratulations. You have won the toss and you will make the first move. ")
            print("Generating table for you..")
            print_slowly("LOADING")
            draw(newBoard)

            #print(str(against))
            if against.upper() == "HARD":
                ai(p1)
            elif against.upper() == "O":
                move(p1)
            elif against.upper() == "EASY":
                badAI(p1)

        else:
            print("Ops! You lost the toss. Player 2 will make the first move!")
            print("Generating table for you..")
            print_slowly("LOADING")
            draw(newBoard)

            #print(str(against))
            if against.upper() == "HARD":
                ai_computerfirst(p2)
            elif against.upper() == "O":
                move(p2)
            elif against.upper() == "EASY":
                badAI_computerfirst(p2)


def print_slowly(text):
    for c in text:
        print(str(c)),
        sys.stdout.flush()
        sleep(0.5)


def play_against():
    global against
    against = input("Do you want to play against the computer or another opponent? type 'easy', 'hard' or just 'o' for opponent: ")
    #for error inputs
    while not (against.upper() == 'EASY' or against.upper() == 'O' or against.upper() == 'HARD'):
        print("Incorrect input. Please Try again!")
        against = input("Do you want to play against the computer or another opponent? type 'easy', 'hard' or just 'o' for opponent: ")

    against = against.upper()
    if against.upper() == 'O':
        sign_select()
    elif against.upper() == 'HARD':
        sign_select()
    elif against.upper() == "EASY":
        sign_select()


        #implement AI against the computer imposible to win level of difficulty har



#ToDo possibilities of win
def win(sign):
    #global newBoard
    #all win possibilities
    if newBoard[0] == sign and newBoard[1] == sign and newBoard[2] == sign:
        print("Congratulations, " + str(sign) + " won!")
        #newBoard = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        play_again()
    elif newBoard[3] == sign and newBoard[4] == sign and newBoard[5] == sign:
        print("Congratulations, " + str(sign) + " won!")
        #newBoard = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        play_again()

    elif newBoard[6] == sign and newBoard[7] == sign and newBoard[8] == sign:
        print("Congratulations, " + str(sign) + " won!")
        #newBoard = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        play_again()

    elif newBoard[0] == sign and newBoard[3] == sign and newBoard[6] == sign:
        print("Congratulations, " + str(sign) + " won!")

        #newBoard = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        play_again()

    elif newBoard[1] == sign and newBoard[4] == sign and newBoard[7] == sign:
        print("Congratulations, " + str(sign) + " won!")

        #newBoard = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        play_again()

    elif newBoard[2] == sign and newBoard[5] == sign and newBoard[8] == sign:
        print("Congratulations, " + str(sign) + " won!")

        #newBoard = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        play_again()

    elif newBoard[0] == sign and newBoard[4] == sign and newBoard[8] == sign:
        print("Congratulations, " + str(sign) + " won!")

        #newBoard = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        play_again()

    elif newBoard[6] == sign and newBoard[4] == sign and newBoard[2] == sign:
        print("Congratulations, " + str(sign) + " won!")

        #newBoard = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        play_again()

def play_again():
    again = input('Do you want to play again?(Yes or No):')
    while not (again.upper() == "YES" or again.upper() == "NO"):
        print('wrong input, please try again!')
        again = input('Do you want to play again?(Yes or No)')

    if again.upper() == "NO":
        print('Thanks for playing!')
        #exit everything
        sys.exit(0)
    else:
        global newBoard
        newBoard = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        return main()

# Generic Move function, can work for either sign
def move(s):
    while not (checkDraw(newBoard)):
        if not (win("X") or win("O")):
            placement = int(input("Where do you want to put your sign? (input from 1-9)"))
            #print("placement pass")
            placement = placement - 1

            while not isAvailable(newBoard, placement):
                print("This spot is already taken, please try another spot!")
                placement = int(input("Where do you want to put your sign? (input from 1-9)"))
                placement = placement - 1


                #ToDo also put in the while loop is that stop is already taken by X or O
                #while placement not in '1 2 3 4 5 6 7 8 9'.split():
                #print("That number is not in the range or that spot is already taken. Try again!")
                #lacement = int(input("Where do you want to put your sign? (input from 1-9)"))

            newBoard[int(placement)] = s
            #print("The move sign is " + str(s))
            #print("The final list is:" + str(newBoard))
            # newBoard[placement] == "X"
            draw(newBoard)


            if s == "X":
                s = "O"
            elif s == "O":
                s = "X"

    print("This is a draw!!!!!!")
    #initialize new board
    play_again()


def ai(s):
    while not (checkDraw(newBoard)):
        if not (win("X") or win("O")):
            placement = int(input("Where do you want to put your sign? (input from 1-9)"))
            print("placement pass")
            placement = placement - 1

            #Error
            while not isAvailable(newBoard, placement):
                print("This spot is already taken, please try another spot!")
                placement = int(input("Where do you want to put your sign? (input from 1-9)"))
                placement = placement - 1

            newBoard[placement] = s
            #print("The move sign is " + str(s))
            #print("The final list is:" + str(newBoard))
            # newBoard[placement] == "X"
            draw(newBoard)

            #sign flipping
            if s == "X":
                s = "O"
            elif s == "O":
                s = "X"

        if checkDraw(newBoard) or not(win("X") or win("O")):
            #Printing AI
            print_slowly("WAIT..")
            compmove = getComputerMove(newBoard)
            compmove = str(compmove)
            if compmove.isdigit():
                print("Now, computer is going to make a move!")
                #print(str(compmove))
                #print(str(s))
                compmove = int(compmove)
                newBoard[compmove] = s
                draw(newBoard)

                #sign flipping
                if s == "X":
                    s = "O"
                elif s == "O":
                    s = "X"
            else:
                print("This is a draw!!!!!!"
                      "You can do better, dude. ")
                play_again()

    print("This is a draw!!!!!!"
          "You can do better, dude.")
    play_again()

def badAI(s):
    while not (checkDraw(newBoard)):
        if not (win("X") or win("O")):
            placement = int(input("Where do you want to put your sign? (input from 1-9)"))
            print("placement pass")
            placement = placement - 1

            #Error
            while not isAvailable(newBoard, placement):
                print("This spot is already taken, please try another spot!")
                placement = int(input("Where do you want to put your sign? (input from 1-9)"))
                placement = placement - 1

            newBoard[placement] = s
            #print("The move sign is " + str(s))
            #print("The final list is:" + str(newBoard))
            # newBoard[placement] == "X"
            draw(newBoard)

            #sign flipping
            if s == "X":
                s = "O"
            elif s == "O":
                s = "X"

        if checkDraw(newBoard) or not(win("X") or win("O")):
            #Printing AI
            print_slowly("WAIT..")
            compmove = getComputerBadMove(newBoard)
            compmove = str(compmove)
            if compmove.isdigit():
                print("Now, computer is going to make a move!")
                #print(str(compmove))
                #print(str(s))
                compmove = int(compmove)
                newBoard[compmove] = s
                draw(newBoard)

                #sign flipping
                if s == "X":
                    s = "O"
                elif s == "O":
                    s = "X"
            else:
                print("This is a draw!!!!!!"
                      "You can do better, dude. ")
                play_again()

    print("This is a draw!!!!!!"
          "You can do better, dude.")
    play_again()

def ai_computerfirst(s):
    b = True

    while b == True:
        if not(win("X") and win("O")) :
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

            print(str(checkDraw(newBoard)))
            #and not(win("X") or win("O"))
        else:
            print("Computer has won the game!!!!!!")
            play_again()

        if checkDraw(newBoard):
            b = False
            print("This game is aa draw!")
            play_again()

        if not checkDraw(newBoard) and not(win("X") and win("O")) :
            placement = int(input("Where do you want to put your sign? (input from 1-9)"))
            print("placement pass")
            placement = placement - 1

            #if spot already taken (placement)
            while not isAvailable(newBoard, placement):
                print("This spot is already taken, please try another spot!")
                placement = int(input("Where do you want to put your sign? (input from 1-9)"))
                placement = placement - 1

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

    else:
        print ("oh boy")


    print("Computer won the game!!!!")
    play_again()

def badAI_computerfirst(s):
    b = True

    while b == True:
        if not(win("X") and win("O")) :
            #Printing AI
            print("Now, computer is going to make a move!")
            print_slowly("WAIT..")
            compmove = getComputerBadMove(newBoard)
            newBoard[compmove] = s
            draw(newBoard)

            #sign flipping
            if s == "X":
                s = "O"
            elif s == "O":
                s = "X"

            print(str(checkDraw(newBoard)))
            #and not(win("X") or win("O"))
        else:
            print("Computer has won the game!!!!!!")
            play_again()

        if checkDraw(newBoard):
            b = False
            print("This game is aa draw!")
            play_again()

        if not checkDraw(newBoard) and not(win("X") and win("O")) :
            placement = int(input("Where do you want to put your sign? (input from 1-9)"))
            print("placement pass")
            placement = placement - 1

            #if spot already taken (placement)
            while not isAvailable(newBoard, placement):
                print("This spot is already taken, please try another spot!")
                placement = int(input("Where do you want to put your sign? (input from 1-9)"))
                placement = placement - 1

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

    else:
        print ("oh boy")


    print("Computer won the game!!!!")
    play_again()



def checkDraw(b):
    return ' ' not in b

def getBoardCopy(b):
    #For testing the move on sample board and keeping the original
    dupeBoard = []
    for j in b:
        dupeBoard.append(j)
    return dupeBoard

def checkWin(b, m):
    return ((b[0] == m and b[1] == m and b[2] == m) or  # H top
            (b[3] == m and b[4] == m and b[5] == m) or  # H mid
            (b[6] == m and b[7] == m and b[8] == m) or  # H bot
            (b[0] == m and b[3] == m and b[6] == m) or  # V left
            (b[1] == m and b[4] == m and b[7] == m) or  # V centre
            (b[2] == m and b[5] == m and b[8] == m) or  # V right
            (b[0] == m and b[4] == m and b[8] == m) or  # LR diag
            (b[2] == m and b[4] == m and b[6] == m))  # RL diag

def testWinMove(b, mark, i):
    # i = the square to check if makes a win
    bCopy = getBoardCopy(b)
    bCopy[i] = mark
    return checkWin(bCopy, mark)

def randomComputerMove(b):
    #randomizer
    for i in range(0, 9):
        if b[i] == ' ':
            return i

def testForkMove(b, mark, i):
    # Determines if a move opens up a fork
    boardCopy = getBoardCopy(b)
    boardCopy[i] = mark
    win_possibities = 0
    for j in range(0, 9):
        if testWinMove(boardCopy, mark, j) and boardCopy[j] == ' ':
            win_possibities += 1
    return win_possibities >= 2


def getComputerMove(b):
    # Check player win moves
    for i in range(0, 9):
        if b[i] == ' ' and testWinMove(b, '0', i):
            return i
    # Check computer win moves
    for i in range(0, 9):
        if b[i] == ' ' and testWinMove(b, 'X', i):
            return i
    # Check computer fork opportunities
    for i in range(0, 9):
        if b[i] == ' ' and testForkMove(b, 'X', i):
            return i
    #  Check player fork opportunities
    for i in range(0, 9):
        if b[i] == ' ' and testForkMove(b, '0', i):
            return i
    # Play a corner
    for i in [0, 2, 6, 8]:
        if b[i] == ' ':
            return i
    # Play center
    if b[4] == ' ':
        return 4
    #Play a side
    for i in [1, 3, 5, 7]:
        if b[i] == ' ':
            return i

def getComputerBadMove(b):
    # Check computer win moves
    for i in range(0, 9):
        if b[i] == ' ' and testWinMove(b, 'X', i):
            return i
    # Check player win moves
    for i in range(0, 9):
        if b[i] == ' ' and testWinMove(b, '0', i):
            return i
    # Play a corner
    for i in [6, 8, 0, 2]:
        if b[i] == ' ':
            return i
    # Play center
    if b[4] == ' ':
        return 4
    #Play a side
    for i in [3, 7, 5, 1]:
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


