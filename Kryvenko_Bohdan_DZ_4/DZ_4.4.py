'''
Написать свой модуль utils и перенести в него функцию currency_rates() из предыдущего задания. Создать скрипт,
в котором импортировать этот модуль и выполнить несколько вызовов функции currency_rates(). Убедиться, что ничего лишнего не происходит.
'''
from utils import currency_rates

print(currency_rates('USD'))
print(currency_rates('EUR'))
print(currency_rates('eur'))