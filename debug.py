numbers = [62, 60, 53, 53, 33, 3, 25, 61, 36, 1, 69, 55, 56, 39, 32, 76, 20, 62, 47]

total = 0
for n in numbers:
  if n % 2 == 1:
    total += n

print(total)
