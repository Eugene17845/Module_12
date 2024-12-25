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
        runner = Runner('Mina')
        i = 0
        while i < 10:
            i += 1
            runner.walk()
        self.assertEqual(runner.distance,50)

    def test_run(self):
        runner = Runner('Steve')
        i = 0
        while i < 10:
            i += 1
            runner.run()
        self.assertEqual(runner.distance,100)

    def test_challenge(self):
        runner = Runner('Stewart')
        runner1 = Runner('Hugh')
        i = 0
        while i < 10:
            i += 1
            runner.run()
            runner1.walk()
        self.assertNotEqual(runner.distance,runner1.distance)