import inquirer
import datetime

from os import system
from termcolor import colored

from cinema import Cinema, Room
from move_calendar import MoveCalendar
from utils import fill_room, choose_cinema, choose_room, step_key, from_json


def join_cinema():
    system('cls')
    name = input('[' + colored('?', 'yellow') + '] ' + 'Название кинотеатра:\n').strip()
    if not name:
        return
    _rooms = input(
        '[' + colored('?', 'yellow') + '] ' + 'Нипишите залы (формат ввода: Название1, Название2, Название3 и т.д\n')
    rooms = [Room(i) for i in sorted(set(_rooms.strip().split(', ')))] if ', ' in _rooms else [_rooms.strip()]
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
    is_del = False
    while True:
        cinema = choose_cinema()

        if cinema == 'Выход':
            break

        while True:
            cinema = cinema
            system('cls')
            questions_refact = [inquirer.List(name='choice', message=f'Отредактируйте кинотеатр: {cinema.name}',
                                              choices=['Название', 'Залы', 'Удалить', 'Выход'])]
            choice = inquirer.prompt(questions_refact)['choice']

            if choice == 'Выход':
                break

            elif choice == 'Название':
                system('cls')
                name = input('[' + colored('?', 'yellow') + '] ' + 'Введите новое название или enter для отмены:\n')
                cinema.name = name.strip() if name else cinema.name

            elif choice == 'Удалить':
                is_del = True
                cinema.del_in_json()
                break

            elif choice == 'Залы':
                while True:
                    cinema = cinema
                    room = choose_room(cinema)

                    if room == 'Выход':
                        break

                    while True:
                        system('cls')

                        questions_set_room = [
                            inquirer.List(name='choice', message=f'Отредактируйте кинотеатр: {room.name}',
                                          choices=['Название', 'Места', 'Удалить', 'Выход'])]
                        mini_choice = inquirer.prompt(questions_set_room)['choice']

                        if mini_choice == 'Выход':
                            break
                        elif mini_choice == 'Места':
                            fill_room(room)
                        elif mini_choice == 'Название':
                            system('cls')
                            name = input(
                                '[' + colored('?', 'yellow') + '] ' + 'Введите новое название или enter для отмены:\n')
                            room.name = name.strip() if name else room.name
                        elif mini_choice == 'Удалить':
                            cinema.rooms.remove(room)

        if not is_del:
            cinema.wright_json()


def join_seance():
    while True:
        cinema = choose_cinema()

        if cinema == 'Выход':
            break

        while True:

            room = choose_room(cinema)

            if room == 'Выход':
                break

            calendar = MoveCalendar()
            date, count_enter = step_key(calendar)
            [input() for _ in range(count_enter)]

            for date_i in date:
                while True:
                    system('cls')
                    print('[' + colored('?', 'yellow') + '] День фильма: ' + str(date_i))

                    name_scene = input(
                        '[' + colored('?', 'yellow') + '] Введите название ' + colored('премьеры',
                                                                                       'green') + '(или enter для пропуска сеанса): \n\t').strip()
                    if not name_scene:
                        break

                    begin_time = input('[' + colored('?',
                                                     'yellow') + '] Введите начало время фильма в формате xx:xx(при необходимости и микросек.): \n\t').strip()
                    end_time = input('[' + colored('?',
                                                   'yellow') + '] Введите конца время фильма в формате xx:xx(при необходимости и микросек.): \n\t').strip()

                    try:
                        if datetime.time(*[int(i) for i in begin_time.split(':')]) >= datetime.time(
                                *[int(i) for i in end_time.split(':')]):
                            raise ValueError
                    except ValueError:
                        input('[' + colored('!', 'red') + '] ' + 'Неверное время, enter для продолжения.')
                        continue

                    room.add_seance(date_i, f'{begin_time}-{end_time}', name_scene)
                    input('[' + colored('.', 'green') + '] ' + 'Успешно добавлено, enter для продолжения.')
                    break
        cinema.wright_json()


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
