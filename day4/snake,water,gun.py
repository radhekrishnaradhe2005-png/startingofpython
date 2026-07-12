import random

def check_winner(user, computer):
    if user == computer:
        return "Draw"

    elif (
        (user == "snake" and computer == "water") or
        (user == "water" and computer == "gun") or
        (user == "gun" and computer == "snake")
    ):
        return "You Win!"

    else:
        return "Computer Wins!"


choices = ["snake", "water", "gun"]

computer = random.choice(choices)

user = input("Enter snake, water, or gun: ").lower()

result = check_winner(user, computer)

print("You chose:", user)
print("Computer chose:", computer)
print(result)