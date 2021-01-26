import random

number = random.randint(1,100)
chances = 0
#print(number)
print("Guess a number (1 to 100)")

while chances<5:
    guess = int(input("Enter your guess: "))
    if guess == number:
        print("YOU WON!")
        chances +=5
    elif guess < number:
        if guess  > number - 5:
            print("low... but close")
        else:
            print("too low...")
    elif guess > number:
        if guess  < number + 5:
            print("high... but close")
        else:
            print("too high...")
    if guess != number:
        chances += 1
        print("You have",5-chances,"chances...")
if guess <= 5:
    print("YOU LOST")
    print("Random number is",number)