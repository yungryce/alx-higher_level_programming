#!/usr/bin/python3
"""class MyInt that inherits from int:"""


class MyInt(int):
    """subclass of builtin int"""
    def __eq__(self, other):
        """
        Invert the behavior of == 
        return int(self) != other
        """
        return not super().__eq__(other)

    def __ne__(self, other):
        """ Invert the behavior of != """
        return not super().__ne__(other)
