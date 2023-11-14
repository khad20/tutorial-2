#a
x = int(input('Give me a number: '))
if x < 0:
    print(x, 'is negative')
else:
    print(x, 'is positive')

#b
mark = input('enter mark')
try:
    mark = int(mark)
    if mark < 40:
        print ('fail')
    else:
        print ('pass')
except ValueError as e:
    print(f'you cannot use {mark} as your mark')
 #c

num = int(input('Enter a number: '))
if num % 2 == 0:
    print(f'{num}is an even number')
else:
    print(f'{num} is an odd number')