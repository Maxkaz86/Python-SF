from task1682 import Rectangle, Square, Circle

rect_1 = Rectangle(3,4)
rect_2 = Rectangle(12,5)

# print(rect_1.get_area())
# print(rect_2.get_area())

square_1 = Square(5)
square_2 = Square(10)

# print(square_1.getSquareArea(), square_2.getSquareArea())
circle_1 = Circle(3)
circle_2 = Circle(13)

figures = [rect_1,rect_2,square_1,square_2, circle_1, circle_2]
for figure in figures:
    if isinstance(figure,Square):
        print(figure.getSquareArea())
    elif isinstance(figure, Circle):
        print(round(figure.getCircleArea(), 2))
    else:
        print(figure.getArea())