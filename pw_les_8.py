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
print(f'{d}\n')

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
        except TypeError:
            return f' You input number = {type(self.divider)}'


res_0 = Division(130, 13)
res_1 = Division(130, 0)
res_2 = Division("130", '5')

print(res_1.get_res_division)
print(res_0.get_res_division)
print(f'{res_2.get_res_division}\n')

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
                if self.user_input.lower() == 'stop':
                    print(self.result)
                    break
                if self.user_input.isdigit():
                    self.result.append(int(self.user_input))
                elif isinstance(self.user_input, str):
                    raise Digit_except('Input type error')

            except Digit_except as err:
                print(err)


res = Digits_items().get_digit
print()
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
from abc import abstractmethod


class ProductNotFound(Exception):
    def __init__(self, txt):
        self.txt = txt


class Warehouse:
    def __init__(self, name, address, external_logistics_departament_list=None,
                 internal_logistics_departament_list=None, sales_departament_list=None):
        if sales_departament_list is None:
            sales_departament_list = [{'departament': 'sales_departament'}, ]
        if internal_logistics_departament_list is None:
            internal_logistics_departament_list = [{'departament': 'internal_logistics_departament'}, ]
        if external_logistics_departament_list is None:
            external_logistics_departament_list = [{'departament': 'external_logistics_departament_list'}, ]
        self.name = name
        self.address = address
        self.external_logistics_departament_list = external_logistics_departament_list
        self.internal_logistics_departament_list = internal_logistics_departament_list
        self.sales_departament_list = sales_departament_list

    def reception_office_equipment(self, obj):
        return self.external_logistics_departament_list.append(obj)

    def transfer_to_departament(self, obj, departament_out, departament_in):
        try:
            if obj not in departament_out:
                raise ProductNotFound(f'Товар не найден в передающем департаменте')

            departament_in.append(obj)
            departament_out.remove(obj)
            return f'Офисная техника {obj.model_name} в количестве {obj.amount}\n' \
                   f'Передано из департамента {departament_out[0]["departament"]}\n' \
                   f'в департамент {departament_in[0]["departament"]}'

        except ProductNotFound as err:
            return err
        except KeyError:
            return f'Разные объекты нельзя сложить! '

    @staticmethod
    def get_amount(d1, d2):
        return {k: v for k, v in d1.items() if k in d2 and v != d2[k]}


class OfficeEquipment:
    def __init__(self, model_name, amount, paper_size, manufacture_company, production_year):
        self.model_name = model_name
        self.amount = amount
        self.paper_size = paper_size
        self.manufacture_company = manufacture_company
        self.production_year = production_year

    @abstractmethod
    def full_product_description(self):
        pass


class Printer(OfficeEquipment):
    def __init__(self, model_name, amount, paper_size, manufacture_company, production_year,
                 printing_technology):
        super().__init__(model_name, amount, paper_size, manufacture_company, production_year)
        self.printing_technology = printing_technology

    @property
    def full_product_description(self):
        return {'model_name': self.model_name, 'amount': self.amount, 'paper_size': self.paper_size,
                'manufacture_company': self.manufacture_company, 'production_year': self.production_year,
                'printing_technology': self.printing_technology}


class Scanner(OfficeEquipment):
    def __init__(self, model_name, amount, paper_size, manufacture_company, production_year,
                 scanner_type, sensor_type):
        super().__init__(model_name, amount, paper_size, manufacture_company, production_year)
        self.scanner_type = scanner_type
        self.sensor_type = sensor_type

    @property
    def full_product_description(self):
        return {'model_name': self.model_name, 'amount': self.amount, 'paper_size': self.paper_size,
                'manufacture_company': self.manufacture_company, 'production_year': self.production_year,
                'scanner_type': self.scanner_type, 'sensor_type': self.sensor_type}


class Copier(OfficeEquipment):
    def __init__(self, model_name, amount, paper_size, manufacture_company, production_year,
                 print_speed, cartridge_resource, is_color=False):
        super().__init__(model_name, amount, paper_size, manufacture_company, production_year)
        self.print_speed = print_speed
        self.cartridge_resource = cartridge_resource
        self.is_color = is_color

    @property
    def full_product_description(self):
        return {'model_name': self.model_name, 'amount': self.amount, 'paper_size': self.paper_size,
                'manufacture_company': self.manufacture_company, 'production_year': self.production_year,
                'print_speed': self.print_speed, 'cartridge_resource': self.cartridge_resource,
                'is_color': self.is_color}


warehouse = Warehouse('Sklad', '')
p_0 = Printer('SLaserP', 25, ['A4', 'A3'], 'samsung', 2019, 'laser_type')
p_1 = Printer('SLaserP', 25, 'A4', 'samsung', 2019, 'laser_type')
s_0 = Scanner('SLaserS', 25, 'A4', 'samsung', 2019, 'laser_type', 'sensor_0')
s_1 = Scanner('SLaserS', 25, 'A4', 'samsung', 2019, 'laser_type', 'sensor_1')
s_3 = Scanner('SLaserS', 225, 'A4', 'samsung', 2019, 'laser_type', 'sensor_0')
c_0 = Copier('SLaserC', 22, 'A4', 'samsung', 2019, '1 in second', 1024, True)
c_3 = Copier('SLaserC', 25, ['A4', 'A3'], 'samsung', 2019, '1 in second', 1024)

print(s_3.full_product_description)

print(warehouse.external_logistics_departament_list)

warehouse.reception_office_equipment(p_0)
warehouse.reception_office_equipment(p_1)
warehouse.reception_office_equipment(s_0)
warehouse.reception_office_equipment(s_1)
warehouse.reception_office_equipment(s_3)
warehouse.reception_office_equipment(c_0)
warehouse.reception_office_equipment(c_3)

print(f'{warehouse.external_logistics_departament_list}\n{len(warehouse.external_logistics_departament_list)}')

print(warehouse.transfer_to_departament(s_0, warehouse.external_logistics_departament_list,
                                        warehouse.internal_logistics_departament_list))
print(warehouse.transfer_to_departament(s_3, warehouse.external_logistics_departament_list,
                                        warehouse.internal_logistics_departament_list))

print(warehouse.transfer_to_departament(p_0, warehouse.external_logistics_departament_list,
                                        warehouse.sales_departament_list))
print(warehouse.transfer_to_departament(c_0, warehouse.external_logistics_departament_list,
                                        warehouse.sales_departament_list))

print(f'{"*" * 30}\n{warehouse.internal_logistics_departament_list}\n'
      f'{warehouse.internal_logistics_departament_list[1].full_product_description}\n'
      f'{warehouse.internal_logistics_departament_list[2].full_product_description}\n')
print(f'{"*" * 30}\n{warehouse.sales_departament_list}\n'
      f'{warehouse.sales_departament_list[1].full_product_description}\n'
      f'{warehouse.sales_departament_list[2].full_product_description}')
print(f'{"*" * 30}\n{warehouse.external_logistics_departament_list}\n'
      f'{len(warehouse.external_logistics_departament_list)}')
print()

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
