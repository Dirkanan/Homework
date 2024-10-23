import threading
import random
import time


class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        for k in range(100):
            amount = random.randint(50, 500)
            with self.lock:
                self.balance += amount
                print(f"Пополнение: {amount}. Баланс: {self.balance}")
                if self.balance >= 500:
                    print("Баланс достиг 500, разблокировка. Доступно расширение территории")

            time.sleep(0.001)

    def take(self):
        for i in range(100):
            amount = random.randint(50, 200)
            with self.lock:
                if self.balance >= amount:
                    self.balance -= amount
                    print(f"Снятие: {amount}. Баланс: {self.balance}")
                else:
                    print(f"Недостаточно средств для снятия: {amount}. Баланс: {self.balance}. Ты шушут нищий")

            time.sleep(0.001)


if __name__ == "__main__":
    bank = Bank()

    t1 = threading.Thread(target=bank.deposit)
    t2 = threading.Thread(target=bank.take)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print(f"Итоговый баланс: {bank.balance}")
