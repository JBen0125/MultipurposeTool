"""
Classes:

        Algepy

Functions:

        quadratic_formula(a, b, c)                              # Used
        vertex(a, b, c)                                         # Used
        area(shape, l, w, h, r, b, s)                           # Used
        cosine(x)                                               # Used
        sine(y)                                                 # Used
        dot_product(a, b, c, d)                                 # Used
        magnitude(ax, by)                                       # Used
        derivative(x, n)                                        # Used
        synthetic_division(degree, divisor)                     # Used
        foil(a, b, x, y)                                        # Used
        euclidD(point1, point2)                                 # Used
        create_complex_number(a, b)                             # Used
        complex_number_multiplication(a, b, multiplier)         # Used
        complex_number_real(a, b)                               # Used
        complex_number_imaginary(a, b)                          # Used
        complex_number_absolute_value(a, b)                     # Used
        complex_number_multiplication_foil(a, b, x, y)          # Used
        matrices_dot_product(a, b, c, d, w, x, y, z)            # Used
        matrices_addition(a, b, c, d, w, x, y, z)               # Used
        matrices_subtration(a, b, c, d, w, x, y, z)             # Used
        matrices_multiply(a, b, c, d, w, x, y, z)               # Used
        matrices_divide(a, b, c, d, w, x, y, z)                 # Used

Objects:

        None

Description:

        This module includes the basic functions of algebra-related courses, which includes but isn't limited
        to, Algebra, Geometry, Calculus, Trigonometry and Linear Algebra.
        
"""

import math as m
import matplotlib.pyplot as mpl
import numpy as np
from discretemath import *


# Magnitude
def magnitude(ax, by):
    """
    This function finds the magnitude.

    (ax, by: int) -> float

    returns magnitude

    >>> magnitude(3, 4)
    5.0
    """
    mag = m.sqrt(m.pow(ax, 2) + m.pow(by, 2))
    return mag


# Quadratic Calculator
def quadratic_formula(a, b, c):
    """
    This function uses the parameters a, b and c to find the Quadratic Formula.

    (a, b and c: int) -> tuple

    returns Qf1, Qf2

    >>> quadratic_formula(1, 0, -4)
    (2.0, -2.0)
    """
    y = (int(m.pow(b, 2))) - (int(4) * int(a) * int(c))
    qf1 = (-int(b) + m.sqrt(y))/(int(2) * int(a))
    qf2 = (-int(b) - m.sqrt(y))/(int(2) * int(a))
    return qf1, qf2


# Vertex Formula
def vertex(a, b, c):
    """
    This function finds the vertex of a quadratic function using a, b and c.

    (a, b and c: int) -> tuple

    returns vertex, QE

    >>> vertex(1, 0, -4)
    (0.0, -4)
    """
    v = (-int(b))/(int(2) * int(a))
    qe = int((a) * (v) ** 2) + int(b * v) + int(c)
    return v, qe


# Area Formula
def area(shape, l, w, h, r, b, s):
    """
    This function finds the area of a shape.

    (shape: str, l, w, h, r, b, s: int) -> float

    returns a

    >>> area("Square", 0, 0, 0, 0, 0, 6)
    36.0
    """
    if shape == "Circle":
        a = m.pow(m.pi * int(r), 2) 
        return a
    if shape == "Triangle":
        a = int(b) * int(h) / 2
        return a
    if shape == "Square":
        a = m.pow(int(s), 2)
        return a


# Cosine
def cosine(x):
    """
    This function finds cosine of an angle in degrees and radians.

    (x: int) -> tuple

    returns r, d

    >>> cosine(90)
    (-0.4480736161291701, 0.0)
    """
    r = m.cos(x)
    d = round(m.cos(x * 2 * m.pi / 360), 4)
    return r, d


# Sine
def sine(y):
    """
    This function finds sine of an angle in degrees and radians.

    (x: int) -> tuple

    returns r, d

    >>> sine(90)
    (0.8939966636005579, 1.0)
    """
    r = m.sin(y)
    d = round(m.sin(y * 2 * m.pi / 360), 4)
    return r, d


# Dot Product
def dot_product(a, b, c, d):
    """
    This function finds the dot product using a, b, c and d.

    (a, b, c, d: int) -> int

    returns vw

    >>> dot_product(1, 2, 3, 4)
    11
    """
    vw = (a * c) + (b * d)
    return vw


# Derivative Power Rule
def derivative(x, n):
    """
    This function uses the power rule to find the derivative.

    (x, n: int) -> tuple

    returns der_variable, der_exponent

    >>> derivative(3, 4)
    (12, 3)
    """
    der_variable = n * x
    der_exponent = n - 1
    return der_variable, der_exponent


# Synthetic Division
def synthetic_division(degree, divisor):
    """
    This function finds synthetic division using the degree and the divisor.

    Ex: if you are trying to perform synthetic division for (x^4 + x^3 - 11x^2 - 5x + 30) and (x - 2),
    your degree would be 4, since it is the highest degree in the equation, and your divisor would be 2, since you are
    dividing it by (x - 2).

    (degree, divisor: int) -> list and dictionary encapsulated into a tuple

    returns e_dict, li

    > synthetic_division(4, 2)
    ({4: 1, 3: 1, 2: -11, 1: -5, 0: 30}, [1, 3, -5, -15, 0])
    """
    li = []
    e_dict = {}
    multiplier = 0
    for i in range(degree + 1):
        degree = degree
        x_i = int(input("Enter the {0} coefficient: ".format(degree)))
        degree -= 1
        e_dict[degree + 1] = x_i
        if i == 0:
            li.append(x_i)
            x_i_p = x_i 
        else:
            multiplier = x_i + divisor * x_i_p
            li.append(multiplier)
            x_i_p = multiplier
    # Divide, Multiply, Subtract, Bring Down
    return e_dict, li


# Polynomial Foil
def foil(a, b, x, y):
    """
    This function foils two polynomials that are in the form (x +/- a)(y +/- b).

    (a, b: int) -> poly1d

    returns f

    >>> foil(2, -2, 1, 1)
    poly1d([ 1,  0, -4])
    """
    p = np.poly1d([x, a])
    q = np.poly1d([y, b])
    f = p * q
    return f


# Euclidean Distance
def euclidD(point1, point2):
    """
    This function finds distance between two points, or in our case, lists.
        
    (point1, point2: list) -> float

    returns euclidDistance

    >>> euclidD([3, 0], [0, 4])
    5.0
    """
    total = 0
    for index in range(len(point1)):
        diff = (point1[index] - point2[index]) ** 2
        total += diff
    euclidDistance = m.sqrt(total)
    return euclidDistance


# Complex Number Operators a+bj
def create_complex_number(a, b):
    """
    This function creates a complex number with a and b.

    (a, b: int) -> complex

    returns x

    >>> create_complex_number(1, 2)
    (1+2j)
    """
    x = complex(a, b)
    return x


# Complex Number Multiplication by a Multiplier
def complex_number_multiplication(a, b, multiplier):
    """
    This function multiplies a complex number by a multiplier.

    (a, b and multiplier: int) -> complex

    returns y

    >>> complex_number_multiplication(1, 2, 3)
    (3+6j)
    """
    x = complex(a, b)
    y = x * multiplier
    return y


# Complex Number Real Part
def complex_number_real(a, b):
    """
    This function returns the real part of a complex number.

    (a, b: int) -> int

    returns y

    >>> complex_number_real(1, 2)
    1
    """
    x = complex(a, b)
    y = x.real
    y = int(y)
    return y


# Complex Numnber Imaginary Part
def complex_number_imaginary(a, b):
    """
    This function returns the imaginary part of a complex number.

    (a, b: int) -> int

    returns y

    >>> complex_number_imaginary(1, 2)
    2
    """
    x = complex(a, b)
    y = x.imag
    y = int(y)
    return y


# Complex Number Absolute Value
def complex_number_absolute_value(a, b):
    """
    This function returns the absolute value of the complex number (a+bj).

    (a, b: int) -> float

    returns c

    >>> complex_number_absolute_value(3, 4)
    5.0
    """
    c = magnitude(a, b)
    c = abs(c)
    return c


# Complex Number Multiplication Foil
def complex_number_multiplication_foil(a, b, x, y):
    """
    This function multiplies two complex numbers together using the FOIL method.

    (a, b, x and y: int) -> complex

    returns f

    >>> complex_number_multiplication_foil(3, 6, 4, 7)
    (-30+45j)
    """
    p = complex(a, b)
    q = complex(x, y)
    f = p * q
    return f


# Matrices Dot Product
def matrices_dot_product(a, b, c, d, w, x, y, z):
    """
    This function does the matrices dot product.

    returns None
    """
    X = np.array([[a, b], [c, d]])
    Y = np.array([[w, x], [y, z]])
    print(np.dot(X, Y))


# Matrices Addition
def matrices_addition(a, b, c, d, w, x, y, z):
    """
    This function does matrices addition.

    returns None
    """
    X = np.array([[a, b], [c, d]])
    Y = np.array([[w, x], [y, z]])
    print(np.add(X, Y))


# Matrices Subtraction
def matrices_subtration(a, b, c, d, w, x, y, z):
    """
    This function does matrices subtraction.

    returns None
    """
    X = np.array([[a, b], [c, d]])
    Y = np.array([[w, x], [y, z]])
    print(np.subtract(X, Y))


# Matrices Multiplication
def matrices_multiply(a, b, c, d, w, x, y, z):
    """
    This function does matrices multiplication.

    returns None
    """
    X = np.array([[a, b], [c, d]])
    Y = np.array([[w, x], [y, z]])
    print(np.multiply(X, Y))


# Matrices Division
def matrices_divide(a, b, c, d, w, x, y, z):
    """
    This function does the matrices division.

    returns None
    """
    X = np.array([[a, b], [c, d]])
    Y = np.array([[w, x], [y, z]])
    print(np.divide(X, Y))


if __name__ == "__main__":
    matrices_divide(1, 2, 3, 4, 5, 6, 7, 8)
