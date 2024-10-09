import random

playing = True
number = random.randint(1,100)
while playing:
    guess = int(input("Please enter your guessing number:) :"))
    if number == guess:
        print("you got the answer right, good job:)")
    else:
        print("sorry, but that is inccorrect")