from random import choices

import inquirer


def user_menu():
    system('cls')
    questions = [inquirer.List(name='choice', message='Выберете действие',
                               choices=[''])]

