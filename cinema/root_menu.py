import json

import inquirer
from os import system

from pyexpat.errors import messages

from cinema import Cinema, Room, to_json
from cinema.main import questions


def choose_cinema(cinemas):
    system('cls')
    questions1 = [inquirer.List(name='choice', message='Выберете кинотеатр',
                                choices=[f'{i + 1}){cin.name}' for i, cin in enumerate(cinemas)] + ['Выход'])]
    choice = inquirer.prompt(questions1)['choice']

    if choice == 'Выход':
        return

    choice = int(choice[:choice.find(')')]) - 1
    cinema = cinemas[choice]
    return cinema


def format_num(num):
    return f'{num: >2}'


def create_choice(room, choice_row):
    result = [f'{str(i + 1): >3}) {room.get_seat()[choice_row][i]}' for i in range(room.len_sub(choice_row))]
    return result


def fill_room(room: Room):
    while True:
        system('cls')
        print(f'Заполните имеющиеся места в зале {room.name}:')
        questions_big = [
            inquirer.List(
                name='seats', message=f'{" " * 4}{" ".join([format_num(i) for i in range(1, room.weight + 1)])}',
                choices=([f'{str(len(room) - i): >3}) {" ".join(room.get_seat()[i])}' for i in range(len(room))]
                         + ['Выход'])

            )
        ]
        choice = inquirer.prompt(questions_big)['seats']
        if choice == 'Выход':
            return
        row = int(choice[:choice.find(')')])
        choice_row = len(room) - row

        # _______________места__________________
        room = room
        choice_row = choice_row
        system('cls')
        print(row, 'ряд')
        questions_small = [
            inquirer.Checkbox(
                'place', message='Выберете место',
                choices=create_choice(room, choice_row)
            )
        ]
        choice = inquirer.prompt(questions_small)['place']
        for check in choice:
            col = int(check[:check.find(')')])
            choice_col = col - 1
            room.refact_seat(choice_row, choice_col)


def join_cinema():
    system('cls')
    name = input('Название кинотеатра:\n')
    rooms = input('Нипишите залы (формат ввода: Название1, Название2, Название3 и т.д\n')
    while (rooms.find(', ') == -1 or len(rooms) == 0) and not rooms.isdigit():
        system('cls')
        print('Неверный ввод залов.')
        rooms = input('Нипишите залы (формат ввода: Название1, Название2, Название3 и т.д\n')
    rooms = [Room(i) for i in sorted(set(rooms.strip().split(', ')))]
    cinema = Cinema(name, rooms)
    for room in cinema.get_rooms():
        system('cls')
        print(room, 'зал')
        weight, _, height = input('Ввидите размеры прямоугольника в котором расположены кресла\n'
                                  '(в формате: кресла по горизонтали X кресла по вертикали)\n').lower().split(' ')
        room.generated_seat(int(weight), int(height))

        fill_room(room)

    cinema.wright_json()


def refact_cinema():
    cinemas = to_json()

    while True:
        system('cls')
        questions1 = [inquirer.List(name='choice', message='Выберете кинотеатр',
                                   choices=[f'{i + 1}){cin.name}' for i, cin in enumerate(cinemas)] + ['Выход'])]
        choice = inquirer.prompt(questions1)['choice']

        if choice == 'Выход':
            break

        choice = int(choice[:choice.find(')')]) - 1
        cinema = cinemas[choice]
        while True:
            cinema = cinema
            system('cls')
            questions_refact = [inquirer.List(name='choice', message=f'Отредактируйте кинотеатр: {cinema.name}',
                                              choices=['Название', 'Залы', 'Выход'])]
            choice = inquirer.prompt(questions_refact)['choice']

            if choice == 'Выход':
                break

            elif choice == 'Название':
                system('cls')
                name = input('Введите новое название или enter для отмены\n')
                cinema.name = name if name else cinema.name

            else:
                while True:
                    cinema = cinema
                    system('cls')
                    questions_rooms = [inquirer.List(name='choice', message='Выберете зал',
                                                     choices=[f'{i + 1}.' for i in range(len(cinema))] + ['Выход'])]
                    choice = inquirer.prompt(questions_rooms)['choice']

                    if choice == 'Выход':
                        break

                    room = cinema.get_rooms()[int(choice[:choice.find('.')]) - 1]
                    fill_room(room)

        cinema.wright_json()


def join_seance():
    cinema = choose_cinema(to_json())
    cinemas = to_json()
    while True:
        system('cls')
        cinema_check = [inquirer.List(name='choice', message='Выберете кинотеатр',
                                choices=[f'{i + 1}){cin.name}' for i, cin in enumerate(cinemas)] + ['Выход'])]
        choice = inquirer.prompt(cinema_check)['choice']

        if choice == 'Выход':
            break

        choice = int(choice[:choice.find(')')]) - 1
        cinema = cinemas[choice]






def remove_seance():
    pass


def root_menu():
    while True:
        system('cls')
        question = [
            inquirer.List('choice',
                          message='Выберете действие',
                          choices=['Добавить кинотеатр', 'Редактор кинотеатра', 'Добавить сеанс', 'Удалить сеанс',
                                   'Назад'])
        ]
        answers = inquirer.prompt(question)['choice']
        if answers == 'Добавить кинотеатр':
            join_cinema()
        elif answers == 'Редактор кинотеатра':
            refact_cinema()
        elif answers == 'Добавить сеанс':
            join_seance()
        elif answers == 'Удалить сеанс':
            remove_seance()
        elif answers == 'Назад':
            return
