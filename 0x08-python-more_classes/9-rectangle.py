#!/usr/bin/python3
"""
module "4-rectangle"
"""


class Rectangle:
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        init method
        no example
        """
        if type(width) == int:
            if width >= 0:
                self.__width = width
            else:
                raise ValueError("width must be >= 0")
        else:
            raise TypeError("width must be an integer")
        if type(height) == int:
            if height >= 0:
                self.__height = height
            else:
                raise ValueError("height must be >= 0")
        else:
            raise TypeError("height must be an integer")
        type(self).number_of_instances += 1

    @property
    def width(self):
        """
        width getter
        """
        return self.__width

    @property
    def height(self):
        """
        height getter
        """
        return self.__height

    @width.setter
    def width(self, value):
        """
        width setter
        """
        if type(value) == int:
            if value >= 0:
                self.__width = value
            else:
                raise ValueError("width must be >= 0")
        else:
            raise TypeError("width must be an integer")

    @height.setter
    def height(self, value):
        """
        height setter
        """
        if type(value) == int:
            if value >= 0:
                self.__height = value
            else:
                raise ValueError("height must be >= 0")
        else:
            raise TypeError("height must be an integer")

    def area(self):
        """
        get area
        """
        return self.__height * self.__width

    def perimeter(self):
        """
        get perimeter
        """
        if (self.__height) == 0 or (self.__width) == 0:
            return 0
        return ((self.__height * 2) + (self.__width * 2))

    def __str__(self):
        """
        print rectangle
        """
        strtmp = ""
        if self.__width == 0 or self.__height == 0:
            return strtmp
        else:
            for iter1 in range(self.__height):
                for iter2 in range(self.__width):
                    strtmp += str(self.print_symbol)
                if iter1 != (self.__height - 1):
                    strtmp += "\n"
        return strtmp

    def __repr__(self):
        """
        representation method
        """
        str1 = "Rectangle("
        return str1 + str(self.__width) + ", " + str(self.__height) + ')'

    def __del__(self):
        """
        finalizer method
        """
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        comparision
        """
        if rect_1.__class__.__name__ is "Rectangle":
            pass
        else:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if rect_2.__class__.__name__ is "Rectangle":
            pass
        else:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() == rect_2.area():
            return rect_1
        if rect_1.area() > rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """
        new rectangle
        """
        new_rect = Rectangle(size, size)
        return new_rect
