__author__ = "Glukharev Oleg"

"""1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление. Числа запрашивать 
у пользователя, предусмотреть обработку ситуации деления на ноль.
"""


def division(digit_1, digit_2):
    """Деление 2-ух позиционных аргументов с обработкой исключений:
    ValueError, ZeroDivisionError
    """
    try:
        digit_1 = float(input('введите 1-ое число: '))
        digit_2 = float(input('введите 2-ое число: '))
        return int(digit_1) / int(digit_2)
    except ValueError:
        return 'Ошибка ввода'
    except ZeroDivisionError:
        return "На ноль делить нельзя"


print(f'{division(2, 4)}\n{"-*-*" * 42}')

"""2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения, 
город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.
"""


def personal_data(name, surname, year_of_birth, city_of_residence, email, phone):
    """Функция принимает обязательные аргументы, вывод будет происходить корректно с вводои именованых аргументов """
    return f'Имя: {name}\nФамилия: {surname}\nГод рождения: {year_of_birth}\n' \
           f'Город проживания: {city_of_residence}\nЭлектронная почта: {email}\nНомер телефона: {phone}'


print(personal_data(name='Oleg', surname='Glukharev', year_of_birth='1992', city_of_residence='St. Petersburg',
                    email='111111111@222222222.333', phone='12345678900'))


def personal_data(name='name', surname='surname', year_of_birth='year_of_birth', city_of_residence='city_of_residence',
                  email='emil', phone='phone'):
    """Функция принимает необязательные аргументы, нозапрашимает ввод по средствам функции input() """
    name = input('введите имя: ')
    surname = input('Введите фамилию: ')
    year_of_birth = input('Введите год рождения: ')
    city_of_residence = input('Введите город проживания: ')
    email = input('Введите электронную почту(email): ')
    phone = input('Введите номер телефона: ')
    return f'Имя: {name}\nФамилия: {surname}\nГод рождения: {year_of_birth}\n' \
           f'Город проживания: {city_of_residence}\nЭлектронная почта: {email}\nНомер телефона: {phone}'


print(f'{personal_data()}\n{"-*-*" * 42}')

"""3. Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму 
наибольших двух аргументов.
"""


# def my_func(*args):
def my_func(arg0, arg1, arg2):
    """Функция принимает 3-и аргумента. Аргументы помещаются в список, который сортируется функцией sorted()
    Возвращается сумма последних двух аргументов([-1][-2])
    """
    # arg_list = sorted([*args])
    arg_list = sorted([arg0, arg1, arg2])
    return arg_list[-1] + arg_list[-2]


print(f'{my_func(7, 4, 9)}\n{"-*-*" * 42}')

"""4. Программа принимает действительное положительное число x и целое отрицательное число y.
Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора **.
Второй — более сложная реализация без оператора **, предусматривающая использование цикла.
"""


def negative_exponentiation(x, y):
    """Функция возведения в степень по средстваи оператора '**' """
    return x ** y


print(negative_exponentiation(2, -4))


def negative_exponentiation2(x, y):
    """Функция возведения в степень.
    Если второй аргумент положительный то возвращается число умноженое само на себя 'y' раз
    Если второй аргумент отрицательный то число умножается само на себя 'y' раз
    и возвращается выражение 1/(полученное число 'x')
    """
    digit = x
    if abs(y) == y:
        for itm in range(1, y):
            x *= digit
        return x
    else:
        for itm in range(1, abs(y)):
            x *= digit
        return 1 / x


print(f'{negative_exponentiation2(2, -4)}\n{"-*-*" * 42}')
"""5. Программа запрашивает у пользователя строку чисел, разделенных пробелом. 
При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел,
разделенных пробелом и снова нажать Enter. Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
Но если вместо числа вводится специальный символ, выполнение программы завершается.
Если специальный символ введен после нескольких чисел, 
то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.
"""


def digits_items_sum(digits):
    """ Функция обработки строки , принимаемая списком и возвращении суммы всех чисел в списке"""
    items_digits = []
    while digits:
        if digits[-1].lower() == 'q':
            global Exit
            Exit = False
            digits.pop()
        else:
            try:
                items_digits.append(int(digits.pop()))
            except ValueError:
                continue
    return sum(items_digits)


user_input = None
total_amount = 0
Exit = True

while Exit:
    user_input = input('Строку чисел, разделенных пробелом(для выхода необходимо ввести: q): ').split(' ')
    result = digits_items_sum(user_input)
    print(f'Сумма только что введеных чисел: {result}')
    total_amount += result
    print(f'Общая сумма: {total_amount}')

print(f'{"-*-*" * 42}')
"""6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
Каждое слово состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки,
но каждое слово должно начинаться с заглавной буквы. Необходимо использовать написанную ранее функцию int_func().
"""
test = 'false true none and with as assert break class continue def del elif else for else if else except ' \
       'finally try for from global if import in is lambda nonlocal not or pass raise return try while yield'


def string_title(exemple_string):
    """Функция переводит все слова принятой строки: 1 символ верхний регист , остальная часть слова нижний регистр
    методом .title()
    """
    return exemple_string.title()


print(string_title(test))


def int_func(exemple_string):
    """Функция принимает слово, преобразует 1-ый символ в верхний регистр, а остальную часть слова в нижний регистр"""
    if exemple_string[0]:
        return exemple_string[0].upper() + exemple_string[1:].lower()


print(int_func('test'))


def string_func(exemple_string):
    """Функция переводит все слова (разделенные пробелом) принятой строки:
    1-ый символ верхний регист , остальная часть слова нижний регистр
    """
    exemple_string = exemple_string.split(' ')
    result_string = []
    for itm in exemple_string:
        result_string.append(int_func(itm))
    return ' '.join(result_string)


print(f'{string_func(test)}\n{"-*-*" * 42}')
