# Создать класс Point2D. Координаты точки задаются 2 параметрами - координатами x, y на плоскости.
# Реализовать метод distance который принимает экземпляр класса Point2D и рассчитывает расстояние между 2мя точками на плоскости.
# Создать защищенный атрибут класса - счетчик созданных экземпляров класса.
# Чтение количества экземпляров реализовать через метод getter.
# Создать класс Point3D, который является наследником класса Point2D. Координаты точки задаются 3 параметрами - координатами x, y, z в пространстве.
# Переопределить конструктор с помощью super().
# Переопределить метод distance для определения расстояния между 2-мя точками в пространстве.

class Point2D:
    __coint_attribute = 0

    @classmethod
    def getter(cls):
        return cls.__coint_attribute

    def __init__(self, x, y):
        self.x = x
        self.y = y
        Point2D.__coint_attribute += 1

    def distance(self, other_point):
        return ((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2) ** 0.5

class Point3D(Point2D):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

    def distance(self, other_point):
        return ((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2 + (self.z - other_point.z)) ** 0.5

p1 = Point2D(10, 20)
print(p1.getter())
p2 = Point2D(100, 200)
p3 = Point3D(100, 100, 100)
print(p3.getter())
p4 = Point3D(2, 3, 5)

print(p1.distance(p2))
print(p3.distance(p4))










