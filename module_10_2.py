from threading import Thread
import time


class Knight(Thread):

    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power
        self.enemies = 100  # Начальное количество врагов
        self.days_batlle = 0

    def run(self):
        print(f"{self.name}, на нас напали!")
        while self.enemies > 0:
            time.sleep(1)
            self.days_batlle += 1
            self.enemies -= self.power
            print(f"{self.name} сражается {self.days_batlle}, осталось {self.enemies} воинов.")
        print(f"{self.name} одержал победу спустя {self.days_batlle} дней(дня)!")


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()
print('Спустя долгие дни и ночи битв рыцари решили закончить с насилием и проповедовать буддизм')
