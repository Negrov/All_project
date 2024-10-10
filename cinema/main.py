import inquirer
from os import system
from user_menu import user_menu
from root_menu import root_menu


while True:
    system('cls')
    questions = [
        inquirer.List('choice',
                      message="Выберете пользователя:",
                      choices=['Покупатель', 'Администатор', 'Выход'])
    ]

    choice = inquirer.prompt(questions)["choice"]

    if choice == 'Покупатель':
        user_menu()
        # print("user_nemu")
    elif choice == 'Администатор':
        root_menu()
        # print('Root')
    if choice == 'Выход':
        print("Выход из программы.")
        break


