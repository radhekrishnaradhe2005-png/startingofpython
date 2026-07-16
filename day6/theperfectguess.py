## WE are going to write a program which generates random number and ask the user to guess it 

''' if the player's guess is higher than the actual number ,then the program diaplay "lower number please "
    .similarly if the user guess id too low the nit should display " higher the number please"
    .when the guess is correct the program display the number of guesses '''
import random

class PerfectGuess:
    def __init__(self):
        self.target = random.randint(1, 100)
        self.guesses = 0

    def play(self):
        while True:
            guess = int(input("Enter your guess (1-100): "))
            self.guesses += 1

            if guess == self.target:
                print("Congratulations! You guessed the number correctly.")
                print(f"Number of guesses: {self.guesses}")
                break

            elif guess > self.target:
                print("Lower number please")

            else:
                print("Higher number please")


game = PerfectGuess()
game.play()

