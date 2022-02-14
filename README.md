# MultiPurposeTool

This multipurpose tool is an user input based program, it has multiple purposes, hence it's name, 
a few things that it can do include running the quadratic formula, ackermann's algorithm, handshaking 
theorem, and more, it does all this based off of user input.

## Created Libraries

- discretemath - Includes functions such as Binomial Theorem, Prime 
  Factorization, GCD, LCM, Boolean Algebra, Handshaking Theorem and more
- algepy - Includes functions such as Quadratic Formula, Area, Dot Product,
  Synthetic Division and more
- mini_games - Includes functions Coin Flip and Roll Dice
- encrypti - Includes functions Caesar Cipher, Binary Translator and
  Hexadecimal Translator
- list_functions - Includes functions Sort, Sum, Mean, Median and Mode

### algepy.py

- **procedure magnitude(ax, by)** - This function finds the magnitude, it
takes two arguments, namely ax and by, which are both integers, and the 
  output is a floating-point integer.
  
- **procedure quadraticFormula(a, b, c)** - This function finds the quadratic
formula, it takes three arguments, namely a, b and c, which are all integers,
  and the output is a 2d tuple that is the negative and positive answers.
  
- **procedure vertex(a, b, c)** - This function finds the vertex, it takes 
three arguments, namely a, b and c, which are all integers, and the output
  is a 2d tuple in the form (x, y), which correspond to the x and y
  coordinates of the vertex.
  
- **procedure area(shape, l, w, h, r, b, s)** - This function finds the area
of a shape using its dimensions. **NOTE: Square, Triangle and Circle are
  currently the only defined shapes**
  
- **procedure cosine(x)** - This function does the cosine of x and returns
the answer in radians and degrees as a tuple.
  
- **procedure sine(y)** - This function does the sine of y and returns the
answer in radians and degrees as a tuple.
  
- **procedure dotProduct(a, b, c, d)** - This function finds the dot product
from the arguments, a, b, c and d, returns an integer.
  
- **procedure derivative(x, n)** - This function uses the leading coefficient
of x, here it is called x, and the degree of x, here it is called n, and
  returns the leading coefficient and the degree of the derivative as a
  tuple.
  
- **procedure syntheticDivision(degree, divisor)** - This function finds the
synthetic division using the degree and the divisor, it prints a list and
  dictionary encapsulated in a tuple, where the list is the polynomials
  leading terms after synthetic division.
  
- **procedure FOIL(a, b, x, y)** - This function computes the foil method
given a problem in the form (x +/- a)(y +/- b), and returns a polynomial.
  
- **procedure euclideanDistance(point1, point2)** - This function computes
the Euclidean Distance from the points, point1 and point2 and returns the
  distance
  
- **procedure createComplexNumber(a, b)** - This function creates a 
complex number given two integers, a and b.
  
- **procedure complexNumberMultiplication(a, b, multiplier)** - This 
  function creates a complex number and multiplies it by the multiplier.
  
- **procedure complexNumberReal(a, b)** - This function returns the real
  part of the complex number.
  
- **procedure complexNumberImaginary(a, b)** - This function returns 
  the imaginary part of the complex number.
  
- **procedure complexNumberAbsoluteValue(a, b)** - This function returns the
absolute value of a complex number
  
- **procedure complexNumberMultiplicationFOIL(a, b, x, y)** - This function
returns the multiplication of two complex numbers using foil.
  
- **procedure matricesDotProduct(a, b, c, d, w, x, y, z)** - This function
prints the matrix dot product of two matrices. **NOTE: The matrix functions
  all take in two 2x2 matrices, so the amount of work these functions can
  do are limited to 2x2 matrices**
  
- **procedure matricesAddition(a, b, c, d, w, x, y, z)** - This function
prints the matrix addition of two matrices.
  
- **procedure matricesSubtraction(a, b, c, d, w, x, y, z)** - This function
prints the matrix subtraction of two matrices.
  
- **procedure matricesMultiply(a, b, c, d, w, x, y, z)** - This function
prints the matrix multiplication of two matrices.
  
- **procedure matricesDivide(a, b, c, d, w, x, y, z)** - This function prints
the matrix division of two matrices.
  
### discretemath.py