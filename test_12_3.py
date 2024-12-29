import unittest
import suite_12_3
class RunnerTest(unittest.TestCase):
    is_frozen = False
    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        runner = suite_12_3.Runner('Mina')
        i = 0
        while i < 10:
            i += 1
            runner.walk()
        self.assertEqual(runner.distance,50)
    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        runner = suite_12_3.Runner('Steve')
        i = 0
        while i < 10:
            i += 1
            runner.run()
        self.assertEqual(runner.distance,100)
    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        runner = suite_12_3.Runner('Stewart')
        runner1 = suite_12_3.Runner('Hugh')
        i = 0
        while i < 10:
            i += 1
            runner.run()
            runner1.walk()
        self.assertNotEqual(runner.distance,runner1.distance)

class TournamentTest(unittest.TestCase):
    is_frozen = True
    @classmethod
    def setUpClass(cls):
        cls.all_results = []

    def setUp(self):
        self.runner0 = suite_12_3.Runner('Усейн', 10)
        self.runner1 = suite_12_3.Runner('Андрей', 9)
        self.runner2 = suite_12_3.Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for n, r in  enumerate(cls.all_results):
            print(r)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        test = suite_12_3.Tournament(90,self.runner0, self.runner2)
        test_start = {n: str(r) for n, r in test.start().items()}
        TournamentTest.all_results.append(test_start)
        self.assertTrue(test_start[2], 'Ник')
    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run_1(self):
        test = suite_12_3.Tournament(90,self.runner1, self.runner2)
        test_start = {n: str(r) for n, r in test.start().items()}
        TournamentTest.all_results.append(test_start)
        self.assertTrue(test_start[2], 'Ник')
    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_ru2(self):
        test = suite_12_3.Tournament(90,self.runner0, self.runner1, self.runner2)
        test_start = {n: str(r) for n, r in test.start().items()}
        TournamentTest.all_results.append(test_start)
        self.assertTrue(test_start[3], 'Ник')

testST = unittest.TestSuite()

testST.addTest(unittest.TestLoader().loadTestsFromTestCase(RunnerTest))
testST.addTest(unittest.TestLoader().loadTestsFromTestCase(TournamentTest))
test_runner = unittest.TextTestRunner(verbosity=2)
test_runner.run(testST)
