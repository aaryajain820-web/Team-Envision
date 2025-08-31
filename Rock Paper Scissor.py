# Rock Paper Scissor Game
# In this game, you type your choice: rock, paper, or scissors.
# The computer will randomly pick its own choice, and then the winner is decided using the classic rules: 
# rock beats scissors, scissors beats paper, and paper beats rock. 
# If both choices are the same, the game ends in a tie.

import random

# Function to display instructions
def display_instructions():
    print("\nWelcome to Rock, Paper, Scissors!")
    print("Rules:")
    print(" Rock beats Scissors")
    print(" Scissors beats Paper")
    print(" Paper beats Rock")
    print("Type 'exit' anytime to quit.\n")

# Function to get computer choice
def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

# Function to determine winner
def determine_winner(player, computer):
    if player == computer:
        return "draw"
    elif (player == "rock" and computer == "scissors") or \
         (player == "scissors" and computer == "paper") or \
         (player == "paper" and computer == "rock"):
        return "player"
    else:
        return "computer"

# Function to play one round
def play_round():
    player_choice = input("Enter Rock, Paper, or Scissors: ").lower()
    
    if player_choice == "exit":
        return None, None, "exit"
    if player_choice not in ["rock", "paper", "scissors"]:
        print("Invalid input! Please try again.\n")
        return None, None, "invalid"
    
    computer_choice = get_computer_choice()
    print(f"Computer chose: {computer_choice.capitalize()}")
    
    winner = determine_winner(player_choice, computer_choice)
    
    if winner == "draw":
        print("It's a draw!\n")
    elif winner == "player":
        print("You win this round!\n")
    else:
        print("Computer wins this round!\n")
    
    return player_choice, computer_choice, winner

# Main function
def main():
    display_instructions()
    player_score = 0
    computer_score = 0
    
    while True:
        _, _, result = play_round()
        
        if result == "exit":
            print("Thanks for playing! Final scores:")
            print(f" You: {player_score} | Computer: {computer_score}")
            break
        elif result == "invalid":
            continue
        elif result == "player":
            player_score += 1
        elif result == "computer":
            computer_score += 1

        print(f"Current Score -> You: {player_score}, Computer: {computer_score}\n")

if __name__ == "__main__":
    main()

