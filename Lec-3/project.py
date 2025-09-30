import random

num= random.randint(1,10)

while(1):
    guess=int(input("Enter any number between 1 to 100 : "))
    if guess==num :
        print("Congrats! You guessed the correct number!")
        break
    elif guess<num:
        print("Low! Guess again")
    else:
        print("High! Guess again")
