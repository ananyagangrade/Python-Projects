import random
emojis = {'r': '✊', 'p': '✋', 's': '✌️'}
choices = tuple(emojis.keys())

def get_user_choice():
 while True:
    user_choice = input("Rock, Paper, or Scissors? (r,p,s): ").lower()
    if user_choice in choices:
        return user_choice
    else:
        print("Invalid Choice")


def display_choices(user_choice,comp_choice):
    print(f'You chose {emojis[user_choice]}')
    print(f'Computer chose {emojis[comp_choice]}')


def determine_winner(user_choice,comp_choice):
    if user_choice == comp_choice:
        print("Tie.")
    elif (
        (user_choice == 'r' and comp_choice == 's') or
        (user_choice == 's' and comp_choice == 'p') or
        (user_choice == 'p' and comp_choice == 'r')
    ):
        print("You win!")
    else:
        print("You lost.")


def play_game():
 while True:
    user_choice = get_user_choice()
    comp_choice = random.choice(choices)
    display_choices(user_choice,comp_choice)
    determine_winner(user_choice,comp_choice)


    cont = input("Continue? (y/n): ").lower()
    if cont == 'n':
        break
play_game()