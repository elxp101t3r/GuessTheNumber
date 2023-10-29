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