import os
from art import logo
import random as r
numbers = [x for x in range(1,100)]
cpu_choice = r.choice(numbers)
def compare(cpu,user):
    if user == cpu:
        return "You guess it!"
    if user < cpu:
        return "Too low!"
    if user > cpu:
        return "Too high!"
print(logo)
p_game = True
easy = 10
hard = 5
level = input('easy or hard: ')
if level == 'easy':
    os.system('clear')
    print(logo)
    print(f'You got {easy} chances...')
    while p_game:
        user_choice = int(input('Guess the number between 1 and 100: '))
        if compare(cpu_choice, user_choice) == 'You guess it!':
            p_game = False
        os.system('clear')
        print(logo)
        print(compare(cpu_choice, user_choice))
        easy -= 1
        if easy == 0:
            print('You lose all the chances..')
            break