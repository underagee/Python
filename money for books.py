# Write your code below. See the Instructions in the tab to the right
books = int(input("How many books do you want to buy? "))
money = int(input("How much do you have? "))
remainder = (books * 20) - money
if money >= books * 20:
  print("You have enough money, go for it!")
else:
  print(f"You need ${remainder} more to buy that number of books")
  