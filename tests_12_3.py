import unittest


class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers


class TournamentTest(unittest.TestCase):
    is_frozen = True

    def skip_if_frozen(test_func):
        def wrapper(self, *args, **kwargs):
            if self.is_frozen:
                print(f"Тест {test_func.__name__} пропущен: Тесты в этом кейсе заморожены")
                self.skipTest('Тесты в этом кейсе заморожены')
            return test_func(self, *args, **kwargs)

        return wrapper

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    @skip_if_frozen
    def setUp(self):
        self.runner_usain = Runner("Усейн", speed=10)
        self.runner_andrey = Runner("Андрей", speed=9)
        self.runner_nik = Runner("Ник", speed=3)

    @skip_if_frozen
    def test_run1(self):
        run_1 = Tournament(90, self.runner_usain, self.runner_nik)
        result = run_1.start()
        self.assertTrue(result[list(result.keys())[-1]] == 'Ник')
        self.all_results['Результат первого забега'] = result

    @skip_if_frozen
    def test_run2(self):
        run_2 = Tournament(90, self.runner_andrey, self.runner_nik)
        result = run_2.start()
        self.assertTrue(result[list(result.keys())[-1]] == 'Ник')
        self.all_results['Результат второго забега'] = result

    @skip_if_frozen
    def test_run3(self):
        run_3 = Tournament(90, self.runner_usain, self.runner_andrey, self.runner_nik)
        result = run_3.start()
        self.assertTrue(result[list(result.keys())[-1]] == 'Ник')
        self.all_results['Результат тертьего забега'] = result

    @classmethod
    def tearDownClass(cls):
        for key_test, value_test in cls.all_results.items():
            print(f'Проведенный тест: {key_test}')
            for key, value in value_test.items():
                print(f'{key}: {value.name}')


class RunnerTest(unittest.TestCase):
    is_frozen = False

    def skip_if_frozen(test_func):
        def wrapper(self, *args, **kwargs):
            if self.is_frozen:
                print(f"Тест {test_func.__name__} пропущен: Тесты в этом кейсе заморожены")
                self.skipTest('Тесты в этом кейсе заморожены')
            return test_func(self, *args, **kwargs)

        return wrapper

    @skip_if_frozen
    def test_walk(self):
        runner_1 = Runner("Тестовый Бегун 1 ")
        for i in range(11):
            runner_1.walk()

        self.assertEqual(runner_1.distance, 55)

    @skip_if_frozen
    def test_run(self):
        runner_2 = Runner("Тестовый Бегун 2 ")
        for i in range(100):
            runner_2.run()

        self.assertEqual(runner_2.distance, 1000)

    @skip_if_frozen
    def test_challenge(self):
        runner_3 = Runner("Тестовый Бегун 3 ")
        runner_4 = Runner("Тестовый Бегун 4 ")
        for i in range(30):
            runner_3.walk()

        for i in range(10):
            runner_4.run()

        self.assertNotEqual(runner_3.distance, runner_4.distance)


if __name__ == "__main__":
    unittest.main()
