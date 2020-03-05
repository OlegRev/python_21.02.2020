__author__ = 'Glukharev Oleg'

"""2 Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.
Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
Результат: [12, 44, 4, 10, 78, 123].
"""
source_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result_list = [source_list[itm + 1] for itm in range(len(source_list) - 1) if source_list[itm] < source_list[itm + 1]]
print(f'Исходного списка: {source_list}\nРезультат: {result_list}')

"""3 Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21. Необходимо решить задание в одну строку.
Подсказка: использовать функцию range() и генератор.
"""
gen_list = [itm for itm in range(20, 241) if itm % 20 == 0 or itm % 21 == 0]
print(gen_list)

"""4 Представлен список чисел. Определить элементы списка, не имеющие повторений.
Сформировать итоговый массив чисел, соответствующих требованию. 
Элементы вывести в порядке их следования в исходном списке.
Для выполнения задания обязательно использовать генератор.
Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
Результат: [23, 1, 3, 10, 4, 11]
"""
source_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
res_list = []
for item in source_list:
    if item in res_list:
        res_list.remove(item)
    else:
        res_list.append(item)
print(f'Пример исходного списка: {source_list}\nРезультат: {res_list}')

source_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
res_gen_list = [itm for itm in source_list if source_list.count(itm) == 1]
print(f'Результат:  {res_gen_list}')

"""5 Реализовать формирование списка, используя функцию range() и возможности генератора.
В список должны войти четные числа от 100 до 1000 (включая границы).
Необходимо получить результат вычисления произведения всех элементов списка.
Подсказка: использовать функцию reduce().
"""
from functools import reduce

res_list = [itm for itm in range(100, 1001) if itm % 2 == 0]
print(reduce(lambda el_1, el_2: el_1 * el_2, res_list))

"""6 Реализовать два небольших скрипта: 
а) итератор, генерирующий целые числа, начиная с указанного, 
б) итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools. 
Обратите внимание, что создаваемый цикл не должен быть бесконечным. 
Необходимо предусмотреть условие его завершения. 
Например, в первом задании выводим целые числа, начиная с 3,
а при достижении числа 10 завершаем цикл.
Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.
"""
from itertools import count
from itertools import cycle


def item_count(digit, number):
    """Функция итератора count(digit, number) """
    itm_list = []
    for itm in count(digit):
        if itm > number:
            break
        else:
            itm_list.append(itm)
        yield itm


try:
    user_input_digit = int(input('Введите целое положительное число "начала" итератора: '))
    user_input_number = int(input('Введите целое положительное число "конца" итератора: '))
    user_input_cycle = int(input('Введите целое положительное число "цикла" : '))
except ValueError:
    print('Ошибка ввода: "начало итератора" = 3 "конец итератора" = 10 "число цикла" = 10')
    user_input_digit = 3
    user_input_number = 10
    user_input_cycle = 10
try:
    print(*item_count(user_input_digit, user_input_number))
except NameError:
    print('введен')
iter_list = item_count(user_input_digit, user_input_number)


def item_cycle(number):
    num_cycl = 0
    for el in cycle(iter_list):
        num_cycl += 1
        if num_cycl > number:
            break
        yield el


print(*item_cycle(user_input_cycle))

"""7 Реализовать генератор с помощью функции с ключевым словом yield, 
создающим очередное значение. При вызове функции должен создаваться объект-генератор.
Функция должна вызываться следующим образом: for el in fact(n). 
Функция отвечает за получение факториала числа, 
а в цикле необходимо выводить только первые n чисел, начиная с 1! и до n!.
Подсказка: факториал числа n — произведение чисел от 1 до n. Например,
факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.
"""
from functools import reduce


def fact(n):
    try:
        res_list = [itm for itm in range(1, n + 1)]
        yield (reduce(lambda el_1, el_2: el_1 * el_2, res_list))
    except TypeError:
        print(f'TypeError - Ошибка типа данных')


user_input = input(f'Для вывода: n! = 1 * 2 * 3 * ...*n\nВведите число n: ')
try:
    user_input = int(user_input)
except ValueError:
    print(f'ValueError - Ошибка ввода данных')
for el in fact(user_input):
    print(f'{user_input}! = {el}')
