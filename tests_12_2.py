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
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner_usain = Runner("Усейн", speed=10)
        self.runner_andrey = Runner("Андрей", speed=9)
        self.runner_nik = Runner("Ник", speed=3)

    def test_run1(self):
        run_1 = Tournament(90, self.runner_usain, self.runner_nik)
        result = run_1.start()
        self.assertTrue(result[list(result.keys())[-1]] == 'Ник')
        self.all_results['Результат первого забега'] = result

    def test_run2(self):
        run_2 = Tournament(90, self.runner_andrey, self.runner_nik)
        result = run_2.start()
        self.assertTrue(result[list(result.keys())[-1]] == 'Ник')
        self.all_results['Результат второго забега'] = result

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


if __name__ == "__main__":
    unittest.main()
