import time
class Video:
    def __init__(self, title, duration, time_now: int = 0, adult_mode: bool = False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

    def __str__(self):
        return self.title

    def __repr__(self):
        return self.title

class User:
    def __init__(self, nickname, pw, age):
        self.nickname = nickname
        self.pw = hash(pw)
        self.age = age

    def __str__(self):
        return self.nickname

    def __eq__(self, other):
        return other.nickname == self.nickname

    def get_info(self):
        return self.nickname, self.pw

class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, pw):
        self.nickname = nickname
        self.pw = hash(pw)
        for self.users in self.users:
            if (nickname, hash(pw)) == nickname.get_info():
                self.current_user = nickname
                return nickname

    def register(self, nickname, pw, age):
        nickname = User(nickname, pw, age)
        if nickname not in self.users:
            self.users.append(nickname)
            self.current_user = nickname
        else:
            print(f'Пользователь {nickname} уже существует')

    def add(self, *videos: Video):
        for video in videos:
            if video.title not in self.videos:
                self.videos.append(video)

    def get_videos(self, search):
        titles = []
        for video in self.videos:
            if search.lower() in str(video).lower():
                titles.append(video)

        return titles

    def watch_video(self, title):
        if self.current_user is None:
            print('Войти в аккаунт чтобы смотреть видео')
            return
        for video in self.videos:
            if title == video.title:
                if video.adult_mode and self.current_user.age >= 18:
                    while video.time_now < video.duration:
                        video.time_now += 1
                        print(video.time_now, end=' ')
                        time.sleep(1)
                    video.time_now = 0
                    print('Конец видео')
                else:
                    print('Вам нет 18 лет, пожалуйста покиньте страницу')
                break

    def log_out (self):
        self.current_user = None

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
