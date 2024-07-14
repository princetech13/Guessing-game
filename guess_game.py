import random
def get_choice():
    player_choice = input("Enter a choice(rock,paper,scissors) " )
    options = ["rock","paper","scissors"]
    computer_choice = random.choice(options)
    choices ={"player": player_choice, "computer": computer_choice}
    return choices

def check_win(player,computer):
    print(f"you chose {player}, computer chose {computer}")
    if player == computer:
     return "it's a tie"
    
    elif player == "rock":
        if computer == "scissors":
            return "Rock smashes scissors! You won"
        else:
           return "Paper covers rock! You lose."
        
    elif player == "Paper":
        if computer == "rock":
            return "Paper covers rock! You won"
        else:
           return "scissors cuts paper! You lose."
        
    elif player == "Scissors":
        if computer == "Paper":
            return "scissors cut paper! You won"
        else:
           return "Paper smashes scissors! You lose."
        
choices = get_choice()
result = check_win(choices["player"],choices["computer"])
print(result)


