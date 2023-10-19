import random
secret_number = random.randint(1,100)
guess = int(input())

for i in range(1, guess + 1):
    if guess > secret_number:
        print("too high")
    if guess < secret_number:
        print("too low")
    else:
        print("you guessed the correct number")
    break
