import random 

# Limit number of guesses allowed
# Catch when someone submits a non-integer
# Play again option

# generate a random number between 1 and 10
secret_num = random.randint(1, 10)




def main():
    while True:
        # get a number guess from the player
        guess = int(input("Guess a number between 1 and 10 > "))
        # compare guess to secret number
        if guess == secret_num:
            print("Congrats you've won! My number was {}.".format(secret_num))
            break
        elif guess > secret_num:
            print("Guess lower")
            continue
        elif guess < secret_num:
            print("Guess higher")
            continue
        # print hit/miss

main()