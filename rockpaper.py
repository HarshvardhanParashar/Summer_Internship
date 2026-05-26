# Rock, Paper, Scissors Game userVs computer
import random
choices = ["rock", "paper", "scissors"]
user_score = 0
computer_score = 0
for i in range(5):
    user_choice = input("Enter your choice (rock, paper, scissors): ").lower()
    computer_choice= random.choices(choices)
    print(f"Computer choice: {computer_choice}")



if user_choice== computer_choice:
    print("Tie!")
elif ((user_choice=="rock" and computer_choice=="scissors") or 
    (user_choice=="paper" and computer_choice=="rock") or 
    (user_choice=="scissors" and computer_choice=="paper")):
    print("You win!")
    
    user_score += 1
else:
    print("Computer wins!")
    computer_score += 1

print(f"Final Score - You: {user_score}, Computer: {computer_score}")