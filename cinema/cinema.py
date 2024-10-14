import json


class Cinema:
    def __init__(self, name, rooms: list[str]):
        self.name = name
        self.rooms = [Room(i) for i in rooms]

    def get_rooms(self):
        return self.rooms

    def append(self, room):
        self.room.append(room)

    @property
    def _to_dict_room(self):
        result = list()
        for room in self.rooms:
            result.append(room.to_dict_())
        return result

    def wright_json(self):
        # with open('cinema\\db_cinema.json', 'w') as db:
        with open('C:\\Users\\Negrov\\PycharmProjects\\pythonProject3\\cinema\\db_cinema.json', 'w') as db:
            cinema_dict = {'name': self.name, 'rooms': self._to_dict_room}
            json.dump(cinema_dict, db)

    def __str__(self):
        return f'{self.name}: {", ".join([room.name for room in self.rooms])}'


class Room:
    def __init__(self, name):
        self.name = name
        self.weight = 0
        self.height = 0
        self.seats = list()

    def __len__(self):
        return len(self.seats)

    def to_dict_(self):
        return {'name': self.name, 'weight': self.weight, 'height': self.height, 'seats': self.seats}

    def len_sub(self, row):
        return len(self.seats[row])

    def generated_seat(self, weight, height):
        self.weight = weight
        self.height = height
        self.seats = [['__' for _ in range(weight)] for _ in range(height)]

    def get_seat(self):
        return self.seats

    def refact_seat(self, weight, height):
        self.seats[weight][height] = '()' if self.seats[weight][height] == '__' else '__'

    def __str__(self):
        return self.name
