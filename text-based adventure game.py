def start_game():
    print("Welcome to the Text Adventure Game!")
    print("You find yourself in a mysterious room...")
    print("You see two doors: one on the left and one on the right.")
    while True:
        choice = input("Which door do you choose? Left or Right? ").lower()
        if choice == "left":
            print("You enter the left door and find a treasure chest. Congratulations, you win!")
            break
        elif choice == "right":
            print("You open the right door and fall into a pit. Game Over!")
            break
        else:
            print("Invalid choice. Please choose Left or Right.")


start_game()