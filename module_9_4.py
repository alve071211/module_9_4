first = 'Мама мыла раму'
second = 'Рамена мало было'
third = list(map(lambda x, y: x[0] == y[0], first, second))
print(third)

def get_advanced_writer(file_name):
        def write_everything(*data_set):
            with open('file_9_4.txt', 'a+') as file:
                for data in data_set:
                    file.write(str(data) + "\n")
            return
        return write_everything

write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

from random import choice
class MysticBall():
    def __init__(self, *words):
        self.words = tuple(words)
    def __call__(self):
        return choice(self.words)

first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())




