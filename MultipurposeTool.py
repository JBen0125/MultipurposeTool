"""
Author: Jayden Ben

Project Name: Multipurpose Tool

Description: Everyone needs help in certain areas, and this program is here to help you out.
This program can convert text to binary, generate a random number, help you with math, and so much more. 
This was originally made for Data Science but it has evolved to be much more than that.

Created: June 24th, 2020
"""

# Required libraries
import math as m
import random as rand
import os
import discretemath
import algepy
import mini_games
import encrypti
import list_functions
import sys

# Variables to be set for easy access
data = []
keys = {}
empty_str = ""


# List Commands
def commands():
    """
    prints a list of commands

    returns None
    """
    print("Data Science: D\nGenerate random number: R\nMath Commands: M\nTranslate to Binary: B"
          "\nTranslate to Hexadecimal: H\nFlip Coin: F\nRoll Dice: Roll\nFinal Grade Calculator: FGC"
          "\nLogic: Logic\nCaesar Cipher: CC")


# Final Grade Calculator
def final_grade_calculator(current, end_goal, weight_of_final):
    """
    This function figures out what score you need on the final to get the score you want.

    (current: float, end_goal, weight_of_final; int) -> float

    returns exam_grade_needed

    >>> final_grade_calculator(70, 70, 20)
    70.0
    """
    final_exam_weight = weight_of_final * 0.01
    exam_grade_needed = (end_goal - current * (1 - final_exam_weight)) / final_exam_weight
    return exam_grade_needed


# Main loop
while True:
    # Get user input
    data_input = input("\nEnter Command (empty to exit, ? for commands): ")

    # If user input is an empty str
    if data_input == empty_str:
        # Set a variable for the OS type
        operate_sys = sys.platform

        # If MacOS
        if operate_sys == "darwin":
            # Play exit sound
            os.system('afplay /System/Library/Sounds/Funk.aiff&')

        # If Linux
        elif operate_sys == "linux" or operate_sys == "linux2":
            # Play exit sound
            os.system('aplay sound2.wav&')

        # If Windows
        elif operate_sys == "win32":
            # Play no sound
            pass

        # Exit the program
        break

    # If user input is a question mark
    elif data_input == "?":
        # Print out the commands
        commands()

    # If the user input is D
    elif data_input.upper() == "D":
        # Print the data science commands
        print("\nData Science Commands: \n-----------------------\nAdd data to list: L\nPrint data: P"
              "\nAdd data to dictionary: D\nSort List: S\nSum List: +\nAverage List: A\nMedian List: M"
              "\nMode List: Mo\nReset List: R\nReset Dictionary: RD\n")

        # While in data science commands
        while True:
            # Get data science user input
            data_command_input = input("Enter a Data Science Command (empty to exit): ")

            # If data science user input is empty string
            if data_command_input == empty_str:
                # Leave data science commands
                break

            # If data science user input is 'l'
            elif data_command_input.upper() == "L":
                # While list item is not empty string
                while True:
                    # List data entries
                    add_input = input("Enter data to add to the list (empty to exit): ")
                    # If data entry is empty string
                    if add_input == empty_str:
                        break
                    # If data entry is not empty string
                    else:
                        data.append(add_input)

            # If data science user input is 'p'
            elif data_command_input.upper() == "P":
                # Print all data
                print(data)
                print(keys)

            # If data science user input is 'd'
            elif data_command_input.upper() == "D":
                # While dictionary entries are not empty strings
                while True:
                    # Get key for dictionary
                    key_input = input("\nEnter data/x-value (empty to exit): ")
                    # If key is empty string
                    if key_input == empty_str:
                        break
                    # If key is not empty string
                    else:
                        # Get value for dictionary
                        value_input = input("\nEnter data/y-value (empty to exit): ")
                        keys[key_input] = value_input

            # If data science user input is 's'
            elif data_command_input.upper() == "S":
                # Print sorted list
                print("list sorted: ", list_functions.sort_list(data))
                print()

            # If data science user input is '+'
            elif data_command_input == "+":
                # Get the sum of all elements in list
                new_li = []
                for item in data:
                    new_li.append(int(item))
                print("sum of list: ", list_functions.sum_list(new_li))
                print()

            # If data science user input is 'a'
            elif data_command_input.upper() == "A":
                # Get the average of the list
                new_li = []
                for item in data:
                    new_li.append(int(item))
                print("average of list: ", list_functions.mean_list(new_li))
                print()

            # If data science user input is 'm'
            elif data_command_input.upper() == "M":
                # Get the median of the list
                new_li = []
                for item in data:
                    new_li.append(int(item))
                print("median of list: ", list_functions.median_list(new_li))
                print()

            # If data science user input is 'Mo'
            elif data_command_input == "Mo":
                # Get the mode of the list
                new_li = []
                for item in data:
                    new_li.append(int(item))
                print("mode of list: ", list_functions.mode_list(new_li))
                print()

            # If data science user input is 'r'
            elif data_command_input.upper() == "R":
                # Reset list
                data = []
                print("List has been reset: ", data)
                print()

            # If data science user input is 'RD'
            elif data_command_input == "RD":
                # Reset dictionary
                keys = {}
                print("Dictionary has been reset: ", keys)
                print()

    # If user input is 'r'
    elif data_input.upper() == "R":
        # Generate random number
        try:
            # Get the max and min
            min_input = int(input("What is the minimum value? "))
            max_input = int(input("What is the maximum value? "))
            print(int(rand.randint(min_input, max_input)))
        except ValueError:
            print()
            continue

    # If user input is 'm'
    elif data_input.upper() == "M":
        # Print math commands
        print("\nMath Commands: \n---------------------------\nCommon Logarithm: Log\nQuadratic Formula: Q\nVertex: V"
              "\nArea: A\nFactorial: F\nCosine: C\nSine: S\nArithmetic Calculator: Ar\nDot Product: D"
              "\nMagnitude: M\nDerivative(Power Rule): Der\nPermutations: P\nCombinations: Comb"
              "\nMatrix Dot Product: MDP\nMatrix Addition: MA\nMatrix Subtraction: MS\nMatrix Multiplication: MM"
              "\nMatrix Division: MD\nSet Operators: Set\nGreatest Common Divisor: GCD\nSynthetic Division: SD"
              "\nPrime Factorization: PF\nLeast Common Multiplier: LCM\nCreate Complex Number: CCN"
              "\nComplex Number Multiplication by a Multiplier: CNM\nComplex Number Real Part: CNR"
              "\nComplex Number Imaginary Part: CNI\nComplex Number Absolute Value: CNAV\nComplex Number Foil: CNF"
              "\nPolynomial Foil: Poly\nEuclidean Distance: ED\nA divides B: |\nBinomial Theorem: Bin\n"
              "Euler's Form: EF\nNumber of Functions: NF\nHandshaking Theorem: HT\nLogistic Equation: LE\n"
              "Ackermann's Function: AF\n")
        # While in math commands
        while True:
            # Get math command
            mth_cmd_input = input("Enter a Math Command (empty to exit): ")

            # If empty string
            if mth_cmd_input == empty_str:
                # Leave math commands
                break

            # If math command is 'Log'
            elif mth_cmd_input == "Log":
                try:
                    # Get value to take log of
                    log_input = int(input("Enter a number to take the common log of: "))
                    print(m.log10(log_input))
                except ValueError:
                    # If value error, send message to say to enter an int
                    print("Please enter an integer")
                    continue

            # If math command is 'q'
            elif mth_cmd_input.upper() == "Q":
                try:
                    # Get the values a, b and c
                    a_input = int(input("Enter the value of A: "))
                    b_input = int(input("Enter the value of B: "))
                    c_input = int(input("Enter the value of C: "))
                    # Print the quadratic formula
                    print("x =", algepy.quadratic_formula(a_input, b_input, c_input))
                except ValueError:
                    # If value error, send message to say to enter an int
                    print("Please enter an integer")
                    continue

            # If math command is 'v'
            elif mth_cmd_input.upper() == "V":
                try:
                    # Get the values a, b and c
                    a_prompt = int(input("Enter the value of A: "))
                    b_prompt = int(input("Enter the value of B: "))
                    c_prompt = int(input("Enter the value of C: "))
                    # Print the vertex
                    print("Vertex =", algepy.vertex(a_prompt, b_prompt, c_prompt))
                except ValueError:
                    # If value error, send message to say to enter an int
                    print("Please enter an integer")
                    continue

            # If math command is 'a'
            elif mth_cmd_input.upper() == "A":
                # Get the features of the shape to take the area of
                shape_input = input("Enter the name of the shape (Case Sensitive): ")
                length_input = int(input("Enter the shape's length (if the shape doesn't use length put 0, don't "
                                         "leave blank): "))
                width_input = int(input("Enter the shape's width (if the shape doesn't use width put 0, don't "
                                        "leave blank): "))
                height_input = int(input("Enter the shape's height (if the shape doesn't use height put 0, don't "
                                         "leave blank): "))
                radius_input = int(input("Enter the shape's radius (if the shape doesn't use radius put 0, don't "
                                         "leave blank): "))
                base_input = int(input("Enter the shape's base (if the shape doesn't use base put 0, don't "
                                       "leave blank): "))
                side_input = int(input("Enter the shape's side (if the shape doesn't use side put 0, don't "
                                       "leave blank): "))
                # Print the area of the shape
                print(algepy.area(shape_input, length_input, width_input, height_input, radius_input, base_input,
                                  side_input))

            # If math command is 'f'
            elif mth_cmd_input.upper() == "F":
                try:
                    # Get value to take the factorial of
                    factorial_input = int(input("Enter number to take factorial of: "))
                    print(m.factorial(factorial_input))
                except ValueError:
                    # If value error, send message to say to enter an int
                    print("Please enter an integer")
                    continue

            # If math command is 'c'
            elif mth_cmd_input.upper() == "C":
                name = "RD"
                try:
                    # Get value to take the cosine of
                    cosine_input = int(input("Enter number to take the cosine of: "))
                except ValueError:
                    # If value error, send message to say to enter an int
                    print("Please enter an integer")
                    continue
                zip(name, algepy.cosine(cosine_input))
                for pair in zip(name, algepy.cosine(cosine_input)):
                    # Print radians and degrees
                    print(pair)

            # If math command is 's'
            elif mth_cmd_input.upper() == "S":
                name = "RD"
                try:
                    # Get the value to take the cosine of
                    sine_input = int(input("Enter number to take the sine of: "))
                except ValueError:
                    # If value error, send message to say to enter an int
                    print("Please enter an integer")
                    continue
                zip(name, algepy.sine(sine_input))
                for pair in zip(name, algepy.sine(sine_input)):
                    # Print radians and degrees
                    print(pair)

            # If math command is 'Ar'
            elif mth_cmd_input == "Ar":
                print("When you are trying to find an arithmetic value that is not given, then you can find "
                      "said value with the formula A(n)=A(1)+(n-1)d, where A(n) is the unknown value, A(1) is "
                      "the first value in the sequence, n is the value of the unknown, and d is the common difference.")
                try:
                    # Get the values to take the arithmetic sequence of
                    a1 = int(input("Enter A(1) here: "))
                    n = int(input("Enter n here: "))
                    d = int(input("Enter d here: "))
                    y = a1 + n - 1 * d
                    print("A({0}) = {1}".format(n, y))
                except ValueError:
                    # If value error, send message to say to enter an int
                    print("Please enter an integer")
                    continue

            # If math command is 'd'
            elif mth_cmd_input.upper() == "D":
                print("Let v = ax + by and w = cx + dy be vectors. Then we define the Dot Product as v * w = ac + bd\n")
                try:
                    # Get the values to take the dot product of
                    a_input = int(input("Enter a here: "))
                    b_input = int(input("Enter b here: "))
                    c_input = int(input("Enter c here: "))
                    d_input = int(input("Enter d here: "))
                    print(algepy.dot_product(a_input, b_input, c_input, d_input))
                except ValueError:
                    # If value error, send message to say to enter an int
                    print("Please enter an integer")
                    continue

            # If math command is 'm'
            elif mth_cmd_input.upper() == "M":
                try:
                    # Get the values to take the magnitude of
                    ax_input = int(input("Enter ax here: "))
                    by_input = int(input("Enter by here: "))
                    print(algepy.magnitude(ax_input, by_input))
                except ValueError:
                    # If value error, send message to say to enter an int
                    print("Please enter an integer!")
                    continue

            # If math command is 'Der'
            elif mth_cmd_input == "Der":
                name = "VE"
                print("The power rule is as follows: d/dx(x^n) = n * x ^ (n-1)")
                try:
                    # Get the values to run the power rule with
                    x_input = int(input("Enter x here: "))
                    n_input = int(input("Enter n here: "))
                except ValueError:
                    # If value error, send message to say to enter an int
                    print("Please enter an integer!")
                    continue
                zip(name, algepy.derivative(x_input, n_input))
                for pair in zip(name, algepy.derivative(x_input, n_input)):
                    # Print V and E
                    print(pair)
                print("Where V is the variable, and E is the exponent written as V^E.\n")

            # If math command is 'p'
            elif mth_cmd_input.upper() == "P":
                print("Using the function P(n,r) = n! / (n-r)! We write a function that can instantly "
                      "figure out the value for n permutation r")
                try:
                    # Get the values to take the permutation
                    n_input = int(input("Enter n here: "))
                    r_input = int(input("Enter r here: "))
                    print(discretemath.nPr(n_input, r_input), "\n")
                except ValueError:
                    # If value error, send message to say to enter an int
                    print("Please enter an integer!")
                    continue

            # If math command is 'Comb'
            elif mth_cmd_input == "Comb":
                print("Using the function C(n,r) = n! / r!(n-r)! We write a function that can instantly "
                      "figure out the value for n choose r")
                try:
                    # Get the values to take the combination
                    n_input = int(input("Enter n here: "))
                    r_input = int(input("Enter r here: "))
                    print(discretemath.nCr(n_input, r_input), "\n")
                except ValueError:
                    # If value error, send message to say to enter an int
                    print("Please enter an integer")
                    continue

            # If math command is 'MDP'
            elif mth_cmd_input == "MDP":
                print("In some cases we multiply two matrices together using the dot product.\n")
                try:
                    # Get values to take the matrix dot product
                    a_input = int(input("Enter a here: "))
                    b_input = int(input("Enter b here: "))
                    c_input = int(input("Enter c here: "))
                    d_input = int(input("Enter d here: "))
                    w_input = int(input("Enter w here: "))
                    x_input = int(input("Enter x here: "))
                    y_input = int(input("Enter y here: "))
                    z_input = int(input("Enter z here: "))
                    algepy.matrices_dot_product(a_input, b_input, c_input, d_input, w_input, x_input, y_input, z_input)
                except ValueError:
                    # If value error, send message to say to enter an int
                    print("Please enter an integer")
                    continue

            # If math command is 'MA'
            elif mth_cmd_input == "MA":
                print("In some cases we can add two matrices together.\n")
                try:
                    # Get the values to take the matrix addition
                    a_input = int(input("Enter a here: "))
                    b_input = int(input("Enter b here: "))
                    c_input = int(input("Enter c here: "))
                    d_input = int(input("Enter d here: "))
                    w_input = int(input("Enter w here: "))
                    x_input = int(input("Enter x here: "))
                    y_input = int(input("Enter y here: "))
                    z_input = int(input("Enter z here: "))
                    algepy.matrices_addition(a_input, b_input, c_input, d_input, w_input, x_input, y_input, z_input)
                except ValueError:
                    # If value error, send message to say to enter an int
                    print("Please enter an integer")
                    continue

            # If math command is 'MS'
            elif mth_cmd_input == "MS":
                print("In some cases we can subtract two matrices.\n")
                try:
                    # Get the values to take the matrix subtraction
                    a_input = int(input("Enter a here: "))
                    b_input = int(input("Enter b here: "))
                    c_input = int(input("Enter c here: "))
                    d_input = int(input("Enter d here: "))
                    w_input = int(input("Enter w here: "))
                    x_input = int(input("Enter x here: "))
                    y_input = int(input("Enter y here: "))
                    z_input = int(input("Enter z here: "))
                    algepy.matrices_subtration(a_input, b_input, c_input, d_input, w_input, x_input, y_input, z_input)
                except ValueError:
                    # If value error, send message to say to enter an int
                    print("Please enter an integer")
                    continue

            # If math command is 'MM'
            elif mth_cmd_input == "MM":
                print("In some cases we multiply two matrices together.\n")
                try:
                    # Get the values for matrix multiplication
                    a_input = int(input("Enter a here: "))
                    b_input = int(input("Enter b here: "))
                    c_input = int(input("Enter c here: "))
                    d_input = int(input("Enter d here: "))
                    w_input = int(input("Enter w here: "))
                    x_input = int(input("Enter x here: "))
                    y_input = int(input("Enter y here: "))
                    z_input = int(input("Enter z here: "))
                    algepy.matrices_multiply(a_input, b_input, c_input, d_input, w_input, x_input, y_input, z_input)
                except ValueError:
                    # If value error, send message to say to enter an int
                    print("Please enter an integer")
                    continue

            # If math command is 'MD'
            elif mth_cmd_input == "MD":
                print("In some cases we divide two matrices.\n")
                try:
                    # Get the values for matrix division
                    a_input = int(input("Enter a here: "))
                    b_input = int(input("Enter b here: "))
                    c_input = int(input("Enter c here: "))
                    d_input = int(input("Enter d here: "))
                    w_input = int(input("Enter w here: "))
                    x_input = int(input("Enter x here: "))
                    y_input = int(input("Enter y here: "))
                    z_input = int(input("Enter z here: "))
                    algepy.matrices_divide(a_input, b_input, c_input, d_input, w_input, x_input, y_input, z_input)
                except ValueError:
                    # If value error, send message to say to enter an int
                    print("Please enter an integer")
                    continue

            # If math command is 'Set'
            elif mth_cmd_input == "Set":
                print()
                try:
                    # Get values for set theory
                    A_element_count = int(input("Enter the element count for A: "))
                    B_element_count = int(input("Enter the element count for B: "))
                    discretemath.set_theory(A_element_count, B_element_count)
                except ValueError:
                    # If value error, send message to say to enter an int
                    print("Please enter an integer")
                    continue

            # If math command is 'GCD'
            elif mth_cmd_input == "GCD":
                try:
                    # Get values for GCD
                    a_GCD_input = int(input("Enter the value of a: "))
                    b_GCD_input = int(input("Enter the value of b: "))
                    discretemath.GCD(a_GCD_input, b_GCD_input)
                    print("\n{0} = {1} * {2} + {3} * {4}\nwhere the LHS is the linear combination\n".format(
                        discretemath.GCD(a_GCD_input, b_GCD_input)[0], a_GCD_input,
                        discretemath.GCD(a_GCD_input, b_GCD_input)[1], b_GCD_input,
                        discretemath.GCD(a_GCD_input, b_GCD_input)[2]))
                except ValueError:
                    # If value error, send message to say to enter an int
                    print("Please enter an integer!")
                    continue

            # If math command is 'LCM'
            elif mth_cmd_input == "LCM":
                try:
                    # Get values to take 'LCM'
                    a_LCM_input = int(input("Enter the value of a: "))
                    b_LCM_input = int(input("Enter the value of b: "))
                    print(discretemath.LCM(a_LCM_input, b_LCM_input))
                except ValueError:
                    # If value error, send message to say to enter an int
                    print("Please enter an integer!")
                    continue

            # If math command is 'SD'
            elif mth_cmd_input == "SD":
                try:
                    # Get values to run synthetic division
                    degree_input = int(input("Enter the degree: "))
                    divisor_input = int(input("Enter the divisor: "))
                    print(algepy.synthetic_division(degree_input, divisor_input))
                except ValueError:
                    # If value error, send message to say to enter an int
                    print("Please enter an integer!")
                    continue

            # If math command is 'PF'
            elif mth_cmd_input == "PF":
                try:
                    # Get values to run prime factorization
                    n_prime_input = int(input("Enter a number to take the prime factorization of "
                                              "(Note: the longer the number the longer it may take): "))
                    discretemath.prime_factorization(n_prime_input)
                    print()
                except ValueError:
                    # If value error, send message to say to enter an int
                    print("Please enter an integer!")
                    continue

            # If math command is 'CCN'
            elif mth_cmd_input == "CCN":
                try:
                    # Get values to create complex number
                    real_input = int(input("Enter the real part of the complex number: "))
                    imaginary_input = int(input("Enter the imaginary part of the complex number: "))
                    print(algepy.create_complex_number(real_input, imaginary_input))
                except ValueError:
                    # If value error, send message to say to enter an int
                    print("Please enter an integer!")
                    continue

            # If math command is 'CNM'
            elif mth_cmd_input == "CNM":
                try:
                    # Get values to run complex number multiplication
                    real_input = int(input("Enter the real part of the complex number: "))
                    imaginary_input = int(input("Enter the imaginary part of the complex number: "))
                    multiplier_input = int(input("Enter the multiplier: "))
                    print(algepy.complex_number_multiplication(real_input, imaginary_input, multiplier_input))
                except ValueError:
                    # If value error, send message to say to enter an int
                    print("Please enter an integer!")
                    continue

            # If math command is 'CNR'
            elif mth_cmd_input == "CNR":
                try:
                    # Get values to get the real part of complex number
                    real_input = int(input("Enter the real part of the complex number: "))
                    imaginary_input = int(input("Enter the imaginary part of the complex number: "))
                    print(algepy.complex_number_real(real_input, imaginary_input))
                except ValueError:
                    # If value error, send message to say to enter an int
                    print("Please enter an integer!")
                    continue

            # If math command is 'CNI'
            elif mth_cmd_input == "CNI":
                try:
                    # Get values to find the imaginary part of the complex number
                    real_input = int(input("Enter the real part of the complex number: "))
                    imaginary_input = int(input("Enter the imaginary part of the complex number: "))
                    print(algepy.complex_number_imaginary(real_input, imaginary_input))
                except ValueError:
                    # If value error, send message to say to enter an int
                    print("Please enter an integer!")
                    continue

            # If math command is 'CNAV'
            elif mth_cmd_input == "CNAV":
                try:
                    # Get values to find the absolute value of the complex number
                    real_input = int(input("Enter the real part of the complex number: "))
                    imaginary_input = int(input("Enter the imaginary part of the complex number: "))
                    print(algepy.complex_number_absolute_value(real_input, imaginary_input))
                except ValueError:
                    # If value error, send message to say to enter an int
                    print("Please enter an integer!")
                    continue

            # If math command is 'CNF'
            elif mth_cmd_input == "CNF":
                try:
                    # Get the values to run complex number multiplication with foil method
                    real_input = int(input("Enter the real part of the first complex number: "))
                    imaginary_input = int(input("Enter the imaginary part of the first complex number: "))
                    real_input_2 = int(input("Enter the real part of the second complex number: "))
                    imaginary_input_2 = int(input("Enter the imaginary part of the second complex number: "))
                    print(algepy.complex_number_multiplication_foil(real_input, imaginary_input, real_input_2,
                                                                    imaginary_input_2))
                except ValueError:
                    # If value error, send message to say to enter an int
                    print("Please enter an integer!")
                    continue

            # If math command is 'Poly'
            elif mth_cmd_input == "Poly":
                try:
                    print("A function in the form (x +/- a)(y +/- b) can be foiled to get "
                          "(xy +/- xb +/- ay +/- ab), example (x+2)(x-2) = x^2 - 4. If your "
                          "x or y doesn't have a leading coefficient, leave it as one for simplicity.")
                    # Get values to create a polynomial
                    a_input = int(input("Enter a: "))
                    b_input = int(input("Enter b: "))
                    x_input = int(input("Enter x: "))
                    y_input = int(input("Enter y: "))
                    print(algepy.foil(a_input, b_input, x_input, y_input))
                except ValueError:
                    # If value error, send message to say to enter an int
                    print("Please enter an integer!")
                    continue

            # If math command is 'ED'
            elif mth_cmd_input == "ED":
                xLi = []
                yLi = []
                try:
                    # Get values to run Euclidean Distance
                    x_1_input = int(input("Enter the value for x_1: "))
                    xLi.append(x_1_input)
                    y_1_input = int(input("Enter the value for y_1: "))
                    yLi.append(y_1_input)
                    x_2_input = int(input("Enter the value for x_2: "))
                    xLi.append(x_2_input)
                    y_2_input = int(input("Enter the value for y_2: "))
                    yLi.append(y_2_input)
                    print(algepy.euclidD(xLi, yLi))
                except ValueError:
                    # If value error, send message to say to enter an int
                    print("Please enter an integer!")
                    continue

            # If math command is '|'
            elif mth_cmd_input == "|":
                try:
                    # Get values to see if a divides b
                    a_divides_input = int(input("Enter the value of A: "))
                    b_divides_input = int(input("Enter the value of B: "))
                    print("{0} | {1} is {2}".format(a_divides_input, b_divides_input,
                                                    discretemath.a_divides_b(a_divides_input, b_divides_input)))
                except ZeroDivisionError:
                    # If divide by zero error, send message to say value can't be zero
                    print("A can't have a value of zero!")
                    continue

            # If math command is 'Bin'
            elif mth_cmd_input == "Bin":
                print("The binomial theorem is defined as (x + y)^n = sum_k=0^n(nCr(n, k))*x^(n-k)*y^k = "
                      "sum_k=0^n(nCr(n, k))x^n*y^(n-k).\n"
                      "The binomial theorem tells us how to expand expressions of the form (x + y)^n.\n"
                      "This function will run through the binomial theorem and return the expansion.\n")
                # Get values to run the binomial theorem on
                x_input = int(input("Enter the value of x: "))
                y_input = int(input("Enter the value of y: "))
                n_input = int(input("Enter the value of n: "))
                print(discretemath.binomial_theorem(x_input, y_input, n_input))

            # If math command is 'EF'
            elif mth_cmd_input == "EF":
                # Get values to run Euler's formula
                vertex_count = int(input("Enter the vertex count: "))
                edge_count = int(input("Enter the edge count: "))
                print(discretemath.eulers_form(vertex_count, edge_count))

            # If math command is 'NF'
            elif mth_cmd_input == "NF":
                # Get values to determine number of functions
                a_input = int(input("Enter the size of set A: "))
                b_input = int(input("Enter the size of set B: "))
                print("Function Types: onto, one-to-one, one-to-one correspondence, normal")
                function_type = input("Enter the function type: ")
                print("The number of {0} functions from A to B is {1}".format(function_type,
                      discretemath.number_of_functions(a_input, b_input, function_type)))

            # If math command is 'HT'
            elif mth_cmd_input == "HT":
                # Get values to run Handshaking Theorem
                vertex_input = int(input("Enter the vertex count(if unknown, enter 0): "))
                edge_input = int(input("Enter the edge count(if unknown, enter 0): "))
                degree_input = int(input("Enter the degree count(if unknown enter 0): "))
                if vertex_input == 0:
                    print("The vertex count is: ", discretemath.handshaking_theorem(None, edge_input, degree_input))
                elif edge_input == 0:
                    print("The edge count is: ", discretemath.handshaking_theorem(vertex_input, None, degree_input))
                else:
                    print("The degree count is: ", discretemath.handshaking_theorem(vertex_input, edge_input, None))

            # If math command is 'LE'
            elif mth_cmd_input == "LE":
                # Get values to find the logistic equation
                x_0 = float(input("Enter the initial value: "))
                r = float(input("Enter the rate of change: "))
                iterate = int(input("Enter the value to iterate over: "))
                print(discretemath.logistic_equation(x_0, r, iterate))

            # If math command is 'AF'
            elif mth_cmd_input == "AF":
                # Get values to run in Ackermann's function
                m_input = int(input("Enter the value of m: "))
                n_input = int(input("Enter the value of n: "))
                print(discretemath.ackermanns_function(m_input, n_input))

            # If not a math command
            else:
                print("\nPlease enter a math command!\n")
                continue

    # If user input is 'b'
    elif data_input.upper() == "B":
        while True:
            # Enter text to translate to binary
            usr_input = input("Enter something to translate to binary (leave empty and press enter to exit): ")
            if usr_input == empty_str:
                break
            else:
                encrypti.bin_translator(usr_input)

    # If user input is 'h'
    elif data_input.upper() == "H":
        while True:
            # Enter text to translate to hex
            usr_input = input("Enter something to translate to hexadecimal (leave empty and press enter to exit): ")
            if usr_input == empty_str:
                break
            else:
                encrypti.hex_translator(usr_input)

    # If user input is 'f'
    elif data_input.upper() == "F":
        # Flip a coin
        mini_games.flip_a_coin()

    # If user input is 'Roll'
    elif data_input == "Roll":
        mini_games.roll_dice()

    # If user input is 'FGC'
    elif data_input == "FGC":
        try:
            # Get values to calculate final grade
            current_grade = float(input("Enter your current grade: "))
            goal = int(input("Enter your overall grade goal: "))
            final_weight = int(input("Enter the weight of the final: "))
            print("You need a {0} percent on the final to get a {1} in the class.".format(round(final_grade_calculator(
                current_grade, goal, final_weight), 2), goal))
        except ValueError:
            # If value error, send message to say to enter a float
            print("Please enter an integer or a float!")
            continue

    # If user input is 'CC'
    elif data_input == "CC":
        # Get string to run through caesar cipher
        string_input = input("Enter the string to be encoded: ")
        n_input = int(input("Enter the number of letters that the string should be shifted: "))
        encrypti.caesar_cipher(n_input, string_input)

    # If user input is 'Logic'
    elif data_input == "Logic":
        print("\nLogic Commands: \n---------------------------\np or q: poq\np and q: paq\nnot p: np\np xor q: pxq\n"
              "if p then q: iptq\np nor q: pnq")
        # While in logic commands
        while True:
            # Get logic command
            logic_operator_input = input("\nEnter a logic operation(empty to exit): ")

            # If logic command is empty string
            if logic_operator_input == empty_str:
                # Leave logic operators
                break

            # If logic command is 'poq'
            elif logic_operator_input == "poq":
                try:
                    # Get values to run p or q
                    p_input = int(input("Enter the truth value for p: "))
                    q_input = int(input("Enter the truth value for q: "))
                    print("The truth value of {0} or {1} is {2}".format(p_input, q_input, discretemath.p_or_q(p_input,
                                                                                                              q_input)))
                except ValueError:
                    # If value error, send message to say to enter 0 or 1
                    print("Please enter an acceptable truth value, i.e. 0 or 1!")
                    continue

            # If logic command is 'paq'
            elif logic_operator_input == "paq":
                try:
                    # Get values to run p and q
                    p_input = int(input("Enter the truth value for p: "))
                    q_input = int(input("Enter the truth value for q: "))
                    print("The truth value of {0} and {1} is {2}".format(p_input, q_input, discretemath.p_and_q(
                                                                                            p_input, q_input)))
                except ValueError:
                    # If value error, send message to say to enter 0 or 1
                    print("Please enter an acceptable truth value, i.e. 0 or 1!")
                    continue

            # If logic command is 'np'
            elif logic_operator_input == "np":
                try:
                    # Get value to run not p
                    p_input = int(input("Enter the truth value for p: "))
                    print("The truth value of not {0} is {1}".format(p_input, discretemath.not_p(p_input)))
                except ValueError:
                    # If value error, send message to say to enter 0 or 1
                    print("Please enter an acceptable truth value, i.e. 0 or 1!")
                    continue

            # If logic command is 'iptq'
            elif logic_operator_input == "iptq":
                try:
                    # Get values to run if p then q
                    p_input = int(input("Enter the truth value for p: "))
                    q_input = int(input("Enter the truth value for q: "))
                    print("The truth value of if {0} then {1} is {2}".format(p_input, q_input, discretemath.if_p_then_q(
                                                                            p_input, q_input)))
                except ValueError:
                    # If value error, send message to say to enter 0 or 1
                    print("Please enter an acceptable truth value, i.e. 0 or 1!")
                    continue

            # If logic command is 'pnq'
            elif logic_operator_input == "pnq":
                try:
                    # Get values to run p nor q
                    p_input = int(input("Enter the truth value for p: "))
                    q_input = int(input("Enter the truth value for q: "))
                    print("The truth value of {0} nor {1} is {2}".format(p_input, q_input,
                                                                         discretemath.p_nor_q(p_input, q_input)))
                except ValueError:
                    # If value error, send message to say to enter 0 or 1
                    print("Please enter an acceptable truth value, i.e. 0 or 1!")
                    continue

    # If user input not a command
    else:
        print("\nPlease enter a command from the command list!")
