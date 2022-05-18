# Создать класс дробь(Fraction), конструктор которого принимает целые числа (num, den - числитель(numerator), знаменатель(denominator) ).
# Выполнить
# Атрибуты числитель и знаменатель в классе сделать приватными. Доступ к атрибутам реализовать через свойства.
# Переопределить методы __sub__, __add__, __mull__, __truediv__ для того, чтобы можно было выполнять соответствующие математические действия с объектами класса дробь.
# (Вычитание, сложение, умножение и деление).
# Добавить класс миксин, в котором реализовать статические методы, для этих же операций(add, sub, mull, div). Добавить класс миксин в класс Fraction
# Создать classmethod который из строки типа 'числитель/знаменатель' возвращает объект класса дробь.
# Переопределить метод __str__, который при выводе объекта на печать будет выводить строку вида num / den.
# Создать объекты класса дробь.
# Выполнить все реализованные методы.

class FranctionWithMixin():

    @staticmethod
    def sub():
        pass

    @staticmethod
    def add():
        pass

    @staticmethod
    def mull():
        pass

    @staticmethod
    def truediv():
        pass



class Franction():
    def __init__(self, num: int, den: int):
        self.__num = num
        self.__den = den

    @property
    def num(self):
        return self.__num

    @property
    def den(self):
        return self.__den

    @num.setter
    def num(self, num):
        self.__num = num

    @den.setter
    def den(self, den):
        self.__den = den

    @classmethod
    def change(cls, str):
        diff = str.split('/')
        return Franction(int(diff[0]), int(diff[1]))

    def add(self):
        return self.__num + self.__den

    def sub(self):
        return self.__num - self.__den

    def mull(self):
        return self.__den * self.__num

    def truediv(self):
        return self.__num // self.__den

    def str(self):
        return f'{self.__num} / {self.__den}'

t = Franction(4, 2)
print(t.str())
print(t.den)
print(t.num)
t.den = 2
t.num = 6
print(t.add())
print(t.sub())
print(t.mull())
print(t.truediv())
print(t.change('6/4'))



