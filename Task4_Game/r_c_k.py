import random

user_score = 0
computer_score = 0

choices = ["rock", "paper", "scissors"]

print("===== ROCK PAPER SCISSORS GAME =====")
print("Instructions:")
print("Type rock, paper, or scissors to play.\n")

while True:
    user_choice = input("Enter your choice (rock/paper/scissors): ").lower()

    if user_choice not in choices:
        print("Invalid choice! Please enter rock, paper, or scissors.\n")
        continue

    computer_choice = random.choice(choices)

    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    if user_choice == computer_choice:
        print("It's a tie!")

    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "paper" and computer_choice == "rock") or
        (user_choice == "scissors" and computer_choice == "paper")
    ):
        print("You win!")
        user_score += 1

    else:
        print("Computer wins!")
        computer_score += 1

    print("\nScore:")
    print(f"You: {user_score}")
    print(f"Computer: {computer_score}")

    play_again = input("\nDo you want to play again? (yes/no): ").lower()

    if play_again != "yes":
        print("\n===== FINAL SCORE =====")
        print(f"You: {user_score}")
        print(f"Computer: {computer_score}")
        print("Thanks for playing!")
        break

    print()