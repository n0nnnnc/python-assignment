import random as R

randInt = R.randint(1, 99)
# randInt = 7
lower = 1
upper = 99
print(" Welcome to the game of guessing number ".center(50, "*"))
for i in range(1, 6):
    print("round{}".format(i).center(50, "-"))
    guess = int(input("Enter an integer from {} to {} : ".format(lower, upper)))
    if guess < randInt:
        print("Hint: Your guess is low")
        lower = guess + 1
    elif guess > randInt:
        print("Hint: Your guess is high")
        upper = guess - 1
    else:
        break
print("#" * 50)
if guess == randInt:
    print("*** CONGRATURATION *** Your guess is correct".center(50))
else:
    print("!!!SORRY!!! The secret number is {}".format(randInt).center(50))
print("#" * 50)
