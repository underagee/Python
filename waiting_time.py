import random, time

# TODO 1: Print a welcome message. Include "press Enter to start".
print("Welcome, How  fast is your reaction? Well let's see")
# TODO 2: use input() to wait for the user to press Enter
input()
# TODO 3: wait a random number of seconds, then print "DRAW!"
random.randint(0,10)
waiting_time  = random.randint(0,10)
print("Stay alert while waiting")
time.sleep(waiting_time)
print ("DRAW!")
# TODO 4: Time how long it takes for the user to press Enter. Get the current time with time.time()
#TimeTaken
start = time.time()
# TODO 5: use input() to wait for the user to press Enter
input()
# TODO 6: Use time.time() again to get the time after the user pressed Enter
stop = time.time()

# TODO 7: Subtract the stop time from the start time to get the elapsed time
reaction_time= stop-start 
# TODO 8: Print how long it took
print(f"Your reaction time was {reaction_time}s")
# TODO 9: Print different results, based on how long it took
if 0.1< reaction_time <0.3:
  print("You're the fastest draw in the west, congratulations! ")
elif reaction_time <0.1:
  print("You pressed Enter too soon, didn't you? ")
elif reaction_time >0.3:
  print("To slow! Try again next time. ")
