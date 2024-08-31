import time


class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age


class Video:
    def __init__(self, title, duration, adult_mode=False):
        self.title = title
        self.duration = duration
        self.adult_mode = adult_mode
        self.time_now = 0


class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, password):
        for user in range(len(self.users)):
            if nickname in self.users[user][0] and hash(password) in self.users[user][1]:
                self.current_user = nickname

    def register(self, nickname, password, age):
        for user in range(len(self.users)):
            if nickname in self.users[user][0]:
                print(f"Пользователь {nickname} уже существует")
                break
        else:
            self.nicname = nickname
            self.password = hash(password)
            self.age = age
            self.users.append([nickname, hash(password), age])
            self.current_user = nickname

    def log_out(self):
        self.current_user = None

    def add(self, *args):
        for arg in args:
            self.videos.append([arg.title, arg.duration])

    def get_videos(self, key_word):
        sort_ = []
        for video in range(len(self.videos)):
            for word in self.videos[video][0].split():
                if key_word.casefold() in word.casefold():
                    sort_.append(self.videos[video][0])
        return sort_

    def watch_video(self, title):
        for video in range(len(self.videos)):
            if self.videos[video][0] != title:
                break

        if self.current_user == None:
            print('Войдите в аккаунт, чтобы смотреть видео')
        elif self.age < 18:
            print('Вам нет 18 лет, пожалуйста покиньте страницу')
        else:
            for video in range(len(self.videos)):
                if self.videos[video][0] == title:
                    for sek in range(1, self.videos[video][1] + 1):
                        time.sleep(1)
                        print(sek, end = ' ')
                    print('Конец видео')


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
