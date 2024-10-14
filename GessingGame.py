import random
random_number = random.randint(1,15)
while True:
    guess = int(input("Guess a number between 1 and 15: "))
    if guess > random_number:
        print("TO HIGH !")
    elif guess < random_number:
        print("TO LOW !")
    else:
        print("YOU WON !")
        play_again=input("Do you wanna play again (y/n): ")
        if play_again == "y":
            random_number = random.randint(1,15)
            guess = None
        else:
            print("Thank you for playing. ")
            break