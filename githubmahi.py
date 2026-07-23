import random
machine_no = random.randint(1,100)
attempt = 5
while attempt > 0:
 guess_no=int(input("enter your guessed no:"))
 if guess_no > machine_no:
    print(" oops!lower value")
 elif guess_no < machine_no:
    print("oops!higher value")
 else:
  print("congratulations!")
 break
attempt -= 1
print("attempts left:",attempt )
if attempt == 0:
  print("fail! you used all 5 attempts.")
  print("The correct number is:", machine_no)   
