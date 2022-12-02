# Write a program to find the minimum of numbers provided by the user

# Get how many numbers the user will enter
numbers = int(input("How many numbers will you enter? "))
# set some initial variables before the loop starts
i = 0
minimum = float('inf')

# write the loop
for i in range(numbers):
  number = int(input("Enter a number: "))
  # add code to get the integer and store it in a variable x
  if number < minimum:
    minimum = number
  # check whether x is smaller than minimum, and reassign minimum to it if so

print("The smallest number is:", minimum)