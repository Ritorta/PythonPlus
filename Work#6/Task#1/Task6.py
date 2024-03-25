# Решить задачи, которые не успели решить на семинаре, задача №6

# Добавьте в модуль с загадками функцию, которая принимает на вход
# строку (текст загадки) и число (номер попытки, с которой она угадана).
# Функция формирует словарь с информацией о результатах отгадывания.
# Для хранения используйте защищённый словарб уровня модуля.
# Отдельно напишите функцию, которая выводит результаты угадывания
# из защищённого словаря в удобном для чтения виде.
# Для формирования результатов используйте генераторное выражение.

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
        save_results(riddle, result)


_data = {}
    

def save_results(puzzle: str, nn: int) -> None:
    _data[puzzle] = nn
    


def show_results():
    res = (f'The riddle "{puzzle}" has been solved, whth an try № {nn}' if nn > 0 else\
            f'The riddle "{puzzle}" has not been solved'\
                for puzzle, nn in _data.items())
    print(*res, sep='\n')


if __name__ == '__main__':
    storage()
    show_results()
