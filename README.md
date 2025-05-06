# Vector2D 

`Vector2D` is a Python module for working with two-dimensional vectors. It supports basic operations like addition, subtraction, scalar multiplication, computing magnitude, and calculating the dot product.

---

##  Description

The `Vector2D` module allows you to create objects representing 2D vectors and perform basic vector operations with them.

**Key Features:**
- [X] Create vectors with given coordinates.
- [X] Compute the magnitude (length) of a vector.
- [X] Calculate the dot product of two vectors.
- [X] Perform vector addition and subtraction.
- [X] Multiply a vector by a scalar.

---

## Instructions for Methods
1. ## Vector Initialization
```py
__init__(self, x, y)
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError("Coordinates x and y must be numbers.")
        self.__x = float(x)
        self.__y = float(y)
```
**Purpose**:
Initializes a new vector with two specified coordinates.

**How to use**:
Provide two numbers (X and Y) during object initialization.
If you provide non-numeric values, an error will be raised.

**Example**:
```py
v1 = Vector2D(3, 4)
print("v1:", v1)

v1: Vector(3.0, 4.0)
```

2. ## Returns the string representation of the vector
```py
def __str__(self):
    return f"Vector({self.__x}, {self.__y})"
```
**Purpose**:
Returns a nicely formatted string representation of the vector when printed.

**How to use**:
Print the object directly to get its coordinates displayed.

**Example**:
```py
v = Vector2D(1, 1)
print(v)
```
### Output:
```py
Vector(1.0, 1.0)
```

3. ## Add two vectors
```py
def __add__(self, other):
    if not isinstance(other, Vector2D):
        raise TypeError("Addition is only possible between instances of Vector2D.")
    return Vector2D(self.__x + other.__x, self.__y + other.__y)
```
**Purpose**:
Adds two vectors coordinate-wise.

**How to use**:
Use the ```+``` operator between two Vector2D instances.

**Example**:
```py
v1 = Vector2D(3, 4)
v2 = Vector2D(1.4, 2)
print("v1 + v2:", v1 + v2)
```
### Output:
```py
v1 + v2: Vector(4.4, 6.0)
```

4. ## Subtracts one vector from another
```py
    def __sub__(self, other):
        if not isinstance(other, Vector2D):
            raise TypeError("Subtraction is only possible between instances of Vector2D.")
        return Vector2D(self.__x - other.__x, self.__y - other.__y)
```
**Purpose**:
    Subtracts one vector from another coordinate-wise.

**How to use**:
Use the ```-``` operator between two Vector2D instances.
```py
    v1 = Vector2D(3, 4)
    v2 = Vector2D(1.4, 2)
    print("v1 - v2:", v1 - v2)
```
### Output:
```py
    v1 - v2: Vector(1.6, 2.0)
```
5. ## Multiplies a vector by a scalar
```py
def __mul__(self, scalar):
    if not isinstance(scalar, (int, float)):
        raise TypeError("Multiplication is only possible with a numeric value.")
    return Vector2D(self.__x * scalar, self.__y * scalar)
```
**Purpose**:
Multiplies the vector by a scalar value (a number), scaling its size without changing its direction.

**How to use**:
Multiply a ```Vector2D``` instance by a number using the ```*``` operator.

Example:
```py
v1 = Vector2D(3, 4)
print("v1 * 3:", v1 * 3)
```
## Output:
```py
v1 * 3: Vector(9.0, 12.0)
```

6. ## Calculates the magnitude (length) of the vector
```py
def magnitude(self):
    return math.sqrt(self.__x ** 2 + self.__y ** 2)
```
**Purpose**:
Calculates the magnitude (length) of the vector from the origin.

**How to use**:
Call the ```.magnitude()``` method on a vector.

Example:
```py
v1 = Vector2D(3, 4)
print("Magnitude v1:", round(v1.magnitude(), 2))
```
## Output:
```py
Magnitude v1: 5.0
```

7. ## Calculates the dot product of two vectors
```py
def dot_product(self, other):
    if not isinstance(other, Vector2D):
        raise TypeError("A second instance of Vector2D is required for computation.")
    return self.__x * other.__x + self.__y * other.__y
```
**Purpose**:
Calculates the dot product between two vectors 

**How to use**:
Call ```.dot_product()``` and pass another Vector2D object as an argument.

**Example**:
```py
v1 = Vector2D(3, 4)
v2 = Vector2D(1.4, 2)
print("Dot product v1 and v2:", v1.dot_product(v2))
```
## Output: 
```py
Dot product v1 and v2: 12.2
```

## :x: Table of Errors (Possible Errors)
| Method | Possible Error | Description |
| ------ | -------------- | ----------- |
|```__init__(x,y)```|:red_circle:```TypeError```| If x or y are not numbers |
|```__add__(other) and __sub__(other)```|:red_circle:```TypeError```|If the other object is not a Vector2D instance|
|```__mul__(scalar)```|:red_circle:```TypeError```|If the scalar is not a number|
|```dot_product(other)```|:red_circle:```TypeError```|If the other object is not a Vector2D instance|

# Author
***Artemenko Maksim ,11IPZ ,student UDU Dragomanova***


![oYQBIq3xLBAnARmgWAi0iIzL3CcAdA99Ebfzoi](https://github.com/user-attachments/assets/e2cc082f-8b0c-4b68-b0ec-8b366110aa43)

