# Kibo FPWP Final Project
# Put your final project code in this file for submission
# Add the names of the authors, a brief description, and link to your video in the file called 'readme.md'
# Then, you can remove these instruction comments
name = input("What is your name? ")
print(f"Welcome {name}. This is a little test on the past world cups. Ready? Let's get it!")
print("\n")

score = 0
while score < 60:
  #Question 1
  print("1. Which country won the World Cup in 1990? ")
  countries = ["A.Italy", "B.France", "C.Germany", "D.Argentina"  ]
  for i in countries:
    print(i)
  for i in range(2):
    ans = input('Answer: ').lower()
    if ans == "c" or ans == "germany":
      print("Correct")
      score += 10
      break
    else:
      print("Wrong answer!")
                                          
                                      
  #Question 2
  # print
  print("2. Who were the winners in the the World Cup played in   2010")
  countries = ["A.Egypt", "B.Portugal", "C.Spain", "D.Argentina"  ]
  for i in countries:
    print(i)
  for i in range(2):
    ans = input('Answer: ').lower()
    if ans == "c"  or ans == "spain":
      print("Correct")
      score += 10
      break
    else:
      print("Wrong answer!")
                                      
                                      
  #Question 3
  print("3. Which country hosted the world cup in the year 2014?")
  countries = ["A.Brazil", "B.USA", "C.Russia", "D.Italy" ]
  for i in countries:
    print(i)
  for i in range(2):
    ans = input('Answer: ').lower()
    if ans == "a" or ans == "brazil":
      print("Correct")
      score += 10
      break
    else:
      print("Wrong answer!")
                                      
                                      
  #Question 4
  print("4. Runner up of World Cup 2018?")
  countries = ["A.Netherlands", "B.Croatia", "C.Mexico",         "D.Italy" ]
  for i in countries:
    print(i)
  for i in range(2):
    ans = input('Answer: ').lower()
    if ans == "b" or ans == "croatia":
      print("Correct")
      score += 10
      break
    else:
      print("Wrong answer!")
                                      
  #Question 5
  print("5. First country to win the World Cup?")
  countries = ["A.Uruguay", "B.Argentina", "C.Hungary", "D.Brazil"]
  for i in countries:
    print(i)
  for i in range(2):
    ans = input('Answer: ').lower()
    if ans == "a" or "uruguay":
      print("Correct")
      score += 10
      break
    else:
      print("Wrong answer!")
  
    #Question 6
  print("6.Which country got evicted first in the 2010 World Cup?")
  countries = ["A.Uruguay", "B.Argentina", "C.Hungary", "D.South Korea" ]
  for i in countries:
    print(i)
  for i in range(2):
    ans = input('Answer: ').lower()
    if ans == "d" or ans == "south korea":
      print("Correct")
      score += 10
      break
    else:
      print("Wrong answer!")
  
  #Question 7
  print("7.How many matches were played in the World Cup 2006?")
  countries = ["A.16", "B.32", "C.62", "D.50" ]
  for i in countries:
    print(i)
  for i in range(2):
    ans = input('Answer: ').lower()
    if ans == "c" or ans == "64":
      print("Correct")
      score += 10
      break
    else:
      print("Wrong answer!")
  
  #Question 8
  print("8.How many countries played in the first world cup hosted?")
  countries = ["A.10", "B.13", "C.24", "D.32" ]
  for i in countries:
    print(i)
  for i in range(2):
    ans = input('Answer: ').lower()
    if ans == "b" or ans == "13":
      print("Correct")
      score += 10
      break
    else:
      print("Wrong answer!")
    
  #Question 9
  print("9.Who was the man of the match in the first match of the World Cup 2022?")
  countries = ["A.Abdelkarim Hassan", "B.Akram Afif", "C.Michael Estrada", "D.Enner Valencia" ]
  for i in countries:
    print(i)
  for i in range(2):
    ans = input('Answer: ').lower()
    if ans == "d" or ans == "enner   valencia":
      print("Correct")
      score += 10
      break
    else:
      print("Wrong answer!")
  
  #Question 10
  print("10.When did the United States of America host the   World cup?")
  countries = ["A.1990", "B.1994", "C.1998", "D.2002" ]
  for i in countries:
    print(i)
  for i in range(2):
    ans = input('Answer: ').lower()
    if ans == "b" or ans == "1994":
      print("Correct")
      score += 10
      break
    else:
      print("Wrong answer!")
    
  
    
  Total = print(f"Your score: {(score)}/100")
                                        
  if score >= 60:
    print(" Congrats!! You passed the assessment")
  else:
      print("Failed!! please try again")
      print("\n---------------------------------------------\n")                              
                                          
