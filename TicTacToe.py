#FinalProject
#Tic-Tac-Toe
#Andrea and Uzair
#trial
#testing for andrea
import random

from time import sleep
import sys

#Public constants
player1_sign = ''
player2_sign = ''

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

    player1_sign = input("Choose between X and O: ")
    player2_sign = ''
    while not (player1_sign.upper() == 'X' or player1_sign.upper() == 'O'):
        print("Please enter the correct input. X or O. Try again!")
        player1_sign = input("Choose between X and O: ")
    player1_sign.upper()
    player2_sign.upper()

    if player1_sign.upper() == "X":
        player2_sign = "O"
    else:
        player2_sign = "X"

    print("You are: " + str(player1_sign.upper()))
    print("Player2 is :" + str(player2_sign.upper()))
    print("Let's begin! ")
    toss()

def Move1():
    num = input("Where do you want to put the " + str(player1_sign))

def toss():
    print("We will have a toss for who will go first.")

    HorT = input("You can choose; Head or Tails? Please type in 'H' or 'T': ")

    #UpperCase
    HorT = HorT.upper()

    while not (HorT.upper() == 'H' or HorT.upper() == 'T'):
        print("Please enter the correct input, H or T. Try again!")
        HorT = input("You can choose; Head or Tails? Please type in 'H' or 'T': ")



    random_int = random.randint(1,3)

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
        elif random_int == tails:
            print("Ops! You lost the toss. Player 2 will make the first move!")
            print("Generating table for you..")
            print_slowly("LOADING")
            draw(newBoard)

    elif HorT.upper() == "T":
        if random_int == tails:
            print("Congratulations. You have won the toss and you will make the first move. ")
            print("Generating table for you..")
            print_slowly("LOADING")
            draw(newBoard)
        else:
            print("Ops! You lost the toss. Player 2 will make the first move!")
            print("Generating table for you..")
            print_slowly("LOADING")
            draw(newBoard)

def print_slowly(text):
    for c in text:
        print(str(c)),
        sys.stdout.flush()
        sleep(0.5)


def play_again():
    again = input('Do you want to play again?(Yes or No):')
    while again.lower() != 'yes' or again.lower() != 'no':
        print('wrong input, please try again!')
        again = input('Do you want to play again?(Yes or No)')

    if again.lower() == 'no':
       print('Thanks for playing!')
    else:
        return main()




def play_against():

    against = input("Do you want to play against the computer or another opponent? type 'C' or 'O': ")

    #for error inputs
    while not (against.upper() == 'C' or against.upper() == 'O'):
        print("Incorrect input. Please Try again!")
        against = input("Do you want to play against the computer or another opponent? type 'C' or 'O': ")

    if against.upper() == 'O':
        sign_select()
        #implemet oponent
    elif against.upper() == 'C':
        sign_select()

        #implement AI against the computer imposible to win level of difficulty hard
        return 0

#possibilities of win
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


def main():

    print("Welcome to Textual Tic-Tac-Toe!")
    print("You can either play with a friend, or you can play against the computer!")
    play_against()

    #put it inside play against.
    #sign_select()

main()


