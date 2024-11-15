import unittest


class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        runner_1 = Runner("Тестовый Бегун 1 ")
        for i in range(11):
            runner_1.walk()

        self.assertEqual(runner_1.distance, 55)

    def test_run(self):
        runner_2 = Runner("Тестовый Бегун 2 ")
        for i in range(100):
            runner_2.run()

        self.assertEqual(runner_2.distance, 1000)

    def test_challenge(self):
        runner_3 = Runner("Тестовый Бегун 3 ")
        runner_4 = Runner("Тестовый Бегун 4 ")
        for i in range(30):
            runner_3.walk()

        for i in range(10):
            runner_4.run()

        self.assertNotEqual(runner_3.distance, runner_4.distance)


if __name__ == '__main__':
    unittest.main()
