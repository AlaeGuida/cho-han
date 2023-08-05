
import random


def game_intro():
    intro = ("In this traditional Japanese dice game, "
             "two dice are rolled in a bamboo cup by the dealer sitting on the floor. "
             "The player must guess if the dice total to an even (cho) or odd (han) number")

    return intro


def bet():

    print(game_intro())

    user_input = input("You have 5000 Mon. How much do you bet? (or QUIT)\n>")

    if user_input.isdigit():
        try:
            if 0 < int(user_input) <= 5000:
                play(user_input)
            else:
                print("Please enter a valid amount 1 - 5000")
                bet()
        except:
            bet()

    elif user_input.upper() == 'QUIT':
        print('Thanks for playing')
        exit()

    else:
        print("Please enter a correct amount 1 - 5000 if you want to play, or 'QUIT' to exit")
        bet()



def play(bet):

    bet()