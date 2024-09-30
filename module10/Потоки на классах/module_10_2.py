import threading
import time

class Knight(threading.Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power
        self.enemies = 100 
        self.days = 0  

    def run(self):
        print(f"{self.name}, на нас напали!")
        while self.enemies > 0:
            time.sleep(1)  
            self.days += 1
            self.enemies -= self.power  
            if self.enemies < 0:
                self.enemies = 0  
            print(f"{self.name} сражается {self.days} день(дня)..., осталось {self.enemies} воинов.")
        print(f"{self.name} одержал победу спустя {self.days} дней(дня)!")

def main():
    first_knight = Knight('Sir Lancelot', 10)
    second_knight = Knight('Sir Galahad', 20)

    # Запускаем потоки рыцарей
    first_knight.start()
    second_knight.start()

    # Ожидаем завершения всех потоков
    first_knight.join()
    second_knight.join()

    print("Все битвы закончились!")

if __name__ == "__main__":
    main()