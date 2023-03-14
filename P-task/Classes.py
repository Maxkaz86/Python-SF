# class User:
#     pass
#
# peter = User()
# peter.name = 'Peter Robertson'
#
# julia = User()
# julia.name = 'Julia Donaldson'
#
# print(peter.name)
# print(julia.name)

# class Product:
#     def __init__(self, name, category, quantity_in_stock):
#         self.name = name
#         self.category = category
#         self.quantity_in_stock = quantity_in_stock
#
#     def is_available(self):
#         return True if self.quantity_in_stock > 0 else False
#
# eggs = Product('eggs', 'food', 5)
# print(eggs.is_available())

# ниже создали класс с конструктором
# class Event:
#     def __init__(self, timestamp = 0, event_type = '', session_id = ''):
#         self.timestamp = timestamp
#         self.type = event_type
#         self.session_id = session_id
#
#     def init_from_dict(self, event_dict):
#         self.timestamp = event_dict.get("timestamp")
#         self.type = event_dict.get("type")
#         self.session_id = event_dict.get("session_id")
# events = [
#     {
#      "timestamp": 1554583508000,
#      "type": "itemViewEvent",
#      "session_id": "0:NynteeXG:MYlskrqZbcmXNSFEJaZIsNVGeDLLpmct",
#     },
#     {
#      "timestamp": 1555296337000,
#      "type": "itemViewEvent",
#      "session_id": "0:NynteeXG:MYlskrqZbcmXNSFEJaZIsNVGeDLLpmct",
#     },
#     {
#      "timestamp": 1549461608000,
#      "type": "itemBuyEvent",
#      "session_id": "0:NynteeXG:MYlskrqZbcmXNSFEJaZIsNVGeDLLpmct",
#     },
# ]
# for event in events:
#     event_obj = Event()
#     event_obj.init_from_dict(event)
#     print(event_obj.timestamp)

# import datetime
# class Product:
#     max_quantity = 100000
#     def __init__(self, name, category, quantity_in_stock):
#         self.name = name
#         self.category = category
#         self.quantity_in_stock = quantity_in_stock
#     def is_available(self):
#         return True if self.quantity_in_stock > 0 else False
#
# class Food(Product):
#     is_critical = True
#     needs_to_be_refreshed = True
#     refresh_frequency = datetime.timedelta(days=1)
#
# eggs = Food(name="eggs", category="food", quantity_in_stock=5)
# print(eggs.max_quantity)

# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#     def getWidth(self):
#         return self.width
#     def getHeight(self):
#         return self.height
#     def getArea(self):
#         return self.width * self.height

# sides это список, в нем находятся размеры сторон
class Polygon:
    def __init__(self, no_of_sides):
        self.n = no_of_sides
        # self.sides = [0 for i in range(no_of_sides)] - это лишний код
    # теперь создадим метод для приема размера для каждой из сторон
    def inputSides(self):
        self.sides = [float(input('введите сторону ' + str(i+1) + ': ')) for i in range(self.n)]
    # теперь выводим на экран стороны
    def dispSides(self):
        for i in range(self.n):
            print('сторона', i+1, '-', self.sides[i])

class Triangle(Polygon):
    def __init__(self):
        super().__init__(3)
    def findArea(self):
        a, b, c = self.sides
        s = (a + b + c)/2
        area = (s*(s-a)*(s-b)*(s-c)**0.5)
        print('площадь треугольника', area)

t = Triangle()
t.inputSides()
t.dispSides()
t.findArea()