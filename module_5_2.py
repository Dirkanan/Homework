class House:
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

h1 = House('ЖК Олимпия', 16)
h2 = House('Страна Девелопмент', 20)
h3 = House('ЖК Седая мечта', 2)
#h1.go_to(-1)
#h2.go_to(17)
#h3.go_to(7)
print(h1)
print(h2)
print(h3)
print(len(h1))
print(len(h2))
print(len(h3))
