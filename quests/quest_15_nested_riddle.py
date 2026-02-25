direction = input("Will you go left or right?: ")
if direction == "left":
    choice = input("Will you swim or wait? ")
    if choice ==  "swim":
        print("YOU FOUND THE TREASURE! YIPPY")
    else:
        print("Oh no pirates found the treasure before you.")
else:
    print("You end up in a Mexican market. Might as well buy a burrito")
