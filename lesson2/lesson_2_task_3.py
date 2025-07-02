import math

def square(x):
    return math.ceil(x * x)
x = float(input("Сторона квадрата: "))
print(f'Площадь квадрата {math.ceil(x * x)}')