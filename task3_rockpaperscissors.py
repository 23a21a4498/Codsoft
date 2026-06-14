import random

choices = ["rock", "paper", "scissors"]

while True:
    user = input("Enter rock, paper, or scissors: ").lower()
    computer = random.choice(choices)

    print("You chose:", user)
    print("Computer chose:", computer)

    if user == computer:
        print("It's a Tie!")
    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        print("You Win!")
    else:
        print("Computer Wins!")

    play_again = input("Play again? (yes/no): ").lower()

    if play_again != "yes":
        print("Game Over!")
        break