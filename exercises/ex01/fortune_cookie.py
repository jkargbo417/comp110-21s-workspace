"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730333820"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint


# Begin your solution here...
print("Your fortune cookie says...")
fortune: int = randint(1,4)
if (fortune == 1):
    print("You will get an A on your next exam")
else:
     if (fortune == 2):
         print("Your next COVID test will be negative")
     else:
         if (fortune == 3):
            print("Your best friend has a crush on you")
         else: 
            if (fortune == 4):
                print("You will become rich off of Dogecoin")
print("Now, go spread positive vibes!")
