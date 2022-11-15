#Checking for numtiples of 3
num = int(input("Enter a multiple 0f 3: "))
if num % 3 == 0:
  print(f"{num} is a multiple of 3")
else:
  print(num)

#Checking for multiples of 5
numm = int(input("Enter a multiple of 5: "))
if numm % 5 == 0:
  print(f"{numm}is a mutliple of 5")
else:
  print(numm)

#Checking for multiples of both 3 and 5
nummm = int(input("Enter a mulitple of both 3 and 5: "))
if nummm % 3 == 0 and nummm % 5 == 0:
  print(f"{nummm} is a multiple of both 3 and 5")
else:
  print(nummm)