#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random

def get_computer_choice():
    """Generate a random choice for the computer."""
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    """Determine the winner based on the user and computer choices."""
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "user"
    else:
        return "computer"

def main():
    user_score = 0
    computer_score = 0
    play_again = 'yes'
    
    print("Rock-Paper-Scissors Game")

    while play_again.lower() == 'yes':
        # User input
        user_choice = input("Choose rock, paper, or scissors: ").lower()
        
        if user_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid choice. Please choose rock, paper, or scissors.")
            continue
        
        # Computer selection
        computer_choice = get_computer_choice()
        
        # Determine winner
        result = determine_winner(user_choice, computer_choice)
        
        # Display results
        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")
        
        if result == "tie":
            print("It's a tie!")
        elif result == "user":
            print("You win!")
            user_score += 1
        else:
            print("You lose!")
            computer_score += 1
        
        # Display scores
        print(f"Score - You: {user_score} | Computer: {computer_score}")
        
        # Play again
        play_again = input("\nDo you want to play another round? (yes/no): ")
    
    print("\nThanks for playing!")
    print(f"Final Score - You: {user_score} | Computer: {computer_score}")

if __name__ == "__main__":
    main()


# In[ ]:




