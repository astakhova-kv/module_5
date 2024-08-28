class UrTube:
    def __init__(self, users=[], videos=[], current_user=None):
        self.users = []
        self.videos = []

    def __contains__(self, item):
        return (item in self.users)

    # def log_in(self, nickname, password):
    #
    #     if self.nickname in self.users:
    #         print(f"Пользователь {nickname} уже существует")
    #     else:
    #         self.users = [nickname, hash(password)]

    def register(self, nickname, password, age):
        if self.nickname not in self.users:
            self.nicname = nickname
            self.password = password
            self.age = age
            self.users = tuple(nickname, password, age)
        else:
            print(f"Пользователь {nickname} уже существует")



    def log_out(self):
        self.current_user = None

    def add(self, *args):
        self.videos = args

    def get_videos(self, key_word):
        new_videos = []
        list1 = []
        print((self.videos))
        for i in range(len(self.videos)):
            list1 = list1.append(v1.title)
            print(list1)
            print(type(list1))
            for j in list1:
                if key_word.casefold() in j.casefold():
                    new_videos.append(self.videos)
        print(new_videos)
    # def watch_video(self):


class Video:
    def __init__(self, title, duration, adult_mode=False, time_now=0):
        self.title = title
        self.duration = duration
        self.adult_mode = adult_mode
        self.time_now = time_now


class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age


# Код для проверки:
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
