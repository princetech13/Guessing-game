# This is a computer base game which allow you to know different part 
# computer what they stand for
score = 0

print("Welcome to my computer game!!!")
playing = input("Do you want to play? ")
print("Okay!, let play!!!")
if playing.lower() != "yes":
     quit()
answer = input("what is the full meaning of cpu? ")
if answer .lower()== "central processing unit":
     print("correct!")
     score+=1
else:
     print("incorrect!")
answer = input("what is the full meaning of GUI? ")
if answer.lower() == "graphical user interface":
     print("correct!")
     score+=1
else:
     print("incorrect!")
answer = input("what is the full meaning of PSU? ")
if answer.lower() == "power supply unit":
     print("correct!")
     score+=1
else:
     print("incorrect!")
answer = input("what is the full meaning of Ram? ")
if answer.lower() == "random access memory":
     print("correct!")
     score+=1
else:
     print("incorrect!")

print("you got" " " + str((score / 4)*100 ) + "%")

