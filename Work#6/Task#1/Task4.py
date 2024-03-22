# Решить задачи, которые не успели решить на семинаре, задача №4

# Создайте модуль с функцией внутри.
# Функция получает на вход загадку, список с возможнными
# вариантами отгадок и количество попыток на угадывание.
# Программа возращает номер попытки, с которой была отгадана
# загадка или ноль если поытки исчерпаны.


def riddle(riddle_text: str, answers: list[str], count: int = 3) -> int:
    print(f'Guess the riddle:\n{riddle_text}')
    for nn in range(1, count + 1):
        ans = input(f'Trying: №{nn}, you answer: ').lower()
        if ans in answers:
            return nn        
    return 0


if __name__ == '__main__':
    result = riddle('Winter and summer with one color. What is it?', ['сhistmas tree', 'ёлка'])
    print(f'Yes is correctly, whth an try № {result}' if result > 0 else 'Nope, true again')
