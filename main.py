
import random

intro = ("In this traditional Japanese dice game, "
         "two dice are rolled in a bamboo cup by the dealer sitting on the floor. "
         "The player must guess if the dice total to an even (cho) or odd (han) number")

print(intro)


def bet():

    game_start = ("The dealer swirls the cup and you hear the rattle of dice."
                  "The dealer slams the cup on the floor, still covering the"
                  "dice and asks for your bet!")

    invalid_input = "Please enter a valid amount (1 - 5000)!"

    user_input = input("You have 5000 mon. How much do you bet? (or QUIT)\n> ")

    if user_input.isdigit():
        try:
            if 0 < int(user_input) <= 5000:
                print(game_start)
                return user_input
            else:
                print(invalid_input)
                play(user_betting)
        except:
            bet()

    elif user_input.upper() == 'QUIT':
        print('Thanks for playing.')
        quit()
    else:
        print(invalid_input)
        bet()


def play(bet_amount):

    first_dice = random.randint(1, 6)
    second_dice = random.randint(1, 6)

    is_even = True

    if (first_dice + second_dice) % 2 == 0:
        is_even = True
    elif (first_dice + second_dice) % 2 == 1:
        is_even = False

    user_choice = input("   CHO (even)  or  HAN(odd)  ?\n> ")

    user_chose_even = True

    if user_choice.upper() == 'CHO':
        user_chose_even = True
    elif user_choice.upper() == 'HAN':
        user_chose_even = False
    else:
        print("Please enter a valid bet!")
        play(user_betting)

    print("The dealer lifts the cup to reveal:\n", "   ", first_dice, " - ", second_dice)

    if user_chose_even == is_even:
        bet_amount = int(bet_amount)*2
        print("You Won", bet_amount, "mon!")

    else:
        # int(new_balance) -= int(bet_amount) ask the player to play again or not
        print("You Lost!")


user_betting = bet()
play(user_betting)
