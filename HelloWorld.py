#HelloWorld.py

print("Hello World!")
name = input("What is your name: ")
# Переменные можна устанавливать через запятую сколько угодно. Будут выводится через пробел
print("Hello,", name,name,name)

i = 5
while i < 15:
    print(i)
    i = i + 2

for i in 'hello world':
    # end - что будет подставлятся в конце строки. По умолчанию \n перенос строки
    print(i * 2, end='')

# Для новой печати с новой строки
print()

for i in 'hello world':
    if i == 'o':
        continue # переход к следующему проходу цикла
    print(i * 2, end='')

print()

for i in 'hello world':
    if i == 'o':
        break # прекращение выполнения цикла
    print(i * 2, end='')

print()

for i in  'hello world':
    if i == 'a':
        break
else: # Выполняется только если break не был вызван
    print('No letter a in the string')

a = int(input("Enter number: "))
if a < -5:
    print('Low')
elif -5 <= a <= 5:
    print('Mid')
else:
    print('Hight')









