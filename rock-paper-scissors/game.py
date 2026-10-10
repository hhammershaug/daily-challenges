# Import the random library
import random

# Track the total scores outside the function so they don't reset
countScorePlayer = 0;
countScoreComputer = 0;

# Function to start the game loop
def playGame():
    # Use the global keyword to modify variables outside the function scope
    global countScorePlayer, countScoreComputer
    
    # Define the available game options
    options = ["rock", "paper", "scissors"]

    # Print the game header to the terminal
    print("\n--- Rock, Paper, Scissors ---")
    
    # Prompt the user to enter their choice and convert to lowercase
    userChoice = input("Choose rock, paper, or scissors: ").lower()

    # Exception check: if input is not in options, print error and exit round
    if userChoice not in options:
        print("Invalid choice!, choose rock, paper, or scissors!")
        return
        
    # Get a random choice for the computer
    computerChoice = random.choice(options)
    print(f"Computer chose: {computerChoice}")

    # Check for a tie match
    if userChoice == computerChoice:
        print("It's a tie!")
        
    # Check all conditions where the user wins and increment player score
    elif (userChoice == "rock" and computerChoice == "scissors") or \
         (userChoice == "paper" and computerChoice == "rock") or \
         (userChoice == "scissors" and computerChoice == "paper"):
        print("YOU WIN!")
        countScorePlayer += 1

    # If it's not a tie and user didn't win, the computer wins and increments computer score
    else:
        print("Computer Wins!")
        countScoreComputer += 1

    # Print the current running score for the round
    print(f"Scoreboard -> Player: {countScorePlayer} | Computer: {countScoreComputer}")

# Standard main block to keep playing the game until closed
if __name__ == "__main__":
    # Create an infinite loop so you can play multiple rounds
    while True:
        playGame()
        
        # Ask the player if they want to keep playing using y/n format
        play_again = input("Play another round? (y/n): ").lower()
        if play_again != "y" and play_again != "yes":
            print("\nThanks for playing!")
            break
