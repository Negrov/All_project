import inquirer
from os import system
from cinema import Cinema, Room


def join_cinema():
        system('cls')
        name = input('Название кинотеатра:\n')
        rooms = input('Нипишите залы (формат ввода: Название1, Название2, Название3 и т.д\n')
        while rooms.find(', ') == -1:
            print('Неверный ввод залов.')
            rooms = input('Нипишите залы (формат ввода: Название1, Название2, Название3 и т.д\n')
        rooms = sorted(set(rooms.strip().split(', ')))
        for room in rooms:
            if not("зал" in room):
                room += ' зал'
        cinema = Cinema(name, rooms)
        for room in cinema.get_rooms():
            system('cls')
            print(room)
            weight, height = input('Ввидите размеры прямоугольника в котором расположены кресла\n'
                                   '(в формате: кресла по горизонтали X кресла по вертикали)\n').lower().split(' x ')
            room.generated_seat(int(weight), int(height))
            print(*room.get_seat(), sep='\n')
            input('Продолить')
        cinema.wright_json()



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
