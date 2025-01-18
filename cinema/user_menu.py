import inquirer

from os import  system

def user_menu():
    system('cls')
    questions = [inquirer.List(name='choice', message='Выберете действие',
                               choices=[''])]

