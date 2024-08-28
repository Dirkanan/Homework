class House:
    houses_history = []

    def __new__(cls, *args, **kwargs):
        cls.houses_history.append(args[0])
        return super().__new__(cls)

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
        self.new_floor = None

    def go_to (self, new_floor):
        self.new_floor = new_floor
        if self.new_floor > self.number_of_floors or self.new_floor < 1:
            print(f'Такого этажа не существует в этом доме {self.name}')
        else:
            for i in range(1, self.new_floor + 1):
                print(i)

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название: {self.name}, {self.number_of_floors} этажей'

    def __eq__(self, other):
        return self.number_of_floors == other.number_of_floors

    def __lt__(self, other):
        return self.number_of_floors < other.number_of_floors

    def __le__(self, other):
        return self.number_of_floors <= other.number_of_floors

    def __gt__(self, other):
        return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):
        return self.number_of_floors >= other.number_of_floors

    def __ne__(self, other):
        return self.number_of_floors != other.number_of_floors

    def __add__(self, value):
        self.number_of_floors += value
        return  self

    def __radd__(self, value):
        self.number_of_floors += value
        return self

    def __iadd__(self, value):
        self.number_of_floors += value
        return self

    def __del__(self):
        print(f'{self.name} заселили бомжи и его наконец снесли, но мы его занесли в хронику градостроителей Лордерона')

h1 = House('Пьяный гном', 2)
print(House.houses_history)
h2 = House('Умный орк', 4)
print(House.houses_history)
h3 = House('Пиво-Интерпрайзис', 100)
print(House.houses_history)


del h2
del h3

print(House.houses_history)
