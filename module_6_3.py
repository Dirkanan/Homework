class Horse:
    def __init__(self, x_distance = 0, sound= 'MAN' ):
        #я тоже отсылочки знаю, не хабиб конечно, но тоже не плохо xDDDD
        self.sound = sound
        self.x_distance = x_distance

    def run (self, dx):
        self.x_distance += dx

class Eagle:
    def __init__(self, y_distance = 0, sound = 'I train, eat, sleep, and repeat'):
        self.y_distance = y_distance
        self.sound = sound

    def fly(self, dy):
        self.y_distance += dy

class Pegas (Horse, Eagle):

    def __init__(self):
        Horse.__init__(self)
        Eagle.__init__(self)


    def move(self, dx, dy):
        super().run(dx)
        super().fly(dy)
        return self.x_distance, self.y_distance

    def get_pos(self):
        return f'({self.x_distance}, {self.y_distance})'

    def voice (self):
        print(self.sound)

p1 = Pegas()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()
