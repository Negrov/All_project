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
    elif choice == 'Администатор':
        root_menu()
    if choice == 'Выход':
        print("Выход из программы.")
        break


