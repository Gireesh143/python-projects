import random

top_of_range = input("Type a number for the top of range: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range<=0:
        print("please type a number larger than 0 next time")
        quit()
else:
    print("Please type a number next time.")
    quit()

random_number = random.randint(0,top_of_range)
guesses = 0

while True:
    guesses += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please type a number next time.")
        continue
    if user_guess == random_number:
        print("You got it!")
        break
    else:
        if user_guess > random_number:
            print("You are above the number!")
        else:
            print("You are below the number!")


print("You got it in "+str(guesses)+" guesses")



