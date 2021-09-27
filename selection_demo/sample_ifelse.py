"""
# ---------------------------
# File           : sample_ifelse.py
# Created        : 27-09-2021 16:26
# Author         : Aishwarya
# Version        : v1.0.0
# Licensing      : (c) 2021 Aishwarya,LYIT
#                  Available under GNU Public License (GPL)
# Description    
# ifelse statement
"""
if __name__== "__main__":
    grade= 50
    module_1 ="python"

    if (grade>=70) and module_1 =="python":
        print("you have earned distinction")
    elif (grade >= 60):
        print("you have earned m.1")
    elif (grade >= 50):
        print("you have earned m.2")
    elif grade >= 40:
        print("you have passed")
    else:
        print("Please try again")