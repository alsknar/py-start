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

