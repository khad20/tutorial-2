import random

# Initialize a counter for doubles
double_count = 0
num_rolls = 100

for _ in range(num_rolls):
    # Simulate rolling two dice
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)

    # Check if it's a double (both dice have the same value)
    if die1 == die2:
        double_count += 1

print(f'Out of {num_rolls} you rolled {double_count} doubles')
