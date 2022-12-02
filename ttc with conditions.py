blank_board = """
  1   2   3
1   |   |  
 --- --- ---
2   |   | 
 --- --- ---
3   |   |  
"""

name   = input("What is your name? ")
print("Welcome to Tic Tac Toe, " + name + ". Here is our playing board:")
print(blank_board)
position = input("Enter a position (i.e., 1,1): ")
print(position)

# TODO: Check the position is valid
# [your code here]
if position == "1,1" or "1,2" or "1,3" or "2,1" or "2,2" or "2,3" or "3,1" or "3,2" or "3,3":
  print(f"your position {position} is valid")
else:
  print("Oops! Invalid position")




# tic-tac-toe positions
a = " "
b = " "
c = " "
d = " "
e = " "
f = " "
g = " "
h = " "
i = " "

# TODO: Update the correct variable based on the position entered
# [your code here]
if position == '1,1':
  a = 'X'
elif position == '1,2':
  b = 'X'
elif position == '1,3':
  c = "x"
elif position == '2,1':
  d = "X"
elif position == '2,2':
  e = 'X'
elif position == '2,3':
  f = 'X'
elif position == '3,1':
  g = 'X'
elif position == '3,2':
  f = 'X'
elif position == '3,3':
 i = 'X'



# print the updated board
board = f"""
  1   2   3
1 {a} | {b} | {c}
 --- --- ---
2 {d} | {e} | {f}
 --- --- ---
3 {g} | {h} | {i}
"""
print(board)