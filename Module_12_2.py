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
        cls.all_results = []

    def setUp(self):
        self.runner0 = Runner('Усейн', 10)
        self.runner1 = Runner('Андрей', 9)
        self.runner2 = Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for n, r in  enumerate(cls.all_results):
            print(r)

    def test_run(self):
        test = Tournament(90,self.runner0, self.runner2)
        test_start = {n: str(r) for n, r in test.start().items()}
        TournamentTest.all_results.append(test_start)
        self.assertTrue(test_start[2], 'Ник')

    def test_run_1(self):
        test = Tournament(90,self.runner1, self.runner2)
        test_start = {n: str(r) for n, r in test.start().items()}
        TournamentTest.all_results.append(test_start)
        self.assertTrue(test_start[2], 'Ник')

    def test_ru2(self):
        test = Tournament(90,self.runner0, self.runner1, self.runner2)
        test_start = {n: str(r) for n, r in test.start().items()}
        TournamentTest.all_results.append(test_start)
        self.assertTrue(test_start[3], 'Ник')