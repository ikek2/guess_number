import time


def values():
    for value in range(5):
        print(value)
        if value%2 == 0:
            print('Четное число')
        else:
            print('Нечетное')
        print('Конец итерации') 

values()# Комментарии

STROKA = 'Check this lifehack'
for c in STROKA:
    print(c, end='', flush=True)
    time.sleep(0.1)