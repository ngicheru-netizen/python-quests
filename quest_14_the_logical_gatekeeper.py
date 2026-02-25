#!/usr/bin/env python3

age=int(input("what is your age? "))
gold=int(input("How much gold do you have? "))


def enter_club (age, gold):
    if age >= 18 and gold >= 20:
        print ("Welcome! Come on in!!")
    else:
        print ("Sorry, you'll need to be 18+ and have 20+ gold coins to come in. Maybe next time")

enter_club(age, gold)
