#система регистрации
class Database:
    def __init__(self):
        self.data = {}

    def add_user(self, username, password):
        self.data[username] = password

class User:
    '''
    Класс пользователя, содержащий атрибуты: логин и пароль
    '''
    def __init__(self, username, password, password_confirm):
        self.username = username
        if password == password_confirm:
            self.password = password


if __name__ == "__main__":
    database = Database()
    while True:
        choice = int(input('Приветствую. Выбирите действие: \n1 - Вход\n2 - Регистрация\n'))
        if choice == 1:
            login = input('Введите логин: ')
            password = input('Введите пароль: ')
            if login in database.data:
                if password == database.data[login]:
                    print(f'Вход выполнен, {login}')
                    break
                else:
                    print('Пользователь ввёл неверный пароль')
            else:
                print('Пользователь не найден')

        if choice == 2:
            user = User(input('Введите логин: '), password := input('Введите пароль: '),
                        password2 := input('Повторите пароль: '))
            list_ = []
            count_title = 0
            count_digit = 0
            for i in range(len(password)):
                list_.append(password[i])
            for elem in list_:
                if elem.isdigit():
                    count_digit += 1
                if elem.istitle():
                    count_title += 1
            if (password != password2 or len(password) <= 8 or password.isalnum() == True or count_title == 0
                    or count_digit == 0):
                print(f'Проверьте свой пароль "{password}" на соответствие требованиям')
                continue
            database.add_user(user.username, user.password)
        print(database.data)