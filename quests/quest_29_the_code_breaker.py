#define a secret code and the number of attempts allowed
secret_code = 42
attempts_no = 3


#while loop to allow the user to guess the code until they run out of attempts or guess correctly
while attempts_no > 0:
    # get user's guess
    guess = int(input(f"guess the number? {attempts_no} attempts remaining "))

    #check guess
    if guess == secret_code:
        print("Wonderful, you've guessed the correct number")
        break
    else:
        attempts_no -= 1 # reduce attempt by 1
        print("incorrect")
# run out of attempts
if attempts_no == 0:
    print(f"you are out of attempts, the code is {secret_code}.")


