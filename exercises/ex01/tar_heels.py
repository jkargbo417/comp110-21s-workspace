"""An exercise in remainders and boolean logic."""

__author__ = "730333820"


# Begin your solution here...
x = int(input("Please enter an integer: "))
if (x % 2 == 0 and x % 7 == 0):
    print("TAR HEELS")
else:
    if (x % 2 == 0 and x % 7 >= 0):
        print("TAR")
    else:
        if (x % 2 >= 0 and x % 7 == 0):
            print("HEELS")
        else:
            if (x >= 0 and x % 7 >= 0):
                print("CAROLINA")
        
