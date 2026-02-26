# Quest 13: The Maze of Many Choices
# This program asks for a score and prints a grade.

score = int(input("Enter your score (0-100): "))

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
else:
    print("Needs some Improvement")
