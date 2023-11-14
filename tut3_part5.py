# Ask the user if they like Python
response = input("Do you like Python? (yes/no): ").lower()  # Convert the response to lowercase

# Check the response using if-elif-else
if response == 'yes' or response == 'y':
    print("You are on the right course.")
elif response == 'no' or response == 'n':
    print("You might change your mind.")
else:
    print("I did not understand your response.")
