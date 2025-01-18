from os import system
from pynput import keyboard
from time import sleep

import json
import inquirer

from _utils import format_num, local_move, create_choice
from cinema import Seance, Room, Cinema


def fill_room(room: Room):
    """Редактор сидений комнаты"""
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


def choose_cinema():
    """Выбор кинотеатра"""
    system('cls')
    cinemas = from_json()
    system('cls')
    cinema_check = [inquirer.List(name='choice', message='Выберете кинотеатр',
                                  choices=[f'{i + 1}){cin.name}' for i, cin in enumerate(cinemas)] + ['Выход'])]
    choice = inquirer.prompt(cinema_check)['choice']

    if choice == 'Выход':
        return 'Выход'

    choice = int(choice[:choice.find(')')]) - 1
    cinema = cinemas[choice]

    return cinema


def choose_room(cinema: Cinema):
    """Выбор комнаты"""
    system('cls')
    questions_rooms = [inquirer.List(name='choice', message='Выберете зал',
                                     choices=[f'{i + 1}.' for i in range(len(cinema))] + ['Выход'])]
    choice = inquirer.prompt(questions_rooms)['choice']

    if choice == 'Выход':
        return 'Выход'

    room = cinema.get_rooms()[int(choice[:choice.find('.')]) - 1]
    return room


def step_key(calendar):
    """Перемещение по календарю через pynput"""
    system('cls')
    choose = list()
    calendar.print(choose)
    is_enter = False
    is_exit = False
    count_enter = 0
    with keyboard.Events() as events:
        for event in events:
            if type(event) == keyboard.Events.Press:
                if event.key == keyboard.Key.up:
                    local_move('up', calendar, choose)
                elif event.key == keyboard.Key.down:
                    local_move('down', calendar, choose)
                elif event.key == keyboard.Key.left:
                    local_move('left', calendar, choose)
                elif event.key == keyboard.Key.right:
                    local_move('right', calendar, choose)

                elif event.key == keyboard.KeyCode.from_char('w'):
                    local_move('up', calendar, choose)
                elif event.key == keyboard.KeyCode.from_char('s'):
                    local_move('down', calendar, choose)
                elif event.key == keyboard.KeyCode.from_char('a'):
                    local_move('left', calendar, choose)
                elif event.key == keyboard.KeyCode.from_char('d'):
                    local_move('right', calendar, choose)

                elif event.key == keyboard.Key.enter:
                    is_enter = True
                elif event.key == keyboard.Key.esc:
                    is_exit = True

            if type(event) == keyboard.Events.Release:
                if is_enter and event.key == keyboard.Key.enter:
                    choose_date = calendar.date
                    if choose_date in choose:
                        choose.remove(choose_date)
                    else:
                        choose.append(choose_date)
                    choose.sort()
                    local_move('', calendar, choose)
                    is_enter = False
                    count_enter += 1

                elif is_exit and event.key == keyboard.Key.esc:
                    return choose, count_enter


def from_json():
    # with open('cinema/cinema.json', 'r') as infile:
    with open('C:\\Users\\Negrov\\PycharmProjects\\All_project\\cinema\\db_cinema.json', 'r') as infile:
        db_data = json.load(infile)
    data = db_data['db']

    cinemas = list()
    for cinema in data:
        rooms = cinema['rooms']
        for i, room in enumerate(rooms):
            seances: list = room['seance']
            for j, seance in enumerate(seances):
                seances[j] = Seance(seance[j]['name_seance'], seance[j]['places'])

            rooms[i] = Room(room['name'], room['seats'])
            rooms[i].seance = seances

        cinemas.append(Cinema(cinema['name'], rooms, cinema['name']))
    return cinemas
