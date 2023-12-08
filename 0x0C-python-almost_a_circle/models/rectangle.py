#!/usr/bin/python3
"""class Rectangle that inherits from Base"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class that inherits from a base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialize a new Rectangle.
        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
            x (int): The x coordinate of the new Rectangle.
            y (int): The y coordinate of the new Rectangle.
            id (int): The identity of the new Rectangle.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Get/set the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Get/set the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Set/get the x coordinate of the Rectangle"""
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Set/get the y coordinate of the Rectangle"""
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """area of a Rectangle"""
        return self.__width * self.__height

    def display(self):
        """Print the Rectangle using the `#` character."""
        if self.__width == 0 or self.__height == 0:
            print("")
            return
        for _ in range(self.__y):
            print()
        for _ in range(self.__height):
            result = ' ' * self.__x
            print(result + '#' * self.__width)

    def update(self, *args, **kwargs):
        """
        Method that update arguments for square object
        Args:
           *args: list of arguments.
           **kwargs: Dictionary of the arguments.
        """
        allowed_keys = ['id', 'width', 'height', 'x', 'y']
        if args and args is not None:
            for i, value in enumerate(args):
                setattr(self, allowed_keys[i], value)
        elif kwargs:
            for key, value in kwargs.items():
                if key in allowed_keys:
                    setattr(self, key, value)
                else:
                    pass

    def to_dictionary(self):
        """Return the dictionary representation of the Square."""
        allowed_keys = ['id', 'width', 'height', 'x', 'y']
        return {key: getattr(self, key) for key in allowed_keys}

    def __str__(self):
        """Return the print() and str() representation of the Rectangle."""
        return (f"[Rectangle] ({self.id}) {self.x}/{self.y} - \
                {self.width}/{self.height}")
