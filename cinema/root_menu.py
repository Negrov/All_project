import inquirer

from os import system
from termcolor import colored

from cinema import Cinema, Room
from cinema.utils import from_json
from move_calendar import MoveCalendar
from utils import fill_room, choose_cinema, choose_room, step_key


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
    while True:
        cinema = choose_cinema()

        if cinema == 'Выход':
            break

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
                name = input('[' + colored('?', 'yellow') + '] ' + 'Введите новое название или enter для отмены\n')
                cinema.name = name.strip() if name else cinema.name

            elif choice == 'Залы':
                while True:
                    cinema = cinema
                    room = choose_room(cinema)

                    if room == 'Выход':
                        break

                    fill_room(room)

        cinema.wright_json()


def join_seance():
    while True:
        cinema = choose_cinema()

        if cinema == 'Выход':
            break

        calendar = MoveCalendar()
        date, count_enter = step_key(calendar)
        [input() for _ in range(count_enter)]

        for sceance in date:
            system('cls')
            print('[' + colored('?', 'yellow') + '] День фильма: ' + str(sceance))
            name_scene = input('[' + colored('?', 'yellow') + '] Введите название ' + colored('премьеры', 'green') + ': \n\t').strip()
            begin_time = input('[' + colored('?', 'yellow') + '] Введите начало время фильма в формате xx:xx(при необходимости и микросек.): \n\t').strip()
            end_time = input('[' + colored('?', 'yellow') + '] Введите конца время фильма в формате xx:xx(при необходимости и микросек.): \n\t').strip()




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
