"""
# ---------------------------
# File           : q2.py
# Created        : 27-09-2021 16:27
# Author         : Aishwarya
# Version        : v1.0.0
# Licensing      : (c) 2021 Aishwarya,LYIT
#                  Available under GNU Public License (GPL)
# Description    
# Read the 5 book title and its values
# After each title & values
# Show the running total
"""


counter = 0
running_total = 0.0
while counter < 5:
    book_title = input("Enter book title")
    book_cost = float(input("Enter book cost"))
    running_total = running_total + book_cost
    print("BookTitle  Book cost  Total")
    print("{} {} {}".format(book_title, book_cost, running_total))
    counter = counter + 1


