# class Rectangle:
#     def __init__(self, x, y, width, height):
#         self.x = x
#         self.y = y
#         self.width = width
#         self.height = height
#     def __str__(self):
#         return f'Rectangle: {self.x}, {self.y}, {self.width}, {self.height}'
#
# s = Rectangle(5,10,50,100)
# print(s.__str__())

# class Rectangle:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#     def getArea(self):
#         return self.a * self.b
#
# figure = Rectangle(12, 45)
#
# print('Площадь фигуры равна', figure.getArea())

class Customers:
    def __init__(self, name, surname, city, balance):
        self.name = name
        self.surname = surname
        self.city = city
        self.balance = balance

    def __str__(self):
        a = str(self.name).capitalize()
        return f'{a} {self.surname}. Город {self.city}. Баланс: {self.balance} руб.'

    def get_guest(self):
        return f'{self.name} {self.surname}. Город {self.city}.'


# customer_1 = Customers('ИВан', 'Петров', 'Москва', 100)
# print(customer_1)

customer_1 = Customers('Иван', 'Петров', 'Москва', 200)
customer_2 = Customers('Максим', 'Казанцев', 'Воронеж', 500)

guests = [customer_1, customer_2]

for i in guests:
    print(i.get_guest())
