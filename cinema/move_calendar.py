import calendar, datetime

from termcolor import colored


class MoveCalendar:
    def __init__(self):
        self.map_cal = None
        self.header = ''
        self.board: list[list] = list()
        self.date = datetime.date.today()
        self.fill_map()
        self.x, self.y = 0, 0
        self._generate_x_y()
        self._print()

    def move(self, key):
        if key == 'left':
            self._step(-1)
        elif key == 'right':
            self._step(1)
        elif key == 'up':
            self._step(-7)
        elif key == 'down':
            self._step(7)
        elif key == 'enter':
            return self.date

    def _step(self, direction):
        self._clear()
        self.date += datetime.timedelta(days=direction)
        self.fill_map()
        self._generate_x_y()
        self._print()

    def fill_map(self):
        calend = calendar.TextCalendar().formatmonth(self.date.year, self.date.month).split('\n')
        self.header = f" {calend[0].strip():<29}↑ ↓ "
        self.board = [i.strip().split() for i in calend[1:-1]]
        day = ' '.join([f' {i:>2} ' for i in self.board[0]])
        self.board = self.board[1:]
        self.header += '\n' + day

        self.board[0] = [" "] * (7 - len(self.board[0])) + self.board[0]
        self.board[-1] = self.board[-1] + [" "] * (7 - len(self.board[-1]))

        self.board = [[f' {j:>2} ' for j in i] for i in self.board]

    def __str__(self):
        return self.header + '\n' + '\n'.join([' '.join(i) for i in self.board])

    def _clear(self):
        self.board[self.y][self.x] = f' {self.board[self.y][self.x][1:-1]} '

    def _print(self):
        self.board[self.y][self.x] = f'[{self.board[self.y][self.x][1:-1]}]'

    def _generate_x_y(self):
        self.x, self.y = \
            [[(i.index(j), self.board.index(i)) for j in i if j == f' {self.date.day:>2} '] for i in self.board if
             f' {self.date.day:>2} ' in i][0][0]

    def print(self, choose):
        board = '\n'.join([' '.join(i) for i in self.board])
        left_lim = board.index('[')
        right_lim = board.index(']')
        print(colored(self.header[:29], 'yellow') + self.header[29:] + '\n' + board[:left_lim] + colored(
            board[left_lim:right_lim + 1], 'red') + board[right_lim + 1:], *choose, sep='\n')
