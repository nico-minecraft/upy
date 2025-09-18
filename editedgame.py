import sys

def intro():
    print("Welcome to the edited game!")
    print("You find yourself at a crossroads in a dark forest.")
    print("Do you go left or right?")

def left_path():
    print("You walk left and encounter a friendly elf.")
    print("He offers you a magic potion. Do you accept? (yes/no)")
    choice = input("> ").strip().lower()
    if choice == "yes":
        print("The potion gives you super strength! You win!")
    else:
        print("You politely decline and continue walking, but get lost. Game over.")

def right_path():
    print("You walk right and fall into a trap!")
    print("Do you try to escape or call for help? (escape/help)")
    choice = input("> ").strip().lower()
    if choice == "escape":
        print("You manage to escape and find treasure! You win!")
    else:
        print("No one hears you. Game over.")

def main():
    intro()
    choice = input("> ").strip().lower()
    if choice == "left":
        left_path()
    elif choice == "right":
        right_path()
    else:
        print("Invalid choice. Game over.")

if __name__ == "__main__":
    main()