import random
def roll_dice():
    print("Welcome to the Dice Rolling Simulator!")
    while True:
        user_input = input("Enter 'exit' to end or press Enter to roll again: ").lower()

        if user_input == 'exit':
            print("Goodbye! Thanks for using the Dice Rolling Simulator.")
            break
        else:
            dice_roll = random.randint(1,6)
            print(f"You rolled a {dice_roll}!")



roll_dice()
