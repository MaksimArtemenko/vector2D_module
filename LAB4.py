import math


class Vector2D:
    """
    A class that represents a 2D vector with support for
    operations like addition, subtraction, scalar multiplication, etc.
    """

    def __init__(self, x: float, y: float):
        """
        Initializes a 2D vector with coordinates x and y.

        :param x: X coordinate (must be a number: integer or float).
        :param y: Y coordinate (must be a number: integer or float).
        :raises TypeError: If x or y are not numbers.
        """
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError("Coordinates x and y must be numbers.")
        self.__x = float(x)
        self.__y = float(y)

    def __str__(self):
        """
        Returns the string representation of the vector.

        :return: A string in the format 'Vector2D(x, y)'.
        """
        return f"Vector({self.__x}, {self.__y})"

    def __add__(self, other):
        """
        Adds two vectors.

        :param other: Another instance of Vector2D to add.
        :return: A new instance of Vector2D as the result of the sum.
        :raises TypeError: If the other object is not a Vector2D instance.
        """
        if not isinstance(other, Vector2D):
            raise TypeError("Addition is only possible between instances of Vector2D.")
        return Vector2D(self.__x + other.__x, self.__y + other.__y)

    def __sub__(self, other):
        """
        Subtracts one vector from another.

        :param other: Another instance of Vector2D to subtract from.
        :return: A new instance of Vector2D as the result of the subtraction.
        :raises TypeError: If the other object is not a Vector2D instance.
        """
        if not isinstance(other, Vector2D):
            raise TypeError("Subtraction is only possible between instances of Vector2D.")
        return Vector2D(self.__x - other.__x, self.__y - other.__y)

    def __mul__(self, scalar):
        """
        Multiplies a vector by a scalar.

        :param scalar: The number to multiply by.
        :return: A new instance of Vector2D with scaled coordinates.
        :raises TypeError: If the scalar is not a number.
        """
        if not isinstance(scalar, (int, float)):
            raise TypeError("Multiplication is only possible with a numeric value.")
        return Vector2D(self.__x * scalar, self.__y * scalar)

    def magnitude(self):
        """
        Calculates the magnitude (length) of the vector.

        :return: The magnitude of the vector as a float.
        """
        return math.sqrt(self.__x ** 2 + self.__y ** 2)

    def dot_product(self, other):
        """
        Calculates the dot product of two vectors.

        :param other: Another instance of Vector2D.
        :return: The dot product as a float.
        :raises TypeError: If the other object is not a Vector2D instance.
        """
        if not isinstance(other, Vector2D):
            raise TypeError("A second instance of Vector2D is required for computation.")
        return self.__x * other.__x + self.__y * other.__y


if __name__ == "__main__":

    try:
        v1 = Vector2D(3, 4)
        v2 = Vector2D(1.4, 2)
        v3 = Vector2D(4, 0)

        print("v1:", v1)
        print("v2:", v2)
        print("Magnitude v1:", round(v1.magnitude(), 2))
        print("Dot product v1 and v2:", v1.dot_product(v2))

        print("v1 + v2:", v1 + v2)
        print("v1 - v2:", v1 - v2)
        print("v1 * 3:", v1 * 3)

    except Exception as e:
        print("Error:", e)
