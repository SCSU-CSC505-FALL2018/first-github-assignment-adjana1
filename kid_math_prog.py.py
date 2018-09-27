import random
import sys

print('Let us practice your math skills')

num1 = random.randint(50, 100)
num2 = random.randint(1, 50)



def add():
    print('Please add these numbers', num1, 'and', num2)
    result_add = float(input('What result did you get? ').strip())
    if result_add == num1 + num2:
        print('Your answer is correct')
        print('The answer is', (num1 + num2))
    else:
        print('Your answer is incorrect')
        print('The answer is', (num1 + num2))        


def subs():
    print('Please subtract', num2, 'from', num1)
    result_sub = float(input('What result did you get?').strip())
    if result_sub == (num1 - num2):
        print('Your answer is correct')
        print('The answer is', (num1 - num2))
    else:
        print('Your answer is incorrect')
        print('The answer is', (num1 - num2))


def mult():
    print('Please multiply', num1, 'and', num2)
    result_mul = float(input('what result did you get?').strip())
    if result_mul == num1 * num2:
        print('Your answer is correct')
        print('The answer is', (num1 * num2))
    else:
        print('Your answer is incorrect')
        print('The answer is', (num1 * num2))



def div():
    print('Please divide', num1, 'and', num2)
    result_div = float(input('what result did you get (to the nearest hundredth)?').strip())
    if result_div == (num1/num2):
        print('Your answer is correct')
        print('The answer is', round((num1 / num2), 2))
    else:
        print('Your answer is incorrect')
        print('The answer is', round((num1 / num2), 2))


print('Let us practice your math skills')

while True:
    math_type = input('\nplease tell me which type of problem you want to work on?\n addition\n subtraction\n multiplication\n division\n').strip().lower()

    if math_type == 'addition':
        add()

    elif math_type == 'subtraction':
        subs()

    elif math_type == 'multiplication':
        mult()

    else:
        div()
