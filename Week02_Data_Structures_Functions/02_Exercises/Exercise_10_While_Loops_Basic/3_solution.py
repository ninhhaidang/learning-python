#!/usr/bin/env python3
"""
Week 2 - Exercise 10: Basic While Loops
Solution File

Student Name: Solution
Date: Week 2
"""

import random

print("=== Week 2 - Exercise 10: Basic While Loops ===\n")

def play_guessing_game():
    print("=== Number Guessing Game ===\n")
    print("I'm thinking of a number between 1 and 100!")
    
    # Generate secret number
    secret_number = random.randint(1, 100)
    attempts = 0
    guesses = []
    
    while True:
        try:
            # Get user input
            guess = int(input("\nEnter your guess: "))
            
            # Validate range
            if guess < 1 or guess > 100:
                print("Please enter a number between 1 and 100!")
                continue
            
            attempts += 1
            guesses.append(guess)
            
            # Check guess
            if guess == secret_number:
                print(f"\nCongratulations! You guessed it in {attempts} attempts!")
                break
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print("Too low! Try again.")
                
        except ValueError:
            print("Please enter a valid number!")
            continue
    
    # Show game statistics
    print(f"\nGame Statistics:")
    print(f"- Secret number: {secret_number}")
    print(f"- Your attempts: {attempts}")
    print(f"- Your guesses: {guesses}")
    
    return attempts

def main():
    total_games = 0
    total_attempts = 0
    
    while True:
        attempts = play_guessing_game()
        total_games += 1
        total_attempts += attempts
        
        # Ask to play again
        while True:
            play_again = input("\nDo you want to play again? (y/n): ").lower()
            if play_again in ['y', 'yes']:
                print("\n" + "="*50)
                break
            elif play_again in ['n', 'no']:
                print(f"\nOverall Statistics:")
                print(f"- Games played: {total_games}")
                print(f"- Total attempts: {total_attempts}")
                print(f"- Average attempts per game: {total_attempts/total_games:.1f}")
                print("\nThanks for playing! Goodbye!")
                return
            else:
                print("Please enter 'y' for yes or 'n' for no.")

# Run the game
if __name__ == "__main__":
    main()
