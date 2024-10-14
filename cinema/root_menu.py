import inquirer
from os import system
from cinema import Cinema, Room


def format_num(num):
    return f'{num: >2}'

def create_choice(room, choice_row):
    result = [f'{str(i + 1): >3}) {room.get_seat()[choice_row][i]}' for i in range(room.len_sub(choice_row))]
    return result

def join_cinema():
        system('cls')
        name = input('Название кинотеатра:\n')
        rooms = input('Нипишите залы (формат ввода: Название1, Название2, Название3 и т.д\n')
        while (rooms.find(', ') == -1 or  len(rooms) == 0) and not rooms.isdigit():
            system('cls')
            print('Неверный ввод залов.')
            rooms = input('Нипишите залы (формат ввода: Название1, Название2, Название3 и т.д\n')
        rooms = sorted(set(rooms.strip().split(', ')))
        cinema = Cinema(name, rooms)
        for room in cinema.get_rooms():
            system('cls')
            print(room, 'зал')
            weight, height = input('Ввидите размеры прямоугольника в котором расположены кресла\n'
                                   '(в формате: кресла по горизонтали X кресла по вертикали)\n').lower().split(' x ')
            room.generated_seat(int(weight), int(height))

            while True:
                weight = int(weight)
                system('cls')
                room = room
                print(f'Заполните имеющиеся места в зале {str(room)}:')
                questions_big = [
                    inquirer.List(
                        name='seats', message=f'{" " * 4}{" ".join([format_num(i) for i in range(1, weight + 1)])}',
                        choices=([f'{str(len(room) - i): >3}) {" ".join(room.get_seat()[i])}' for i in range(len(room))]
                                + ['Выход'])

                    )
                ]
                choice = inquirer.prompt(questions_big)['seats']
                if choice == 'Выход':
                    break
                row = int(choice[:choice.find(')')])
                choice_row = len(room) - row

                #_______________места__________________
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

        cinema.wright_json()

def refact_cimina():
    pass


def root_menu():
    while True:
        system('cls')
        questions = [
            inquirer.List('choice',
                          message='Выберете действие',
                          choices=['Добавить кинотеатр', 'Редактор кинотеатра', 'Назад'])
        ]
        answers = inquirer.prompt(questions)['choice']
        if answers == 'Добавить кинотеатр':
            join_cinema()
        elif answers == 'Редактор кинотеатра':
            refact_cimina()
        elif answers == 'Назад':
            return
