
import random

intro = ("In this traditional Japanese dice game, "
         "two dice are rolled in a bamboo cup by the dealer sitting on the floor. "
         "The player must guess if the dice total to an even (cho) or odd (han) number")

# game intro so the player know how it works

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
            else:                       # player has to enter a bet from 1 to 5000
                print(invalid_input)
                play(user_betting)
        except:
            bet()

    elif user_input.upper() == 'QUIT':  # this option for the player to quit the game
        print('Thanks for playing.')
        quit()
    else:       # in case the player enter an invalid input like their dog's name
        print(invalid_input)
        bet()


def play(bet_amount):

    first_dice = random.randint(1, 6)  # we generate 2 numbers from 1 to 6 because that's how dice is, only 6 numbers
    second_dice = random.randint(1, 6)

    is_even = True      # we set is_even as True

    if (first_dice + second_dice) % 2 == 0:     # if sum of the two generated numbers is even, we keep it as True
        is_even = True
    elif (first_dice + second_dice) % 2 == 1:   # if sum of the two generated numbers is even, we change it to False
        is_even = False

    # player has to decide either sum of the previous two generated numbers is gonna be odd or even.

    player_choice = input("   CHO (even)  or  HAN(odd)  ?\n> ")

    if player_choice.upper() == 'CHO':
        player_chose_even = True      # if player says even we set player_chose_even as True
        print("The dealer lifts the cup to reveal:\n", "   ", first_dice, " - ", second_dice)

        if player_chose_even == is_even:    # we compare sum of the two previous generated nums with player choice
            return_amount = int(bet_amount) * 2
            print("You Won", return_amount, "mon!")
        else:
            print("You Lost!")

    elif player_choice.upper() == 'HAN':
        player_chose_even = False       # again if player says even we set player_chose_even as False
        print("The dealer lifts the cup to reveal:\n", "   ", first_dice, " - ", second_dice)

        if player_chose_even == is_even:
            return_amount = int(bet_amount) * 2
            print("You Won", return_amount, "mon!")
        else:
            print("You Lost!")

    else:                                   # in case the player again enter their neighborhood's name
        print('Please enter a valid bet!')
        play(bet_amount)


user_betting = bet()
play(user_betting)
