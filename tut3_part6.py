#a
try:
    n = input('Give me a number over 100: ')
    n = int(n)
    if n <= 100:
        print(n, 'is not over 100')
    else:
        print(n, 'is over 100')
except ValueError:
    print("Invalid input. Please enter a valid integer.")

#b
try:
    age = input('Enter your age: ')
    age = int(age)
    if age >= 18:
        print("You can vote")
    else:
        print("You are not old enough to vote")
except ValueError:
    print("Invalid input. Please enter a valid integer for your age.")
