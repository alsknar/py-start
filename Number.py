# Nubmer.py

# Целые числа

a = 255 + 34
print('Сумма 255 + 34 = ', a)

a = 5 * 2
print('Умножение 5 * 2 = ', a)

a = 20 / 3
print('Деление 20 / 3 = ', a)

a = 20 // 3
print('Деление без остатка 20 // 3 = ', a)

a = 20 % 3
print('Остаток от деления 20 % 3 = ', a)

a = 3 ** 4
print('Возведение в степень 3 ** 4 = ', a)

a = pow(3, 4, 27)
print('Возведение в степень по модулю 3 ** 4 % 27 = ', a)

a = 3 ** 150
print('Python 3 поддерживает дланную математику для целых числ 3 ** 150 = ', a)


# Битовые операции

n = -37
print('Число -37 в бинарном виде ', bin(n)) 

print('Количество бит для числа -37 ', n.bit_length())

print('Число -37 в байтах ', n.to_bytes(2,byteorder='big',signed=True))

print('Десятичное число из байта ', int.from_bytes(n.to_bytes(2,byteorder='big',signed=True),byteorder='big',signed=True))

# Вещественные числа

n = 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1
print(n) # 0.99999999999999 Вещественные числа с ошибками, не поддерживают длинную матемитику

n = 0.998
print(n.as_integer_ratio())

if n.is_integer():
    print('Целое число')
else:
    print('Действительное число')

print('Действительное число в шестнадцатеричном виде ',n.hex())

print('Из шестнадцатерисного вида в действительное число', float.fromhex(n.hex()))

# Подключение сторонних модулей
import math
import random

print(math.pi)
print(random.random())



