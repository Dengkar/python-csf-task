import random

secret_number = random.randint(1,100)
while True:
    guess = int(input())
    if guess > secret_number:
        print("Too high")
    if guess < secret_number:
        print("Too low")
    else:
        print("you have guessed the correct number")
        break
