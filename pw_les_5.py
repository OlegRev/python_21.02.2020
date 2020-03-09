__author__ = "Glukharev Oleg"

"""Урок 5. Работа с файлами
1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем. 
Об окончании ввода данных свидетельствует пустая строка.
"""


def create_file_with_data(name_file='les_5_1_file.txt'):
    """Функция принимает имя файла, затем запрашивает строки для добавления в созданый файл"""
    try:
        with open(name_file, "x+") as file:
            num_string = 0
            while True:
                user_input = input('Введите строку для записи в файл(для завершения введите пустую строку): ')
                if user_input.lower() == '':
                    return (f'Файл с именем: "{name_file}" создан, в файл записано: {num_string} строк')
                else:
                    num_string += 1
                    file.write(f'{user_input}\n')
    except FileExistsError:
        return f'Ошибка: Файл с именем "{name_file}" уже существует'


print(create_file_with_data())

"""
2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
 количества слов в каждой строке.
"""


def counting_the_number_of_lines_and_characters_in_file(name_file='les_5_2_file.txt'):
    """Функция принимает имя файла для подсчета количества строк в файле,
     количества слов и символов в каждей строке и общее количество слов и символов в файле
     """
    try:
        with open(name_file, "r") as file:
            lines = file.readlines()
            number_of_lines = len(lines)
            characters = 0
            word_in_line = [len(line.split(' ')) for line in lines]
            for idx, line in enumerate(lines):
                characters += len(line)
                print(f'В {idx + 1} строке: {word_in_line[idx]}-слов и {len(line)}-символов.', end='|')

            return f'Обзор файла "{name_file}": \nКоличество строк в файле "{name_file}": {number_of_lines}\n' \
                   f'Общее количество в файле: слов {sum(word_in_line)}, символов: {characters}'
    except FileExistsError:
        return f'Ошибка: Файл с именем "{name_file}" уже существует'
    except FileNotFoundError:
        return f'Файл с именем: "{name_file}" не найден в директории'


# user_input = input('Введите имя файла: ')
print(counting_the_number_of_lines_and_characters_in_file())

""" 
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов. 
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. 
Выполнить подсчет средней величины дохода сотрудников.
"""


def employee_income(name_file='les_5_3_file.txt', salary_of_less=20000):
    """Функци принимает на вход имя файла и границу оклади ниже которой выводятся сотрудники,
    подсчитывается и выводится средний оклад сотрудников (файл должен иметь данные вида:
    Фамилия_сотрудника оклад_сотрудника(разделителем является 'пробел'))
    """
    try:
        with open(name_file, "r") as file:
            lines = [itm.strip('\n') for itm in file.readlines()]
            split_line = [line.split(' ') for line in lines]
            surnames_of_employees = [itm for line in range(len(split_line)) for itm in split_line[line]
                                     if itm.isalpha()]
            employee_salary = [int(itm) for line in range(len(split_line)) for itm in split_line[line]
                               if itm.isdigit()]
            index_res = [idx for idx, itm in enumerate(employee_salary) if itm < salary_of_less]
            average_employee_income = round(sum(employee_salary) / len(employee_salary), 2)

            return f'Обзор файла "{name_file}": \n' \
                   f'Сотрудники оклад которых менее 20000: {[surnames_of_employees[itm] for itm in index_res]}\n' \
                   f'Средняя велечина дохода сотрудников: {average_employee_income}'
    except FileNotFoundError:
        return f'Ошибка: Файл с именем "{name_file}" не найден в директории'
    except FileExistsError:
        return f'Ошибка: Файл с именем "{name_file}" уже существует'


# user_input = input('Введите имя файла: ')
print(employee_income())

# Варианты решений 1
"""
with open('pw_les_5_3.txt', 'r') as file:
   average_employee_income = 0
   surnames = []
   result = []
   file_list = [itm.strip('\n') for itm in file.readlines()]
   split_list = [line.split(' ') for line in file_list]
   res_list = [itm for lists in split_list for itm in lists]
   for itm in res_list:
       try:
           if itm.isalpha():
               result.append(itm)
           else:
               result.append(int(itm))
       except ValueError:
           continue
   res_dict = {result[itm]: result[itm + 1] for itm in range(0, len(result) - 1, 2)}
   for key in res_dict.keys():
       if res_dict[key] < 20000:
           surnames.append(key)
       average_employee_income += res_dict[key]
   average_employee_income = round(average_employee_income / len(res_dict.keys()), 2)

   print(f'Сотрудников имеет оклад менее 20 тыс: {surnames}\n'
         f'Средней величины дохода сотрудников {average_employee_income}')
"""
# Варианты решений 2
"""
with open('pw_les_5_3.txt', 'r') as file:
   file_list = [itm.strip('\n') for itm in file.readlines()]
   surnames = []
   split_list = [line.split(' ') for line in file_list]
   res = [itm for itm_list in split_list for itm in itm_list if itm.isalpha() or itm.isdigit()]
   res_dict = {res[itm]: int(res[itm + 1]) for itm in range(0, len(res) - 1, 2)}
   average_employee_income = 0

   for key in res_dict.keys():
       if res_dict[key] < 20000:
           surnames.append(key)
       average_employee_income += res_dict[key]
   average_employee_income = round(average_employee_income / len(res_dict.keys()), 2)

   print(f'Сотрудников имеет оклад менее 20 тыс: {surnames}\n'
         f'Средней величины дохода сотрудников {average_employee_income}')
"""

"""
4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. 
При этом английские числительные должны заменяться на русские. 
Новый блок строк должен записываться в новый текстовый файл.
"""


def translation_numerators_in_file(name_file='les_5_4_file.txt', new_name_file='new_les_5_4_file.txt'):
    """Функция принимает имя файла и имя нового файла для записи переведеной нумерации прописью"""
    try:
        with open(name_file, "r") as file:

            lines = [itm.strip('\n') for itm in file.readlines()]
            split_line = [line.split(' ') for line in lines]
            num_list = [_ for _ in range(17)]
            num_dict = {'1': 'Один', '2': 'Два', '3': 'Три', '4': 'Четыре', '5': 'Пять', '6': 'Шесть', '7': 'Семь',
                        '8': 'Восемь', '9': 'Девять', '10': 'Десять', '11': 'Одинадцать', '12': 'Двенадцать',
                        '13': 'Тринадцать', '14': 'Четырнадцать', '15': 'Пятнадцать', '16': 'Шестнадцать'}
            with open(new_name_file, "x+") as new_file:
                for line in split_line:
                    if int(line[2]) in num_list:
                        line[0] = num_dict[line[2]]
                        line = ' '.join(line)
                        new_file.write(f'{line}\n')
        return f'Файл "{new_name_file}" создан с записью переведенной нумерации из файла "{name_file}"'
    except FileNotFoundError:
        return f'Ошибка: Файл с именем "{name_file}" не найден в директории'
    except FileExistsError:
        return f'Ошибка: Файл с именем "{new_name_file}" уже существует'


print(translation_numerators_in_file())

"""
5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""


def create_file_with_digit(name_file='les_5_5_file.txt', n=10):
    """Функция принимает на вход имя файла который будет создан с записью ряда чисел,
    и число которое будет границей ряда от 1 до 'числа включительно'.
    """
    try:
        with open(name_file, "x+") as file:
            user_input = [str(itm) for itm in range(n + 1)]
            file.write(f"{' '.join(user_input)}\n")
        with open(name_file, "r") as file:
            data = [int(itm) for itm in file.readline() if itm.isdigit()]
            return f'Сумма чисел в файле "{name_file}" равна: {sum(data)}'
    except FileNotFoundError:
        return f'Ошибка: Файл с именем "{name_file}" не найден в директории'
    except FileExistsError:
        return f'Ошибка: Файл с именем "{name_file}" уже существует'


print(create_file_with_digit())

"""
6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет 
и наличие лекционных, практических и лабораторных занятий по этому предмету и их количество. 
Важно, чтобы для каждого предмета не обязательно были все типы занятий. Сформировать словарь, 
содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
Примеры строк файла:
Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —

Пример словаря:
{“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""


def subject_name_total_number_of_lessons(name_file='les_5_6_file.txt'):
    """Функци принимает на вход имя файла """
    try:
        with open(name_file, "r") as file:
            charectr = [':', '(л)', '(пр)', '(лаб)']
            result_list = []
            lines = [itm.strip('\n') for itm in file.readlines()]
            split_line = [line.split(' ') for line in lines]
            for itm in split_line:
                number_classes = 0
                for el in range(len(itm)):
                    if itm[el].endswith(':'):
                        itm[el] = itm[el].strip(charectr[0])
                        result_list.append(itm[el])
                    elif itm[el].endswith('(л)'):
                        itm[el] = int(itm[el].strip(charectr[1]))
                        number_classes += itm[el]
                    elif itm[el].endswith('(пр)'):
                        itm[el] = int(itm[el].strip(charectr[2]))
                        number_classes += itm[el]
                    elif itm[el].endswith('(лаб)'):
                        itm[el] = int(itm[el].strip(charectr[3]))
                        number_classes += itm[el]
                    else:
                        itm[el] = ''
                result_list.append(number_classes)
            result_dict = {result_list[itm]: result_list[itm + 1] for itm in range(0, len(result_list) - 1, 2)}

            return f'Обзор файла "{name_file}":\n{result_dict}'
    except FileNotFoundError:
        return f'Ошибка: Файл с именем "{name_file}" не найден в директории'
    except FileExistsError:
        return f'Ошибка: Файл с именем "{name_file}" уже существует'


print(subject_name_total_number_of_lessons())

"""
7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста."""
from json import dump


def company_made_profit_or_loss(name_file='les_5_7_file.txt', loos=0, json_name_file='les_5_7_file.json', open_mode_jsonfile='x+'):
    """Функци принимает на вход имя файла.txt, имя файла.json
    режим открытия файла ".json" и границу прибыли(по умолчанию "0"),ниже которой фирмы не входят в расчет
    средней прибыли компаний, подсчитывается и выводится средняя прибыль фирм и записывается в .json файл
    с режимом открытия "jsonfile_open_mode"(jsonfile_open_mode='x+')
    """
    try:
        with open(name_file, "r") as file:
            lines = [itm.strip('\n') for itm in file.readlines()]
            split_line = [line.split(' ') for line in lines]
            company_name = [line[itm] for line in split_line for itm in range(len(line)) if itm == 0]
            company_profit_loos = [int(line[itm]) - int(line[itm + 1]) for line in split_line for itm in
                                   range(0, len(line) - 1, 2)
                                   if line[itm].isdigit()]
            company_profit = [itm for itm in company_profit_loos if itm > loos]
            average_company_profit = round(sum(company_profit) / len(company_profit), 2)
            average_profit_dict = {'average_profit': average_company_profit}
            result_dict = {company_name[itm]: company_profit_loos[itm] for itm in range(len(company_name))}
            result_list = [result_dict, average_profit_dict]
    except FileNotFoundError:
        return f'Ошибка: Файл с именем "{name_file}" не найден в директории'
    try:
        with open(json_name_file, open_mode_jsonfile) as j_file:
            dump(result_list, j_file)

            return f'Обзор созданого файла{result_list}\n'
    except FileExistsError:
        with open(json_name_file, 'r') as j_file:
            return f'Ошибка: Файл с именем "{json_name_file}" уже существует\n' \
                   f'{j_file.readlines()}'
    except FileNotFoundError:
        return f'Ошибка: Файл с именем "{json_name_file}" не найден в директории'


print(company_made_profit_or_loss())
