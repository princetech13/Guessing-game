import random

user_wins = 0
computer_wins = 0
options = ["rock","paper","scissors"]
while True:
    user_input = input("Type Rock/paper/Scissors or Q to Quit: " ).lower()
    if user_input == "q":
        break
        if user_input not in options:
            continue
        random_num = random.randint(0,2)
        # rock = 0, paper =1, scissors = 2
        computer_picked = options[random_num]
        print("computer picked", compter_picked + "." )
        if user_input == "rock" and computer_picked == "scissors":
            print("you won!")
            user_wins+=1
        elif user_input == "paper" and computer_picked == "rock":
            print("you won!")
            user_wins+=1
        elif user_input == "scissors" and computer_picked == "paper":
            print("you won!")
            user_wins+=1
    else:
        print("you lost!!")
        computer_wins+=1
print("you won", user_wins,"times")
print("The computer won", computer_wins,"times")
print("REPLAY!!")

