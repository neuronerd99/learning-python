import random

def get_choices(): ## function to create player and computer choices    
    player_choice = input ("Enter a choice (rock, paper, scissors):") ## player choice defined by user input
    options = ["rock", "paper", "scissors"] ## choices can only be selected from this list
    computer_choice = random.choice(options) ## computer choice is randomly selected from options
    choices = {"player": player_choice, "computer": computer_choice} ## dictionary in which choices are stored
    return choices

def check_win(player, computer): ## function to check winner
    print (f"You chose {player}, computer chose {computer}")
    if player == computer:
        return "It's a tie!"
    elif player == "rock":
        if computer == "scissors":
            return "Rock smashes scissors! You win! :)"
        else:
            return "Paper covers rock! You lose :("
    elif player == "paper":
        if computer == "rock":
            return "Paper covers rock! You win! :)"
        else:
            return "Scissors cuts paper! You lose :("
    elif player == "scissors":
        if computer == "paper":
            return "Scissors cuts paper! You win! :)"
        else:
            return "Rock smashes scissors! You lose :("

choices = get_choices()
result = check_win(choices["player"], choices["computer"]) ## calling check_win function with player and computer choices as arguments; choices["player"] value is obtained after user input and is stored in dict (same for computer choice)
print(result)

