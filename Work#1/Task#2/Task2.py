# Урок 1. Основы Python

# Условие.
# 2. Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей. 
# Дано a, b, c - стороны предполагаемого треугольника. 
# Требуется сравнить длину каждого отрезка-стороны с суммой двух других. 
# Если хотя бы в одном случае отрезок окажется больше суммы двух других, 
# то треугольника с такими сторонами не существует. 
# Отдельно сообщить является ли треугольник разносторонним, равнобедренным или равносторонним.


a = float(input(f'Enter the triangle side a : '))
b = float(input(f'Enter the triangle side b : '))
c = float(input(f'Enter the triangle side c : '))

if a + b > c and a + c > b and b + c > a:
#    print("Triangle exist")
    if a != b and a != c and b != c:
        print("Triangle versatile(разносторонний)")
    elif  a == b == c:
        print("Triangle is equilateral(равносторонний)")
    else:
    #    elif a == b or b == c or c == a:     
        print("Triangle is isosceles(равнобедренный)")
else:
    print("Triangle dont exist")