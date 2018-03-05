# modules
import random
number = random.randint(1,9)
guess = 0
count = 0

while guess != number and guess != "exit ":
    guess = input("what's your guess? ")
    if guess == 'exit':
        break
    guess = int(guess)
    count += 1

    if guess < number:
        print("too low!")
    elif guess > number:
        print("too high!")
    else:
        print("you got it!")
        print("And it only took you", count, 'tries!')