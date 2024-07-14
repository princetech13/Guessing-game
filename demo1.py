import random
def get_choice():
    player_choice = input("Enter a choice (Rock,Paper,Scissors) ")
    options = ["Rock","Paper","Scissors"]
    computer_choice = random.choice(options)
    choices = {"player" : player_choice, "computer" : computer_choice}
    return choices

def check_win(player, computer):
    score = 0
    print(f"you chose {player}, computer chose {computer}")
    if player == computer :
       print("its a tie")
    
    elif player == "Rock":
        if computer == "Paper" :
            print("Rock smashes Paper! You won")
       
        else:
            print("Paper smashes Rock!  You lose")
            
    elif player == "Paper" :
        if computer == "Rock":
            print("Paper smashes Rock! You won")
           
        else:
            print("Rock smashes Paper! You lose")
    
    elif player == "Scissors" :
        if computer == "Paper" :
            print("Scissors cuts Paper! You won")
           
        else:
            print("Paper smashes Scissors! You lose")
    
output = get_choice()
result = check_win(output["player"], output["computer"])
print(result)

