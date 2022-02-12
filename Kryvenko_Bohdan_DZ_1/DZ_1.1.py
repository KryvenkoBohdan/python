'''
1. Реализовать вывод информации о промежутке времени в зависимости от его продолжительности duration в секундах:
до минуты: <s> сек; до часа: <m> мин <s> сек; до суток: <h> час <m> мин <s> сек; * в остальных случаях: <d> дн <h> час <m> мин <s> сек.
Примеры:
duration = 53
53 сек
duration = 153
2 мин 33 сек
duration = 4153
1 час 9 мин 13 сек
duration = 400153
4 дн 15 час 9 мин 13 сек
Примечание: можете проверить себя здесь, подумайте, можно ли использовать цикл для проверки работы кода сразу для
нескольких значений продолжительности, будет ли тут полезен список?
'''

duration = int(input('Введите промежуток времени в секундах:  '))
d = duration // 86400
h = duration % 86400 // 3600
m = duration % 86400 % 3600 // 60
s = duration % 86400 % 3600 % 60 // 1

if duration >= 86400:
    print(f'Введенный вами промежуток времени составляет: {d} дн {h} час {m} мин {s} сек')
elif 3600 <= duration < 86400:
    print(f'Введенный вами промежуток времени составляет: {h} час {m} мин {s} сек')
elif 60 <= duration <3600:
    print(f'Введенный вами промежуток времени составляет: {m} мин {s} сек')
else:
    print(f'Введенный вами промежуток времени составляет: {s} сек')





