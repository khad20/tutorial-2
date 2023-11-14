#exercise 1 part A
import random
hidden =  6
random_num = random.randint(1,20)
#user = input('guess a number between 1 and 20')

while(int({user}!=hidden)):
    print(f'sorry{user} is not the correct number')
    user = input('enter a number')
print(f'{user} was correct')

#while(True):
   # try:
    #    user = int(user)
    #except ValueError:
     #   print('please enter a number')
     #continue

#partB
import random
hidden =  6
random_num = random.randint(1,20)


while(int({user}!=hidden)):
    print(f'sorry{user} is not the correct number')
    user = input('enter a number')
print(f'{user} was correct')

#partC
import random
hidden =  6
is_matched = False
random_num = random.randint(1,20)
#user = input('guess a number between 1 and 20')

while(not is_matched):
    if random_num == hidden:
        print(f'sorry{random_num} is the correct number')
    is_matched= True
else:
    print(f'{random_num} is not  correct')
    random_num = random.randint(1,20)


