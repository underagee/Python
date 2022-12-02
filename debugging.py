# Original instructions: Print the sum of the odd numbers between 10 and 25
# Add print statements to debug the code
total = 0
print(f"Before the loop, total is {total}")
for i in range(10,25,2):
  print(f"i is {i}, total is {total}")
  total + i
print(f"After the loop, total is {total}")
print(total)


# What is wrong with the code? (answer in a comment)
# The range should begin with 11(instead of 10)
# The range should end with 26 (instead of 25)
# The increment should be total += i (instead of total + i) 