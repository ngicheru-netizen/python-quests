#Quest 24: Master Spell
#This quest is all about functions. Passing on one function's output to another function

def ask_for_age():
    age = int(input("Welcome to the Master Spell!\nTo proceed, please enter your age: "))
    return age

def can_they_vote(age):
    if age >= 18:
        return True
    else:
        return False

#Ask the user for their age
user_age = ask_for_age()

#Pass the result from the ask_for_age function to the can_they_vote function
can_they_vote(user_age)

if can_they_vote(user_age) == True:
    print("Congratulations! You are old enough to vote!")
else:
    print("Sorry, you are not old enough to vote")

