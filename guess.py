# See the Instructions tab

# Set secret number
secret_number = 49
print("I'm thinking of a number between 1 and 99")


import random
secret_number = random.randint(1,99)
number =0

while number != secret_number :
  number= int(input("Enter a guess: "))
  if number < secret_number:      
    print("Your guess is too low")
  elif number > secret_number:
    print("Your guess is too high")
    
print(f"Congrats! The number was {secret_number}")
#Ask the user to guess
# Check to see if the guess is <, >, or = secret number
# Print the right message