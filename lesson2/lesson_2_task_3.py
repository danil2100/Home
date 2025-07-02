import math


def square(x):
    return math.ceil(x * x)


x = float(input("Сторона квадрата: "))
result = square(x)
rounded_result = math.ceil(result)

print(f'Площадь квадрата {math.ceil(x * x)}')
