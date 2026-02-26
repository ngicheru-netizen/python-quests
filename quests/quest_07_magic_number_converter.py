# Quest 7: The Magic Number Converter
# This program asks the user for their birth year
# then calculates their approximate age.

birth_year = int(input("Enter your birth year: "))

current_year = 2026
age = current_year - birth_year

print(f"You are approximately {age} years old.")
