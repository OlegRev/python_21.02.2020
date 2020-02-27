__author__ = "Glukharev Oleg"
"""
1. Создать список и заполнить его элементами различных типов данных. Реализовать скрипт проверки типа данных каждого 
элемента. Использовать функцию type() для проверки типа. Элементы списка можно не запрашивать у пользователя, 
а указать явно, в программе.
"""
type_list = [0, True, "string", 42.42, {'one': 1, 'two': 4.2, 'tree': 'is_good'}, {1, 3, 5, 7, 9, 3, 'a', 'b', 'c'}]
for itm in type_list:
    print(type(itm))
"""
2. Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы с индексами
 0 и 1, 2 и 3 и т.д. При нечетном количестве элементов последний сохранить на своем месте. 
 Для заполнения списка элементов необходимо использовать функцию input().
"""
exemple_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13']
print(exemple_list)
for itm in range(0, len(exemple_list) - 1, 2):
    exemple_list[itm], exemple_list[itm + 1] = exemple_list[itm + 1], exemple_list[itm]
print(exemple_list)

"""
3. Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится месяц 
(зима, весна, лето, осень). Напишите решения через list и через dict.
"""
# lists
digit_list = ['12', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11']
seasons_list = ['зима', 'весна', 'лето', 'осень']
user_input = input('введите номер месяца от 1 до 12: ')
while user_input not in digit_list:
    print('Вы ввели неверное значение наберите цифру от 1 до 12')
    user_input = input('введите номер месяца от 1 до 12: ')
if user_input in digit_list[0: 3: 1]:
    print(seasons_list[0])
elif user_input in digit_list[3: 6: 1]:
    print(seasons_list[1])
elif user_input in digit_list[6: 9: 1]:
    print(seasons_list[2])
else:
    print(seasons_list[3])

# dict
user_input = input('введите номер месяца от 1 до 12: ')
while user_input not in digit_list:
    print('Вы ввели неверное значение наберите цифру от 1 до 12')
    user_input = input('введите номер месяца от 1 до 12: ')
seasons = {'1': 'зима', '2': 'зима', '3': 'весна', '4': 'весна', '5': 'весна', '6': 'лето', '7': 'лето', '8': 'лето',
           '9': 'осень', '10': 'осень', '11': 'осень', '12': 'зима'}
print(seasons[user_input])

"""
4. Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с новой строки.
 Строки необходимо пронумеровать. Если в слово длинное, выводить только первые 10 букв в слове.
"""
user_input = input('строку с пробелами: ')
user_input = user_input.split()
num = 1
for itm in user_input:
    if len(itm) > 10:
        itm = itm[0: 10]
    print(f"{num}. {itm}")
    num += 1
"""
5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел. У пользователя
 необходимо запрашивать новый элемент рейтинга. Если в рейтинге существуют элементы с одинаковыми значениями, 
 то новый элемент с тем же значением должен разместиться после них.
Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].
"""
#exemple_list = range(3, 42, 3)
#exemple_list = list(reversed(exemple_list))
exemple_list = [9, 7, 6, 4, 4, 3]
num = 0
user_input = int(input('введите новое значение рейтинга: '))

for itm in exemple_list:
    if user_input < exemple_list[-1]:
        exemple_list.append(user_input)
        break
    elif itm < user_input:
        exemple_list.insert(num, user_input)
        break
    num += 1
print(exemple_list)

"""
6. *Реализовать структуру данных «Товары». Она должна представлять собой список кортежей. Каждый кортеж хранит 
информацию об отдельном товаре. В кортеже должно быть два элемента — номер товара и словарь с параметрами 
(характеристиками товара: название, цена, количество, единица измерения). Структуру нужно сформировать программно,
 т.е. запрашивать все данные у пользователя.
Пример готовой структуры:
[
(1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
(2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
(3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
]
Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара, например
 название, а значение — список значений-характеристик, например список названий товаров.
Пример:
{
“название”: [“компьютер”, “принтер”, “сканер”],
“цена”: [20000, 6000, 2000],
“количество”: [5, 2, 7],
“ед”: [“шт.”]
}
"""
product_list = []
product_structure = ['Название', 'Цена', 'Количество', 'Единица измерения']
user_input = input('Введите количество наименований товаров которое вы хотите добавить: ')
product_dict = {}
name_list = []
price_list = []
amt_list = []
units_list = []
analytic = [name_list, price_list, amt_list, units_list]
item = 0

while not user_input.isdigit():
    user_input = input('Введите целое не отрицательное количество наименований товаров: ')
for num in range(int(user_input)):
    product_name = input(f'{product_structure[0]}: ')
    name_list.append(product_name)
    product_price = input(f'{product_structure[1]}: ')

    while not product_price.isdigit():
        product_price = input(f'{product_structure[1]:}: ')
    price_list.append(product_price)
    product_amt = input(f'{product_structure[2]}: ')
    while not product_amt.isdigit():
        product_amt = input(f'{product_structure[2]}: ')
    amt_list.append(product_amt)
    product_units = input(f'{product_structure[3]}: ')
    units_list.append(product_units)
    product_list.append((num +1, {product_structure[0]: product_name, product_structure[1]: int(product_price),
                                  product_structure[2]: int(product_amt), product_structure[3]: product_units}))

for itm in product_structure:
    product_dict.update({itm: analytic[item]})
    item += 1
for itm in product_list:
    print(itm)
for itm in product_dict.items():
    print(itm)
