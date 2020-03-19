__author__ = "Glukharev Oleg"
"""1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата
«день-месяц-год».В рамках класса реализовать два метода. Первый, с декоратором @classmethod,
должен извлекать число, месяц, год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod,
должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных.
"""


class Data:

    @staticmethod
    def validation(param, number):
        try:
            if param == 'd':
                if 1 <= number <= 31:
                    return number
                else:
                    raise Valid_except(f'Ошибка ввода даты: {param}:{number}')
            elif param == 'm':
                if 1 <= number <= 12:
                    return number
                else:
                    raise Valid_except(f'Ошибка ввода даты: {param}:{number}')
            elif param == 'y':
                if 1 <= number <= 9999:
                    return number
                else:
                    raise Valid_except(f'Ошибка ввода даты: {param}:{number}')
        except Valid_except as eror:
            print(eror)

    @classmethod
    def to_extract(cls, data):
        cls.data = data
        try:
            s_data = [int(item) for item in data.split('-')]
            dmy = {'d': s_data[0], 'm': s_data[1], 'y': s_data[2]}
            return {key: value for key, value in dmy.items() if isinstance(Data.validation(key, value), int)}



        except ValueError:
            return f'Ошибка типпа введеных данных'


class Valid_except(Exception):
    def __init__(self, txt):
        self.txt = txt


data_0 = '17-03-2020'
data_1 = '123-12-2020'
data_2 = '21-13-2020'
data_3 = '17-03-20202'

d = Data.to_extract(data_3)
print(d)
d = Data.to_extract(data_2)
print(d)
d = Data.to_extract(data_1)
print(d)
d = Data.to_extract(data_0)
print(d)

"""2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных, 
вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту 
ситуацию и не завершиться с ошибкой.
"""


class Zero_except(Exception):
    def __init__(self, txt):
        self.txt = txt


class Division:
    def __init__(self, divisible, divider):
        self.divisible = divisible
        self.divider = divider

    @property
    def get_res_division(self):
        try:
            if self.divider == 0:
                raise Zero_except(f' You input divider = {self.divider}')
            else:
                return f'Result: {self.divisible} / {self.divider} = {round(self.divisible / self.divider, 2)}'
        except Zero_except as err:
            return f' You input divider = {self.divider}'


res_0 = Division(130, 13)
res_1 = Division(130, 0)
print(res_1.get_res_division)
print(res_0.get_res_division)

"""3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять список 
только числами. Класс-исключение должен контролировать типы данных элементов списка.
Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно, пока пользователь сам не остановит 
работу скрипта, введя, например, команду “stop”. При этом скрипт завершается, сформированный список с числами 
выводится на экран.
Подсказка: для данного задания примем, что пользователь может вводить только числа и строки. 
При вводе пользователем очередного элемента необходимо реализовать проверку типа элемента и вносить его в список,
только если введено число. Класс-исключение должен не позволить пользователю ввести текст (не число) и 
отобразить соответствующее сообщение. При этом работа скрипта не должна завершаться.
"""


class Digit_except(Exception):
    def __init__(self, txt):
        self.txt = txt


class Digits_items:
    def __init__(self, user_input=None):
        self.user_input = user_input
        self.result = []

    @property
    def get_digit(self):

        while True:

            try:
                self.user_input = input('Введите число.(для выходы введите: stop): ')
                if str(self.user_input).lower() == 'stop':
                    print(self.result)
                    break
                if self.user_input.isdigit():
                    self.result.append(self.user_input)
                elif isinstance(self.user_input, str):
                    raise Digit_except('Input type error')

            except Digit_except as err:
                print(err)


res = Digits_items().get_digit

"""4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). 
В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
уникальные для каждого типа оргтехники. 
5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу в
определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники,
а также других данных, можно использовать любую подходящую структуру, например словарь.
6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных. 
Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных. 
Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей,
изученных на уроках по ООП.
"""


class Warehouse:
    def __init__(self, name, external_logistics_departament, internal_logistics_departament, sales_departament):
        self.name = name
        self.external_logistics_departament = external_logistics_departament
        self.internal_logistics_departament = internal_logistics_departament
        self.sales_departament = sales_departament




class OfficeEquipment:
    def __init__(self, name, amount, paper_size, manufacture_company, production_year):
        self.name = name
        self.amount = amount
        self.paper_size = paper_size
        self.manufacture_company = manufacture_company
        self.production_year = production_year

    def full_product_description(self):
        pass



class Printer(OfficeEquipment):
    def __init__(self, name, paper_size, amount, manufacture_company, production_year,
                 printing_technology):
        super().__init__(name, amount, paper_size, manufacture_company, production_year)
        self.printing_technology = printing_technology

    @property
    def full_product_description(self):
        return f'{self.name} | {self.paper_size} | {self.amount} |\n{self.manufacture_company} | ' \
               f'{self.production_year} |\n{self.printing_technology}\n'


class Scanner(OfficeEquipment):
    def __init__(self, name, amount, paper_size, manufacture_company, production_year,
                 scanner_type, sensor_type):
        super().__init__(name, amount, paper_size, manufacture_company, production_year)
        self.scanner_type = scanner_type
        self.sensor_type = sensor_type

    @property
    def full_product_description(self):
        return f'{self.name} | {self.paper_size} | {self.amount} |\n{self.manufacture_company} | ' \
               f'{self.production_year} |\n{self.scanner_type} | {self.sensor_type}\n'


class Copier(OfficeEquipment):
    def __init__(self, name, amount, paper_size, manufacture_company, production_year,
                 print_speed, cartridge_resource, is_color):
        super().__init__(name, amount, paper_size, manufacture_company, production_year)
        self.print_speed = print_speed
        self.cartridge_resource = cartridge_resource
        self.is_color = is_color

    @property
    def full_product_description(self):
        return f'{self.name} | {self.paper_size} | {self.amount} |\n{self.manufacture_company} | ' \
               f'{self.production_year} |\n{self.print_speed} | {self.cartridge_resource} | is_color: {self.is_color}\n'


"""7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число»,
реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта, 
создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров. 
Проверьте корректность полученного результата.
"""


class ComplexNumCalc:
    def __init__(self, material_part, imaginary):
        self.material_part = material_part
        self.imaginary = imaginary

    def __add__(self, other):
        material_part = self.material_part + other.material_part
        imaginary = self.imaginary + other.imaginary
        return f'{material_part} + {imaginary}i'

    def __sub__(self, other):
        material_part = self.material_part - other.material_part
        imaginary = self.imaginary - other.imaginary
        return f'{material_part} + {imaginary}i'

    def __mul__(self, other):
        material_part = self.material_part * other.material_part - self.imaginary * other.imaginary
        imaginary = self.imaginary * other.material_part + self.material_part * other.imaginary
        return f'{material_part} + {imaginary}i'

    def __truediv__(self, other):
        material_part = round((self.material_part * other.material_part + self.imaginary * other.imaginary) \
                              / (other.material_part ** 2 + other.imaginary ** 2), 2)
        imaginary = round((self.imaginary * other.material_part - self.material_part * other.imaginary) \
                          / (other.material_part ** 2 + other.imaginary ** 2), 2)
        return f'{material_part} + {imaginary}i'


a_bi = ComplexNumCalc(2, 5)
c_di = ComplexNumCalc(12, 6)
print(a_bi + c_di)
print(a_bi - c_di)
print(a_bi * c_di)
print(a_bi / c_di)
