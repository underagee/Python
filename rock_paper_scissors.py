# Write your solution below the starter code
# Follow the instructions in the tab to the right

#import random

# Welcome the user to the game
print("Welcome to rock, paper, scissors. Good luck!")

a = int(input("Enter your choice: 1 for Rock, 2 for Sccissors and 3 for Paper: "))

import random
b = random.randint(1,3)
print(f"Computer chooses {b}")

if a == b:
  print("It's a draw")
elif a == 1 and b == 2 or a == 2 and b == 1:
  print("Rock smashes scissors. Rock wins!")
elif a == 1 and b == 3 or a == 3 and b == 1:
  print("Paper covers Rock. Paper wins!")
elif a == 2 and b == 3 or a == 3 and b == 2:
  print("Scissors cuts Paper. Scissors wins!")
else:
  print("Try again!")

# Make a choice for the computer player
  
# Get a choice from the user
# Compare the user and computer choice
# Print the right message, based on the choices
