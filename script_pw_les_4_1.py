__author__ = 'Glukharev Oleg'

"""1 Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника. 
В расчете необходимо использовать формулу: (выработка в часах*ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
"""
from sys import argv


def employee_payroll(argv):
    """Параметрическая скрипт функция расчета заработной платы сотрудника (выработка в часах*ставка в час) + премия
    с вводом параметров из командной строки"""
    try:
        script_name, production_in_hours, rate_per_hour, premium = argv
        return f'Заработной платы сотрудника составила: ' \
               f'{(float(production_in_hours) * float(rate_per_hour)) + float(premium)}\nФормула рассчета' \
               f'((выработка в часах: {production_in_hours} * ставка в час: {rate_per_hour}) + премия:{premium})'
    except ValueError:
        print(f'{argv[1:]} - Ошибка ввода данных')


print(employee_payroll(argv))
