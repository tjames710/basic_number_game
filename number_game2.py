import random 

# Limit number of guesses allowed

# Catch when someone submits a non-integer




# generate a random number between 1 and 10
def secret_num():
    secret_num = random.randint(1, 10)
    return secret_num

    
def get_guess_from_user():
    while True:
        try:
            guess = int(input("Guess a number between 1 and 10 > "))
            break
        except ValueError:
            print("Must enter a valid number 1 - 10.")

    return guess

# Play again option
def play_again(): 
    while True:
        new_game = input("Would you like to play again? Y/N > ")
        if new_game == "Y":
            start = main()
            start
        elif new_game == "N":
            break
    return play_again


def main():

    secret_number = secret_num()

    while True:

        # get a number guess from the player
        users_guess = get_guess_from_user()
            

        # compare guess to secret number
        if  users_guess == secret_number:
            print("Congrats you've won! My number was {}.".format(secret_number))
            break
        elif users_guess > secret_number:
            print("Guess lower")
            continue
        elif users_guess < secret_number:
            print("Guess higher")
            continue



    
    return main


main()
play_again()

