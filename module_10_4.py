import threading
import random
import time
import queue


class Table:
    def __init__(self, number):
        self.number = number
        self.guest = None


class Guest(threading.Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        time.sleep(random.randint(3, 10))


class Cafe:
    def __init__(self, *tables):
        self.tables = list(tables)
        self.queue = queue.Queue()

    def guest_arrival(self, *guests):
        for guest_name in guests:
            guest = Guest(guest_name)
            self.queue.put(guest)
            print(f"{guest_name} в очереди")
            guest.start()

    def discuss_guests(self):
        while not self.queue.empty() or any(table.guest is not None for table in self.tables):
            for table in self.tables:
                if table.guest is not None and not table.guest.is_alive():
                    print(f"{table.guest.name} покушал(-а) и ушёл(ушла)")
                    print(f"Стол номер {table.number} свободен")
                    table.guest = None

                if table.guest is None and not self.queue.empty():
                    guest = self.queue.get()
                    table.guest = guest
                    print(f"{guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}")


if __name__ == "__main__":
    tables = [Table(i) for i in range(1, 6)]
    cafe = Cafe(*tables)
    guests = ['Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
              'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra']
    cafe.guest_arrival(*guests)
    cafe.discuss_guests()

print('STOP')
