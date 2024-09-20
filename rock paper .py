import random

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def get_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (player_choice == "rock" and computer_choice == "scissors") or \
         (player_choice == "scissors" and computer_choice == "paper") or \
         (player_choice == "paper" and computer_choice == "rock"):
        return "You win!"
    else:
        return "Computer wins!"

def rock_paper_scissors():
    while True:
        player_choice = input("Enter rock, paper, or scissors (or 'quit' to exit): ").lower()
        if player_choice == "quit":
            print("Thanks for playing!")
            break
        if player_choice not in ["rock", "paper", "scissors"]:
            print("Invalid choice! Please try again.")
            continue
        
        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")
        
        result = get_winner(player_choice, computer_choice)
        print(result)

if __name__ == "__main__":
    rock_paper_scissors()
