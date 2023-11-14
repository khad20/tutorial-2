#a
import random

choice = input(
    """
    welcome to temperature converter!
    pick an option
    1-celsius to farenheit
    2-farenheit to celsius
    """
)

try:
    choice = int(choice)
except ValueError as e:
    print("please enter a  number")
    exit(1)

if choice == 1:
    celsius = input ('enter a temperature in celsius')
    try:
        celsius = float(celsius)
    except ValueError as e:
        print('please enter a number')
        exit(1)
    
    farenheit = celsius * 9 / 5 +32
    print(f'{celsius} is {farenheit}f')

elif choice == 2:
    farenheit = input ('enter a temperature inn farenheit')
    try:
        farenheit = float (farenheit)
    except ValueError as e:
        print('please enter a number')
        exit(1)
    celsius = farenheit -32 / 9 / 5
    print(f'{farenheit} f is {celsius}c')

#b
# Function to perform arithmetic operations
def calculate(num1, operator, num2):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 == 0:
            return "Error: Division by zero"
        return num1 / num2
    else:
        return "Invalid operator"

# Get user input for the expression
try:
    num1 = int(input("Enter the first integer: "))
    operator = input("Enter the operator (+, -, *, /): ")
    num2 = int(input("Enter the second integer: "))

    result = calculate(num1, operator, num2)

    print(f"Result: {result}")

except ValueError:
    print("Invalid input. Please enter valid integers.")
except Exception as e:
    print(f"An error occurred: {e}")


#c
# Get the cost of the meal from the diner
meal_cost = float(input("Enter the cost of the meal: $"))

# Get the diner's satisfaction level
satisfaction = int(input("Rate your satisfaction (1 = Totally satisfied, 2 = Satisfied, 3 = Dissatisfied): "))

# Calculate the tip based on the satisfaction level
if satisfaction == 1:
    tip_percentage = 20
elif satisfaction == 2:
    tip_percentage = 15
elif satisfaction == 3:
    tip_percentage = 10
else:
    print("Invalid satisfaction rating. Please choose 1, 2, or 3.")
    exit()

# Calculate the tip amount
tip_amount = (tip_percentage / 100) * meal_cost

# Report the satisfaction level and tip
print(f"Satisfaction Level: {satisfaction}")
print(f"Tip Amount: ${tip_amount:.2f}")
