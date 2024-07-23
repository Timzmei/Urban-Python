import time as tm

class UrTube():

    
    def __init__(self, users = [], videos = [], current_user = None):
        self.users = users
        self.videos = videos
        self.current_user = current_user
        
    def log_in(self, nickname, password):
        for user in self.users:
            if user.nickname == nickname and user.password == hash(password):
                self.current_user = user
                return True
        return False
    
    def register(self, nickname, password, age):
        k = False
        if len(self.users) == 0:
            self.users.append(User(nickname, hash(password), age))
            print(f"Пользователь {nickname} успешно зарегистрирован")
            self.log_in(nickname, password)
            k = True
        else:
            for user in self.users:
                if user.nickname == nickname:
                    print(f"Пользователь {nickname} уже существует")
                    k = True
        if k == False:
            self.users.append(User(nickname, hash(password), age))
            print(f"Пользователь {nickname} успешно зарегистрирован")
            self.log_in(nickname, password)

    def log_out(self):
        self.current_user = None
        
    def add(self, *args):
        for video in args:
            if len(self.videos) == 0:
                self.videos.append(video)
            for old_video in self.videos:
                if old_video.title.lower() != video.title.lower():
                    self.videos.append(video)

    def get_videos(self, title):
        list_video = []
        for video in self.videos:
            if title.lower() in video.title.lower():
                list_video.append(video.title)
        return list_video
    
    def watch_video(self, title):
        if self.current_user is None:
            print('Войдите в аккаунт, чтобы смотреть видео')
        elif self.current_user.age < 18:
            print('Вам нет 18 лет, пожалуйста покиньте страницу')
        else:
            for video in self.videos:
                # print(f'Название видео: {video.title}')
                if title.lower() == video.title.lower():
                    for i in range(1, video.duration + 1):
                        print(i, end=' ', flush=True)
                        tm.sleep(0.5)
                    print('Конец видео')
                


class Video():
    def __init__(self, title: str, duration: int, time_now = 0, adult_mode = False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode


class User():
    def __init__(self, nickname: str, password: int, age: int):
        self.nickname = nickname
        self.password = password
        self.age = age
        
    def __str__(self):
        return f'{self.nickname}'



def main():  
    ur = UrTube()
    v1 = Video('Лучший язык программирования 2024 года', 200)
    v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

    # Добавление видео
    ur.add(v1, v2)

    # Проверка поиска
    print(ur.get_videos('лучший'))
    print(ur.get_videos('ПРОГ'))

    # Проверка на вход пользователя и возрастное ограничение
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('vasya_pupkin', 'lolkekcheburek', 13)
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
    ur.watch_video('Для чего девушкам парень программист?')

    # Проверка входа в другой аккаунт
    ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
    print(ur.current_user)

    # Попытка воспроизведения несуществующего видео
    ur.watch_video('Лучший язык программирования 2024 года!')
        
if __name__ == "__main__":
    main()