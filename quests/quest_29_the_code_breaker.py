secret_code = 42
attempts_no = 3



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

