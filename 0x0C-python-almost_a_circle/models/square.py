#!/usr/bin/python3
"""class Square that inherits from Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """defines a square class"""
    def __init__(self, size, x=0, y=0, id=None):
        """
        Args:
            size (int): The size of the new Square.
            x (int): The x coordinate of the new Square.
            y (int): The y coordinate of the new Square.
            id (int): The identity of the new Square.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get/set the width of the square"""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Method that update arguments for square object
        Args:
           *args: list of arguments.
           **kwargs: Dictionary of the arguments.
        """
        allowed_keys = ['id', 'size', 'x', 'y']
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
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """Return the print() and str() representation of the Rectangle."""
        return (f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}")
