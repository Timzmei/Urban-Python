import unittest
from runner import Runner

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        runner = Runner("Test Runner")
        for _ in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50)

    def test_run(self):
        runner = Runner("Test Runner")
        for _ in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)

    def test_challenge(self):
        runner1 = Runner("Runner 1")
        runner2 = Runner("Runner 2")
        for _ in range(10):
            runner1.walk()
            runner2.run()
        self.assertNotEqual(runner1.distance, runner2.distance)

if __name__ == '__main__':
    unittest.main()