"""
# ---------------------------
# File           : q1.py
# Created        : 27-09-2021 16:27
# Author         : Aishwarya
# Version        : v1.0.0
# Licensing      : (c) 2021 Aishwarya,LYIT
#                  Available under GNU Public License (GPL)
# Description    
# Guessing game
# Getting the input from the user
# compare the guess & actual number
# until get the right answer
# Ask the user want to retry
"""
actual_number = 10
while 1:
    guess = int(input("Try to guess the number (1-10):"))
    if guess == actual_number:
        print("YES, you have guessed it.Its {}".format(actual_number))
        break
    else:
        retry = input("Wrong guess, Do you want to try again, Enter N for No, Y for Yes")
        if retry == "N":
            break
