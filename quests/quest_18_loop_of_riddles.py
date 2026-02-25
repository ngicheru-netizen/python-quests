#Quest 18: The Loop of Riddles
# This is a simple guessing game script that uses the while loop

secret_number = 7

user_guess = int(input("Welcome to the Loop of Riddles! Guess the secret number between 1 and 10: "))
while user_guess != secret_number:
    print("Wrong guess! Try again.")
    user_guess = int(input("Guess the secret number between 1 and 10: "))

print("Congratulations! You've guessed the secret number 7 and escaped the Loop of Riddles!")
