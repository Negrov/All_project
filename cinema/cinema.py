import json


class Cinema:
    def __init__(self, name, rooms: list[str]):
        self.name = name
        self.rooms = [Room(i) for i in rooms]

    def get_rooms(self):
        return self.rooms

    def append(self, room):
        self.room.append(room)

    def wright_json(self):
        with open('db_cinema.json', 'w') as db:
            cinema_dict = {'name': self.name, 'rooms': self.rooms}
            json.dump(cinema_dict, db)

    def __str__(self):
        return f'{self.name}: {", ".join([room.name for room in self.rooms])}'


class Room:
    def __init__(self, name):
        self.name = name
        self.weight = 0
        self.height = 0
        self.seats = list()

    def generated_seat(self, weight, height):
        self.weight = weight
        self.height = height
        self.seats = [[' ' for _ in range(weight)] for _ in range(height)]

    def get_seat(self):
        return self.seats

    def refact_seat(self, weight, height):
        self.seats[weight][height] = '#'

    def __str__(self):
        return self.name
