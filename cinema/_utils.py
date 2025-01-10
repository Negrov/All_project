from os import system


def local_move(action, calend, choose):
    system('cls')
    if action == 'left':
        calend.move('left')
    elif action == 'right':
        calend.move('right')
    elif action == 'up':
        calend.move('up')
    elif action == 'down':
        calend.move('down')
    calend.print(choose)


def format_num(num):
    return f'{num: >2}'


def create_choice(room, choice_row):
    result = [f'{str(i + 1): >3}) {room.get_seat()[choice_row][i]}' for i in range(room.len_sub(choice_row))]
    return result
