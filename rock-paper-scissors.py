import random
import simplegui

COMPUTER_SCORE = 0
HUMAN_SCORE = 0
human_choice = ""
computer_choice = ""

def choice_to_number(choice):
    return {'rock':0, 'paper':1, 'scissor':2}[choice]

def number_to_choice(number):
    return {0:'rock', 1:'paper', 2:'scissor'}[number]

def random_computer_choice():
    return random.choice(['rock','paper','scissor'])

def choice_result(human_choice, computer_choice):
    global COMPUTER_SCORE
    global HUMAN_SCORE
    computer_choice_number = choice_to_number(computer_choice)
    human_choice_number = choice_to_number(human_choice)
