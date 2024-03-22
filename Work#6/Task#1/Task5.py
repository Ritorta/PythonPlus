# Решить задачи, которые не успели решить на семинаре, задача №5

# Добавьте в модуль с загадками функцию, которая хранит словарь списков.
# Ключ словаря - загадка, значние - список с отгадками.
# Функция в цикле вызвает загадывающую функцию, чтобы передать ей все
# свои загадки.

from Task4 import riddle as rd


def storage():
    puzzels = {
        'I do not have wings, but I can fly. I don’t have eyes, but I can cry! What is it?' : ['cloud', 'облако'],
        'Clean, but not water, White, but bot snow, Sweet, but not ice-cream. What is it?' : ['sugar', 'сахар'],
        'I can fly. But i am not a bird. I sleep during the day. What is it?' : ['a bat', 'bat', 'bat-pony', 'летучая-мышь', 'летучая мышь'],
    }
    for riddle, answer in puzzels.items():
        result = rd(riddle, answer)
        print(f'Yes is correctly, whth an try № {result}' if result > 0 else 'Nope')


if __name__ == '__main__':
    storage()
