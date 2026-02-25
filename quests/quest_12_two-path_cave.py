#Quest 12: The Two Path Cave
# This is a simple password checker. If user puts in the correct password the script prints "Access Granted" if not it prints "Access Denied"


password = "python2026"

password_input = input("Enter the password to access the cave: ")

if password_input == password:
    print("Access Granted . . . \nWelcome to the Two Path Cave!")  

else: 
    print("Access Denied")

