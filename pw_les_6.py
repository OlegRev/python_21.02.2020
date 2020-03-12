"""1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы:
красный, желтый, зеленый. Продолжительность первого состояния (красный) составляет 7 секунд,
второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
 Проверить работу примера, создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее
сообщение и завершать скрипт.
"""
from itertools import cycle
from time import sleep


class TrafficLight:
    def __init__(self, __color):
        self.__color = __color
        self.get_tl(5)

    def get_tl(self, number):
        color_list = ['Red', 'Yellow', 'Green', 'Yellow']

        while color_list[0] != self.__color:
            el = color_list.pop(0)
            color_list.append(el)
        num_cycl = 0
        for idx, itm in cycle(enumerate(color_list)):
            self.__color = color_list[idx]
            print(self.get_color())
            num_cycl += 1
            if num_cycl > number:
                break
            elif self.__color == 'Red' or self.__color == 'Green':
                sleep(7)
            else:
                sleep(2)

    def get_color(self):
        return self.__color


traffic_light = TrafficLight('Yellow')
print('#' * 20)
traffic_light_1 = TrafficLight('Green')

"""2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина). 
Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными.
Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна. 
Использовать формулу: длинаширинамасса асфальта для покрытия одного кв метра дороги асфальтом,
толщиной в 1 см*число см толщины полотна. Проверить работу метода.
Например: 20м*5000м*25кг*5см = 12500 т
"""


class Road:
    def __init__(self, __length, __width):
        self.__length = __length
        self.__width = __width

    def get_mass_of_asphalt(self, thickness):
        m = 25
        mass_of_asphalt = self.__length * self.__width * thickness * m
        return f'Масса асфальта необходимая для покрытия дорожного полотна\n толщиной = {thickness} см,' \
               f' длинной = {self.__length} м и шириной = {self.__width} м:\n' \
               f'{round(mass_of_asphalt, 2)} килограмм\nили\n' \
               f'{round(mass_of_asphalt / 1000, 2)} тон'


road_0 = Road(20, 5000)
print(road_0.get_mass_of_asphalt(5))
road_1 = Road(30, 10000)
print(road_1.get_mass_of_asphalt(10))

"""3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker. 
В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии 
(get_total_income). Проверить работу примера на реальных данных (создать экземпляры класса Position, 
передать данные, проверить значения атрибутов, вызвать методы экземпляров).
"""


class Worker:
    def __init__(self, surname, name, patronymic, position, wage, bonus):
        self.surname = surname
        self.name = name
        self.patronymic = patronymic
        self.position = position
        self.wage = wage
        self.bonus = bonus
        self.__income = {'wage': self.wage, 'bonus': self.bonus}


class Position(Worker):
    def get_full_name(self):
        return f'Фамилия Имя Отчество: {self.surname} {self.name} {self.patronymic}\nДолжность: {self.position}'

    def get_total_income(self):
        return f'Доход сотрудника с учетом премии: {sum(self._Worker__income.values())}\nОклад: {self.wage}\nПремия: {self.bonus}'


process_engineer = Position('Глухарев', 'Олег', 'Анатольевич', 'инженер-технолог, programmer', 386842, 21355)

print(f'{Position.get_full_name(process_engineer)}\n{Position.get_total_income(process_engineer)}')

"""4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
speed, color, name, is_police (булево). А также методы: go, stop, turn(direction), 
которые должны сообщать, что машина поехала, остановилась, повернула (куда). 
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и
40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат. 
Выполните вызов методов и также покажите результат.
"""


class Car:
    def __init__(self, name, color, speed, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'Автомобиль {self.name} поехал\n{self.show_speed()}'

    def stop(self):
        self.speed = 0
        return f'Автомобиль {self.name} остановился\n{self.show_speed()}'

    def turn(self, direction):
        direction_list = ['вперед', 'вправо', 'назад', 'влево', 'forward', 'right', 'back', 'left']
        try:
            if str(direction).lower() in direction_list:
                self.direction = direction
            else:
                self.direction = FileNotFoundError
        except FileNotFoundError:
            return f'Вы ввели недопустимое направление список направлений:\n {direction_list}'

        return f'Автомобиль {self.name} повернул по направлению: {self.direction}\n{self.show_speed()}'

    def show_speed(self):
        return f'Скорость автомобиля {self.name} составляет {self.speed}'


class TownCar(Car):
    def show_speed(self, speed_limit=60):
        if self.speed > speed_limit:
            return f'Ваш автомобиль {self.name}\nпревысил скорость на {self.speed - speed_limit} км/ч'
        else:
            return f'Скорость автомобиля {self.name} составляет {self.speed}'


class SportCar(Car):
    def show_speed(self):
        self.speed = self.speed + 50
        return f'Скорость автомобиля {self.name} составляет {self.speed} это SportCar +50 к скорости)))'


class WorkCar(Car):
    def show_speed(self, speed_limit=40):
        if self.speed > speed_limit:
            return f'Ваш автомобиль {self.name}\nпревысил скорость на {self.speed - speed_limit} км/ч'
        else:
            return f'Скорость автомобиля {self.name} составляет {self.speed}'


class PoliceCar(Car):
    def __init__(self, name, color, speed, is_police=True, speed_limit=60):
        super().__init__(name, color, speed,)
        self.is_police = is_police
        self.speed_limit = speed_limit

    def catch_a_criminal(self):
        from math import inf
        self.speed_limit = inf
        return f'Преступник обнаружен ограничение скорости снято: {self.speed_limit}'


t_car1 = TownCar('Lada', 'Black', 50)
print(f'{t_car1.name}\n{t_car1.speed}\n{t_car1.is_police}\n{t_car1.color}')
print(f'{t_car1.show_speed()}\n{t_car1.go()}\n{t_car1.turn("right")}\n{t_car1.stop()}\n')

t_car2 = TownCar('Lada', 'Black', 80)
print(f'{t_car2.name}\n{t_car2.speed}\n{t_car2.is_police}\n{t_car2.color}')
print(f'{t_car2.show_speed()}\n{t_car2.go()}\n{t_car2.turn("left")}\n{t_car2.stop()}\n')

w_car1 = WorkCar('Truck', 'White', 30)

print(f'{w_car1.name}\n{w_car1.speed}\n{w_car1.is_police}\n{w_car1.color}')
print(f'{w_car1.show_speed()}\n{w_car1.go()}\n{w_car1.turn("back")}\n{w_car1.stop()}\n')

w_car2 = WorkCar('Truck', 'Black', 60)

print(f'{w_car2.name}\n{w_car2.speed}\n{w_car2.is_police}\n{w_car2.color}')
print(f'{w_car2.show_speed()}\n{w_car2.go()}\n{w_car2.turn("forward")}\n{w_car2.stop()}\n')

s_car = SportCar('Dodge Viper', 'Dark Grey', 180)
print(f'{s_car.name}\n{s_car.speed}\n{s_car.is_police}\n{s_car.color}')
print(f'{s_car.show_speed()}\n{s_car.go()}\n{s_car.turn("right")}\n{s_car.stop()}\n')

p_car = PoliceCar('Chevrolet Camaro', 'While-Red', 200)
print(f'{p_car.name}\n{p_car.speed}\n{p_car.is_police}\n{p_car.color}')
print(f'{p_car.show_speed()}\n{p_car.go()}\n{p_car.turn("right")}\n{p_car.stop()}\n{p_car.catch_a_criminal()}\n')

"""5. Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и 
метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка),
Pencil (карандаш), Handle (маркер). В каждом из классов реализовать переопределение метода draw. 
Для каждого из классов методы должен выводить уникальное сообщение. Создать экземпляры классов и проверить, 
что выведет описанный метод для каждого экземпляра.
"""


class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return f'Запуск отрисовки'


class Pen(Stationery):
    def draw(self):
        return f'Отрисовки ручкой сложно стереть, рисуйте хорошо)'


class Pencil(Stationery):
    def draw(self):
        return f'Можно рисовать что угодно всегда есть ластик)'


class Handle(Stationery):
    def draw(self):
        return f'Отрисовка маркером не стерается, будьте осторожны'


pen = Pen('Ручка')
print(pen.draw())

pencil = Pencil('Карандаш')
print(pencil.draw())

handle = Handle('Маркер')
print(handle.draw())
