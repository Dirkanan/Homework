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



h1 = House('ЖК Олимпия', 16)
h2 = House('Страна Девелопмент', 20)
h3 = House('ЖК Седая мечта', 2)
h1.go_to(-1)
h2.go_to(17)
h3.go_to(7)
