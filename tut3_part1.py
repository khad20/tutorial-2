#a
n = int(input('Give me a number over 100: '))
if n <= 100:
    print(n, 'is not over 100')

#b
x = int(input('Enter age'))
if x >= 18:
    print('can vote')
else:
    print('cant vote')


age = input('what is your age?')
try:
    age = int(age)
    if age >=18:
        print ('can vote')
    else:
        print ('cant vote')
except ValueError as e:
    print(f'you cannot use {age} as your age')
