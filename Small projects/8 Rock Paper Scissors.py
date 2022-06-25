"""Rock Paper Scissors game for two players."""
from getpass import getpass
num_of_rounds = int(input("Choose number of rounds: "))
name_player_1 = (input("Player one! Enter your name: ")).capitalize()
name_player_2 = (input("Player two! Enter your name: ")).capitalize()
score_player_1 = 0
score_player_2 = 0
CHOICE_OPTIONS = ("Rock", "Paper", "Scissors")


def serial_number_of_choice(name, choice):
    global CHOICE_OPTIONS
    print(name + "!")
    choice = getpass("Make a choice:\n# Rock\n#  Paper\n#  Scissors\n")
    choice = choice.capitalize()
    for serial_option in range(len(CHOICE_OPTIONS)):
        if choice == CHOICE_OPTIONS[serial_option]:
            return serial_option
        elif choice not in CHOICE_OPTIONS:
            print("Your choice is invalid!")
            serial_number_of_choice(name, choice)


while num_of_rounds >= 1:
    player_1_choice = CHOICE_OPTIONS[serial_number_of_choice(name=name_player_1, choice=player_1_choice)]
    player_2_choice = CHOICE_OPTIONS[serial_number_of_choice(name=name_player_2, choice=player_2_choice)]
    print('{:^10}'.format(name_player_1), "-->", '{:^10}'.format(player_1_choice))
    print('{:^10}'.format(name_player_2), "-->", '{:^10}'.format(player_2_choice))

    """for choice in range(len(CHOICE_OPTIONS)):
        if (player_1_choice == CHOICE_OPTIONS[serial_number_of_choice(name=name_player_1, choice=player_1_choice)])\
        and (CHOICE_OPTIONS[serial_number_of_choice(name=name_player_2, choice=player_2_choice)]):
            score_player_1 += 1
        elif (player_2_choice == CHOICE_OPTIONS[choice]) and (player_1_choice == [choice + 1]):
            score_player_2 += 1
        else:
            print("You both made the same choices, try again!")
    num_of_rounds -= 1"""


'''def name__main__(make_a_coice):
    make_a_choice(name=name_player_1, choice=player_1_choice)
    make_a_choice(name=name_player_2, choice=player_2_choice)'''