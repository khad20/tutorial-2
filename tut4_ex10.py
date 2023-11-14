import random

# Generate a random number between 1 and 20
hidden_number = random.randint(1, 20)

# Set the maximum number of attempts
max_attempts = 5
attempts = 0

print("Welcome to the Guess the Number Game!")

while attempts < max_attempts:
    guess = int(input(f"Guess the number (between 1 and 20). Attempts remaining: {max_attempts - attempts}: "))

    if guess == hidden_number:
        print(f"Congratulations! You guessed the number {hidden_number} in {attempts + 1} attempts.")
        break
    elif guess < hidden_number:
        print("The correct number is higher.")
    else:
        print("The correct number is lower.")
    
    attempts += 1

if attempts == max_attempts:
    print(f"Sorry, you've run out of attempts. The hidden number was {hidden_number}.")
