"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Zuzana Burešová
email: zuza.buresova@centrum.cz
discord: zuza_34473
"""

from random import randint

separator = 47 * "-"

def introduction():
    """
    just greetings
    """
    print(f"Hi there!", separator, \
    "I\'ve generated a random 4 digit number for you.", \
    "Let\'s play a bulls and cows game.", separator, \
    "Enter a number:""", separator, sep ="\n")


def generate_random_number() -> list: 
    """
    generates a random x-digit number with non-repeating digits
    """
    random_number = 0
    while len(set(str(random_number))) != 4:
        random_number = randint(1000, 9999)
    return list(str(random_number))
    

def input_guess_number() -> list:
    """
    verifies that the user entered the guess_number correctly 
    and warns him of any errors
    """
    incorrect_input = True
    while incorrect_input == True:
        guess_number = input(">>> ")
        if guess_number.isnumeric() != True:
            print(f"You did not enter a number. Try it again:",\
             separator, sep="\n")
        elif len(guess_number) != 4:
            print(f"Your number is not 4 digits. Try it again:",\
             separator, sep="\n")
        elif (str(guess_number))[0] == "0":
            print(f"Your number must not start with '0'. Try it again:",\
             separator, sep="\n")
        elif len(set(str(guess_number))) < 4:
            print(f"Your number must not contain duplicates. Try it again:",\
             separator, sep="\n")
        else:
            incorrect_input = False
    else:
        return list(str(guess_number))


def evaluate_guess_number(number_1: list, number_2: list):
    """
    bull = correct code, correct position;
    cow = correct code, wrong position;
    print number of bulls and cows
    """
    cows = 0
    bulls = 0
    for index1, number1 in enumerate(number_1):
        for index2, number2 in enumerate(number_2):
            if number1 == number2 and index1 == index2:
                bulls += 1
            elif number1 == number2 and index1 != index2:
                cows += 1
    if bulls == 1 and cows == 1:
        print(f"{bulls} bull, {cows} cow\n{separator}")
    elif cows == 1:
        print(f"{bulls} bulls, {cows} cow\n{separator}")
    elif bulls == 1:
        print(f"{bulls} bull, {cows} cows\n{separator}")
    else:
        print(f"{bulls} bulls, {cows} cows\n{separator}")


def players_category(tips: int) -> str:
    if tips < 6:
        return "amazing!"
    elif tips < 11:
        return "average."
    else:
        return "not so good.."


def play_game():
    introduction()
    random_number = generate_random_number()
    #print(random_number)
    guess_number = input_guess_number()
    #print(guess_number)
    tips_number = 1
    category = players_category(tips_number)
    while random_number != guess_number:
        evaluate_guess_number(random_number, guess_number)
        guess_number = input_guess_number()
        tips_number += 1
    print(f"Correct, you\'ve guessed the right number\nin {tips_number} \
guesses!")
    print(separator)
    print(f"That\'s {category}", sep="\n")

if __name__ == "__main__":
    play_game()