# Доп*
# 4. В отдельном файле напишите программу с классом Car.
# a. Создайте конструктор класса Car. Создайте атрибуты класса Car — color (цвет), type (тип), year (год).
# b. Напишите пять методов.
# i. Первый — запуск автомобиля, при его вызове выводится сообщение «Автомобиль заведен».
# ii. Второй — отключение автомобиля — выводит сообщение «Автомобиль заглушен».
# iii. Третий — присвоение автомобилю года выпуска. Четвертый метод — присвоение автомобилю типа.
# iv. Пятый — присвоение автомобилю цвета.

class Car:

    def __init__(self, color=None, type=None, year=None):
        self.color = color
        self.type = type
        self.year = year

    def launch(self):
        print('Автомобиль заведен')

    def disabling(self):
        print('Автомобиль заглушен')

    def age(self):
        self.year=input("Введите год выпуска: ")
        print(self.year)

    def model(self):
        self.type = input("Введите тип машины: ")
        print(self.type)

    def colour(self):
        self.color = input("Введите цвет машины: ")
        print(self.color)

machine=Car()
machine.launch()
machine.disabling()
machine.age()
machine.model()
machine.colour()
