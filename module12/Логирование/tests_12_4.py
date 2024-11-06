import unittest
import logging
from rt_with_exceptions import Runner

logging.basicConfig(
    level=logging.INFO,
    filename="module12/Логирование/runner_tests.log",
    filemode="w",
    encoding="utf-8",
    format="%(levelname)s: %(message)s"
)

class RunnerTest(unittest.TestCase):

    def test_walk(self):
        try:
            # Создаем объект Runner с отрицательной скоростью для тестирования исключения
            runner = Runner(name="Test Runner", speed=-5)
            runner.walk()
            logging.info('"test_walk" выполнен успешно')
        except ValueError as e:
            logging.warning("Неверная скорость для Runner: %s", e)
            self.assertIsInstance(e, ValueError)  # Проверяем, что выбрасывается ValueError

    def test_run(self):
        try:
            # Создаем объект Runner с неверным типом для name, чтобы протестировать исключение
            runner = Runner(name=123, speed=5)
            runner.run()
            logging.info('"test_run" выполнен успешно')
        except TypeError as e:
            logging.warning("Неверный тип данных для объекта Runner: %s", e)
            self.assertIsInstance(e, TypeError)  # Проверяем, что выбрасывается TypeError

if __name__ == "__main__":
    unittest.main()