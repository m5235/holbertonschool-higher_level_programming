#!/usr/bin/python3
class Square:
    """
    class of size
    """

    def __init__(self, size=0):
        """square class constructor.
        """

        self.size = size

    @property
    def size(self):
        """def size from class.
        """

        return self.__size

    @size.setter
    def size(self, value):
        """square size setter.
        """

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Calculates the square area.
        """

        return self.__size * self.__size
