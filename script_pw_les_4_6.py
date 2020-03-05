__author__ = 'Glukharev Oleg'

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
from sys import argv


def item_count(argv):
    """Параметрическая скрипт функция итератора со значимыми 1-ым и 2-ым параметрами"""
    try:
        script_name, user_input_digit, user_input_number, user_input_cycle = argv
        user_input_digit, user_input_number, user_input_cycle = int(user_input_digit), int(user_input_number), int(
            user_input_cycle)
        print(f'"начало итератора" = {user_input_digit} "конец итератора" = {user_input_number} '
              f'"число цикла" = {user_input_cycle}')
    except ValueError:
        user_input_digit = 3
        user_input_number = 10
        user_input_cycle = 10
        print(f'Ошибка ввода: "начало итератора" = {user_input_digit} "конец итератора" = {user_input_number} '
              f'"число цикла" = {user_input_cycle}')

    itm_list = []
    for itm in count(user_input_digit):
        if itm > user_input_number:
            break
        else:
            itm_list.append(itm)
        yield itm

    def item_cycle(user_input_cycle):
        """Функция циклического повторения заданых ситерированых значений со значимым 3-им параметром"""
        num_cycl = 0
        for el in cycle(itm_list):
            num_cycl += 1
            if num_cycl > user_input_cycle:
                break
            yield el

    print('Вывод цикла итератора')
    [print(c) for c in item_cycle(user_input_cycle)]
    print("Вывод цикла итератора: ", *item_cycle(user_input_cycle))


print('Вывод итератора')
[print(i) for i in item_count(argv)]
print("Вывод итератора: ", *item_count(argv))
