# Quest 28: The Adventure Begins
# This is a simple text-based adventure game that uses functions and if statements to create a branching

#This function starts the adventure and presents the user with a choice of two paths. 
def start():
    print("\nYou are standing in a dark forest.")
    print("There are two paths ahead of you.")
    choice = input("Do you go 'left' or 'right'? ").lower()

    if choice == "left":
        cave()
    elif choice == "right":
        river()
    else:
        print("Invalid choice. Try again.")
        start()

#This function represents the left path and presents the user with a choice to fight or run from a dragon.
def cave():
    print("\nYou enter a dark cave and find a dragon blocking your path!")
    choice = input("Do you 'fight' or 'run'? ").lower()

    if choice == "fight":
        print("\nYou bravely fight the dragon and defeat it. You are a legend! THE END.")
    elif choice == "run":
        print("\nYou run as fast as you can and escape safely. You live to fight another day! THE END.")
    else:
        print("Invalid choice. Try again.")
        cave()

#This function represents the right path and presents the user with a choice to swim or wait at a river.
def river():
    print("\nYou reach a wide river with a mysterious glow beneath the water.")
    choice = input("Do you 'swim' or 'wait'? ").lower()

    if choice == "swim":
        print("\nYou dive in and discover a chest of treasure at the bottom. You are rich! THE END.")
    elif choice == "wait":
        print("\nYou wait for hours but nothing comes. Night falls and you get lost in the dark. THE END.")
    else:
        print("Invalid choice. Try again.")
        river()


start()
