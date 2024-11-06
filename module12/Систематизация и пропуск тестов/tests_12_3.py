import unittest

from runner_and_tournament import Runner, Tournament

class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        runner = Runner(name="Test Runner", speed=5)
        runner.run()
        self.assertEqual(runner.distance, 10)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        runner = Runner(name="Test Runner", speed=5)
        runner.walk()
        self.assertEqual(runner.distance, 5)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        runner1 = Runner(name="Усэйн", speed=10)
        runner2 = Runner(name="Болт", speed=8)
        self.assertNotEqual(runner1, runner2)

class TournamentTest(unittest.TestCase):
    is_frozen = True

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_first_tournament(self):
        tournament = Tournament(100, Runner("Усэйн", 10), Runner("Ник", 5))
        results = tournament.start()
        self.assertEqual(results[1].name, "Усэйн")

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_second_tournament(self):
        tournament = Tournament(100, Runner("Андрей", 9), Runner("Ник", 5))
        results = tournament.start()
        self.assertEqual(results[1].name, "Андрей")

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_third_tournament(self):
        tournament = Tournament(100, Runner("Усэйн", 10), Runner("Андрей", 9), Runner("Ник", 5))
        results = tournament.start()
        self.assertEqual(results[3].name, "Ник")

if __name__ == "__main__":
    unittest.main()
