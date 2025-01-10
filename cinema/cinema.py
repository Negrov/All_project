import json
import datetime


# def refact(data, val, dic):
#     data[val] = dic


class Room:
    def __init__(self, name, _seats=None):
        self.name = name
        self._seats = _seats if _seats else list()
        self.weight = len(self._seats[0]) if _seats else 0
        self.height = len(self._seats) if _seats else 0

        self.seance = dict()

    def add_seance(self, date, time_seance, seance):
        """time_sceance  —  нач-кон (нач — hour:min)"""
        month = date.month
        day = date.day

        if not self.valid(month, day, time_seance):
            return False

        if month in self.seance:
            if day in self.seance[mounth]:
                self.seance[mounth][day].update({time_seance: Seance(seance, self._seats.copy())})
            else:
                self.seance[mounth].update({day: {time_seance: Seance(seance, self._seats.copy())}})
        else:
            self.seance[month] = {day: {time_seance: Seance(seance, self._seats.copy())}}
        return True

    def __len__(self):
        return len(self._seats)

    def to_dict_(self):
        return {'name': self.name, 'seats': self._seats, 'seance': self.seance}

    def len_sub(self, row):
        return len(self._seats[row])

    def generated_seat(self, weight, height):
        self.weight = weight
        self.height = height
        self._seats = [['__' for _ in range(weight)] for _ in range(height)]

    def get_seat(self):
        return self._seats

    def refact_seat(self, weight, height):
        self._seats[weight][height] = '()' if self._seats[weight][height] == '__' else '__'

    def __str__(self):
        return self.name

    def valid(self, month, day, time_active):
        if month not in self.seance or day not in self.seance[month]:
            return True

        try:
            review_time = [datetime.time(*[int(j) for j in i.split(':')]) for i in time_active.split('-')]
            time_list = [[datetime.time(*[int(j) for j in i.split(':')]) for i in k.split('-')] for k in
                         self.seance[month][day].keys()]
        except ValueError:
            return False

        for i in time_list:
            if i[0] <= review_time[0] <= i[1] or i[0] <= review_time[1] <= i[1] \
                    or any([review_time[0] <= j <= review_time[1] for j in i]):
                return False
        return True


class Cinema:
    def __init__(self, name, rooms: list[Room, ...], _name=None):
        self.name = name
        self.rooms = rooms
        self._name = _name

    def get_rooms(self):
        return self.rooms

    def __len__(self):
        return len(self.rooms)

    def append(self, room):
        self.room.append(room)

    @property
    def _to_dict_room(self):
        result = list()
        for room in self.rooms:
            result.append(room.to_dict_())
        return result

    def wright_json(self):
        # with open('cinema.json', 'r') as db:
        with open('C:\\Users\\Negrov\\PycharmProjects\\pythonProject3\\cinema\\db_cinema.json', 'r') as db:
            db_data: dict = json.load(db)

        flag = False
        for i, data in enumerate(db_data['db']):
            if data['name'] in (self.name, self._name):
                flag = True
                db_data['db'][i] = {'name': self.name, 'rooms': self._to_dict_room}

        # with open('cinema\\db_cinema.json', 'w') as db:
        with open('C:\\Users\\Negrov\\PycharmProjects\\pythonProject3\\cinema\\db_cinema.json', 'w') as db:
            db_data if flag else db_data['db'].append({'name': self.name, 'rooms': self._to_dict_room})
            json.dump(db_data, db)

    def __str__(self):
        return f'{self.name}: {", ".join([room.name for room in self.rooms])}'


class Seance:
    def __init__(self, seance, places):
        self.name_seance = seance
        self.places = places

    def __dict__(self):
        return {'name_seance': self.name_seance, 'places': self.places}
