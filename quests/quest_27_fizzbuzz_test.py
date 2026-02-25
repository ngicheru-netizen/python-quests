#Quest 27: FizzBuzz Test

#This for loop iterates through the numbers 1 to 100 and checks if each number is divisible by 3, 5, or both.
for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)

