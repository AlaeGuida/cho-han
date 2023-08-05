
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
                print("Please enter a valid amount (1 - 5000)")
                bet()
        except:
            bet()

    elif user_input.upper() == 'QUIT':
        print('Thanks for playing')
        exit()

    else:
        print("Please enter a valid amount (1 - 5000) if you want to play, or 'QUIT' to exit")
        bet()


def play(user_bet):

    game_start = (" The dealer swirls the cup and you hear the rattle of dice."
                  "The dealer slams the cup on the floor, still covering the"
                  "dice and asks for your bet.")

    print(game_start)

    first_dice = random.randint(1, 6)
    second_dice = random.randint(1, 6)

    result = ""

    user_choice = input("   'even'  or  'odd'  ?\n>")

    print("The dealer lifts the cup to reveal:\n", "   ", first_dice, " - ", second_dice)

    calc = (first_dice + second_dice) % 2

    if calc == 0:
        result = "even"
    elif calc == 1:
        result = "odd"

    if user_choice.lower() == result:
        print("You Won", (user_bet * 2), "!")
    elif user_choice.lower() != result:
        print("You Lost!")


bet()
