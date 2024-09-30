import time
from time import sleep
import threading

def write_words(word_count, file_name):
    with open(f'module10\Создание потоков\{file_name}', 'w', encoding='utf-8') as f:
        for i in range(1, word_count + 1):
            f.write(f"Какое-то слово № {i}\n")
            sleep(0.1)
    print(f"Завершилась запись в файл {file_name}")
    
def thread_task(word_count, file_name):
    write_words(word_count, file_name)

def main():
    start_time = time.time()

    write_words(10, 'example1.txt')
    write_words(30, 'example2.txt')
    write_words(200, 'example3.txt')
    write_words(100, 'example4.txt')

    end_time = time.time()
    print(f"Работа функций заняла: {end_time - start_time:.6f} секунд")
    


    start_time_threads = time.time()

    threads = []
    threads.append(threading.Thread(target=thread_task, args=(10, 'example5.txt')))
    threads.append(threading.Thread(target=thread_task, args=(30, 'example6.txt')))
    threads.append(threading.Thread(target=thread_task, args=(200, 'example7.txt')))
    threads.append(threading.Thread(target=thread_task, args=(100, 'example8.txt')))

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    end_time_threads = time.time()
    print(f"Работа потоков заняла: {end_time_threads - start_time_threads:.6f} секунд")

if __name__ == "__main__":
    main()