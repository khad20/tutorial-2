total = 0

for i in range(5):
    try:
        num = float(input("Enter a number: "))
        total += num
    except ValueError:
        print("Invalid input. Please enter a valid number.")

print("The total of the 5 numbers is:", total)
