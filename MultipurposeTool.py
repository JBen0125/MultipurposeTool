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
            # Play error sound
            os.system('afplay /System/Library/Sounds/Funk.aiff&')

        # If Linux
        elif operate_sys == "linux" or operate_sys == "linux2":
            pass

        # If Windows
        elif operate_sys == "win32":
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

            # If data science user input is l
            elif data_command_input.upper() == "L":
                while True:
                    add_input = input("Enter data to add to the list (empty to exit): ")
                    if add_input == empty_str:
                        break
                    else:
                        data.append(add_input)
            elif data_command_input.upper() == "P":
                print(data)
                print(keys)
            elif data_command_input.upper() == "D":
                while True:
                    key_input = input("\nEnter data/x-value (empty to exit): ")
                    if key_input == empty_str:
                        break
                    else:
                        value_input = input("\nEnter data/y-value (empty to exit): ")
                        keys[key_input] = value_input
            elif data_command_input.upper() == "S":
                print("list sorted: ", list_functions.sort_list(data))
                print()
            elif data_command_input == "+":
                new_li = []
                for item in data:
                    new_li.append(int(item))
                print("sum of list: ", list_functions.sum_list(new_li))
                print()
            elif data_command_input.upper() == "A":
                new_li = []
                for item in data:
                    new_li.append(int(item))
                print("average of list: ", list_functions.mean_list(new_li))
                print()
            elif data_command_input.upper() == "M":
                new_li = []
                for item in data:
                    new_li.append(int(item))
                print("median of list: ", list_functions.median_list(new_li))
                print()
            elif data_command_input == "Mo":
                new_li = []
                for item in data:
                    new_li.append(int(item))
                print("mode of list: ", list_functions.mode_list(new_li))
                print()
            elif data_command_input.upper() == "R":
                data = []
                print("List has been reset: ", data)
                print()
            elif data_command_input == "RD":
                keys = {}
                print("Dictionary has been reset: ", keys)
                print()
    elif data_input.upper() == "R":
        try:
            min_input = int(input("What is the minimum value? "))
            max_input = int(input("What is the maximum value? "))
            print(int(rand.randint(min_input, max_input)))
        except ValueError:
            print()
            continue
    elif data_input.upper() == "M":
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
        while True:
            mth_cmd_input = input("Enter a Math Command (empty to exit): ")
            if mth_cmd_input == empty_str:
                break
            elif mth_cmd_input == "Log":
                try:
                    log_input = int(input("Enter a number to take the common log of: "))
                    print(m.log10(log_input))
                except ValueError:
                    print("Please enter an integer")
                    continue
            elif mth_cmd_input.upper() == "Q":
                try:
                    a_input = int(input("Enter the value of A: "))
                    b_input = int(input("Enter the value of B: "))
                    c_input = int(input("Enter the value of C: "))
                    print("x =", algepy.quadratic_formula(a_input, b_input, c_input))
                except ValueError:
                    print("Please enter an integer")
                    continue
            elif mth_cmd_input.upper() == "V":
                try:
                    a_prompt = int(input("Enter the value of A: "))
                    b_prompt = int(input("Enter the value of B: "))
                    c_prompt = int(input("Enter the value of C: "))
                    print("Vertex =", algepy.vertex(a_prompt, b_prompt, c_prompt))
                except ValueError:
                    print("Please enter an integer")
                    continue
            elif mth_cmd_input.upper() == "A":
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
                print(algepy.area(shape_input, length_input, width_input, height_input, radius_input, base_input,
                                  side_input))
            elif mth_cmd_input.upper() == "F":
                try:
                    factorial_input = int(input("Enter number to take factorial of: "))
                    print(m.factorial(factorial_input))
                except ValueError:
                    print("Please enter an integer")
                    continue
            elif mth_cmd_input.upper() == "C":
                name = "RD"
                try:
                    cosine_input = int(input("Enter number to take the cosine of: "))
                except ValueError:
                    print("Please enter an integer")
                    continue
                zip(name, algepy.cosine(cosine_input))
                for pair in zip(name, algepy.cosine(cosine_input)):
                    print(pair)
            elif mth_cmd_input.upper() == "S":
                name = "RD"
                try:
                    sine_input = int(input("Enter number to take the sine of: "))
                except ValueError:
                    print("Please enter an integer")
                    continue
                zip(name, algepy.sine(sine_input))
                for pair in zip(name, algepy.sine(sine_input)):
                    print(pair)
            elif mth_cmd_input == "Ar":
                print("When you are trying to find an arithmetic value that is not given, then you can find "
                      "said value with the formula A(n)=A(1)+(n-1)d, where A(n) is the unknown value, A(1) is "
                      "the first value in the sequence, n is the value of the unknown, and d is the common difference.")
                try:
                    a1 = int(input("Enter A(1) here: "))
                    n = int(input("Enter n here: "))
                    d = int(input("Enter d here: "))
                    y = a1 + n - 1 * d
                    print("A({0}) = {1}".format(n, y))
                except ValueError:
                    print("Please enter an integer")
                    continue
            elif mth_cmd_input.upper() == "D":
                print("Let v = ax + by and w = cx + dy be vectors. Then we define the Dot Product as v * w = ac + bd\n")
                try:
                    a_input = int(input("Enter a here: "))
                    b_input = int(input("Enter b here: "))
                    c_input = int(input("Enter c here: "))
                    d_input = int(input("Enter d here: "))
                    print(algepy.dot_product(a_input, b_input, c_input, d_input))
                except ValueError:
                    print("Please enter an integer")
                    continue
            elif mth_cmd_input.upper() == "M":
                try:
                    ax_input = int(input("Enter ax here: "))
                    by_input = int(input("Enter by here: "))
                    print(algepy.magnitude(ax_input, by_input))
                except ValueError:
                    print("Please enter an integer!")
                    continue
            elif mth_cmd_input == "Der":
                name = "VE"
                print("The power rule is as follows: d/dx(x^n) = n * x ^ (n-1)")
                try:
                    x_input = int(input("Enter x here: "))
                    n_input = int(input("Enter n here: "))
                except ValueError:
                    print("Please enter an integer!")
                    continue
                zip(name, algepy.derivative(x_input, n_input))
                for pair in zip(name, algepy.derivative(x_input, n_input)):
                    print(pair)
                print("Where V is the variable, and E is the exponent written as V^E.\n")
            elif mth_cmd_input.upper() == "P":
                print("Using the function P(n,r) = n! / (n-r)! We write a function that can instantly "
                      "figure out the value for n permutation r")
                try:
                    n_input = int(input("Enter n here: "))
                    r_input = int(input("Enter r here: "))
                    print(discretemath.nPr(n_input, r_input), "\n")
                except ValueError:
                    print("Please enter an integer!")
                    continue
            elif mth_cmd_input == "Comb":
                print("Using the function C(n,r) = n! / r!(n-r)! We write a function that can instantly "
                      "figure out the value for n choose r")
                try:
                    n_input = int(input("Enter n here: "))
                    r_input = int(input("Enter r here: "))
                    print(discretemath.nCr(n_input, r_input), "\n")
                except ValueError:
                    print("Please enter an integer")
                    continue
            elif mth_cmd_input == "MDP":
                print("In some cases we multiply two matrices together using the dot product.\n")
                try:
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
                    print("Please enter an integer")
                    continue
            elif mth_cmd_input == "MA":
                print("In some cases we can add two matrices together.\n")
                try:
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
                    print("Please enter an integer")
                    continue
            elif mth_cmd_input == "MS":
                print("In some cases we can subtract two matrices.\n")
                try:
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
                    print("Please enter an integer")
                    continue
            elif mth_cmd_input == "MM":
                print("In some cases we multiply two matrices together.\n")
                try:
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
                    print("Please enter an integer")
                    continue
            elif mth_cmd_input == "MD":
                print("In some cases we divide two matrices.\n")
                try:
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
                    print("Please enter an integer")
                    continue
            elif mth_cmd_input == "Set":
                print()
                try:
                    A_element_count = int(input("Enter the element count for A: "))
                    B_element_count = int(input("Enter the element count for B: "))
                    discretemath.set_theory(A_element_count, B_element_count)
                except ValueError:
                    print("Please enter an integer")
                    continue
            elif mth_cmd_input == "GCD":
                try:
                    a_GCD_input = int(input("Enter the value of a: "))
                    b_GCD_input = int(input("Enter the value of b: "))
                    discretemath.GCD(a_GCD_input, b_GCD_input)
                    print("\n{0} = {1} * {2} + {3} * {4}\nwhere the LHS is the linear combination\n".format(
                        discretemath.GCD(a_GCD_input, b_GCD_input)[0], a_GCD_input,
                        discretemath.GCD(a_GCD_input, b_GCD_input)[1], b_GCD_input,
                        discretemath.GCD(a_GCD_input, b_GCD_input)[2]))
                except ValueError:
                    print("Please enter an integer!")
                    continue
            elif mth_cmd_input == "LCM":
                try:
                    a_LCM_input = int(input("Enter the value of a: "))
                    b_LCM_input = int(input("Enter the value of b: "))
                    print(discretemath.LCM(a_LCM_input, b_LCM_input))
                except ValueError:
                    print("Please enter an integer!")
                    continue
            elif mth_cmd_input == "SD":
                try:
                    degree_input = int(input("Enter the degree: "))
                    divisor_input = int(input("Enter the divisor: "))
                    print(algepy.synthetic_division(degree_input, divisor_input))
                except ValueError:
                    print("Please enter an integer!")
            elif mth_cmd_input == "PF":
                try:
                    n_prime_input = int(input("Enter a number to take the prime factorization of "
                                              "(Note: the longer the number the longer it may take): "))
                    discretemath.prime_factorization(n_prime_input)
                    print()
                except ValueError:
                    print("Please enter an integer!")
            elif mth_cmd_input == "CCN":
                try:
                    real_input = int(input("Enter the real part of the complex number: "))
                    imaginary_input = int(input("Enter the imaginary part of the complex number: "))
                    print(algepy.create_complex_number(real_input, imaginary_input))
                except ValueError:
                    print("Please enter an integer!")
            elif mth_cmd_input == "CNM":
                try:
                    real_input = int(input("Enter the real part of the complex number: "))
                    imaginary_input = int(input("Enter the imaginary part of the complex number: "))
                    multiplier_input = int(input("Enter the multiplier: "))
                    print(algepy.complex_number_multiplication(real_input, imaginary_input, multiplier_input))
                except ValueError:
                    print("Please enter an integer!")
            elif mth_cmd_input == "CNR":
                try:
                    real_input = int(input("Enter the real part of the complex number: "))
                    imaginary_input = int(input("Enter the imaginary part of the complex number: "))
                    print(algepy.complex_number_real(real_input, imaginary_input))
                except ValueError:
                    print("Please enter an integer!")
            elif mth_cmd_input == "CNI":
                try:
                    real_input = int(input("Enter the real part of the complex number: "))
                    imaginary_input = int(input("Enter the imaginary part of the complex number: "))
                    print(algepy.complex_number_imaginary(real_input, imaginary_input))
                except ValueError:
                    print("Please enter an integer!")
            elif mth_cmd_input == "CNAV":
                try:
                    real_input = int(input("Enter the real part of the complex number: "))
                    imaginary_input = int(input("Enter the imaginary part of the complex number: "))
                    print(algepy.complex_number_absolute_value(real_input, imaginary_input))
                except ValueError:
                    print("Please enter an integer!")
            elif mth_cmd_input == "CNF":
                try:
                    real_input = int(input("Enter the real part of the first complex number: "))
                    imaginary_input = int(input("Enter the imaginary part of the first complex number: "))
                    real_input_2 = int(input("Enter the real part of the second complex number: "))
                    imaginary_input_2 = int(input("Enter the imaginary part of the second complex number: "))
                    print(algepy.complex_number_multiplication_foil(real_input, imaginary_input, real_input_2,
                                                                    imaginary_input_2))
                except ValueError:
                    print("Please enter an integer!")
            elif mth_cmd_input == "Poly":
                try:
                    print("A function in the form (x +/- a)(y +/- b) can be foiled to get "
                          "(xy +/- xb +/- ay +/- ab), example (x+2)(x-2) = x^2 - 4. If your "
                          "x or y doesn't have a leading coefficient, leave it as one for simplicity.")
                    a_input = int(input("Enter a: "))
                    b_input = int(input("Enter b: "))
                    x_input = int(input("Enter x: "))
                    y_input = int(input("Enter y: "))
                    print(algepy.foil(a_input, b_input, x_input, y_input))
                except ValueError:
                    print("Please enter an integer!")
            elif mth_cmd_input == "ED":
                xLi = []
                yLi = []
                try:
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
                    print("Please enter an integer!")
            elif mth_cmd_input == "|":
                try:
                    a_divides_input = int(input("Enter the value of A: "))
                    b_divides_input = int(input("Enter the value of B: "))
                    print("{0} | {1} is {2}".format(a_divides_input, b_divides_input,
                                                    discretemath.a_divides_b(a_divides_input, b_divides_input)))
                except ZeroDivisionError:
                    print("A can't have a value of zero!")
            elif mth_cmd_input == "Bin":
                print("The binomial theorem is defined as (x + y)^n = sum_k=0^n(nCr(n, k))*x^(n-k)*y^k = "
                      "sum_k=0^n(nCr(n, k))x^n*y^(n-k).\n"
                      "The binomial theorem tells us how to expand expressions of the form (x + y)^n.\n"
                      "This function will run through the binomial theorem and return the expansion.\n")
                x_input = int(input("Enter the value of x: "))
                y_input = int(input("Enter the value of y: "))
                n_input = int(input("Enter the value of n: "))
                print(discretemath.binomial_theorem(x_input, y_input, n_input))
            elif mth_cmd_input == "EF":
                vertex_count = int(input("Enter the vertex count: "))
                edge_count = int(input("Enter the edge count: "))
                print(discretemath.eulers_form(vertex_count, edge_count))
            elif mth_cmd_input == "NF":
                a_input = int(input("Enter the size of set A: "))
                b_input = int(input("Enter the size of set B: "))
                print("Function Types: onto, one-to-one, one-to-one correspondence, normal")
                function_type = input("Enter the function type: ")
                print("The number of {0} functions from A to B is {1}".format(function_type,
                      discretemath.number_of_functions(a_input, b_input, function_type)))
            elif mth_cmd_input == "HT":
                vertex_input = int(input("Enter the vertex count(if unknown, enter 0): "))
                edge_input = int(input("Enter the edge count(if unknown, enter 0): "))
                degree_input = int(input("Enter the degree count(if unknown enter 0): "))
                if vertex_input == 0:
                    print("The vertex count is: ", discretemath.handshaking_theorem(None, edge_input, degree_input))
                elif edge_input == 0:
                    print("The edge count is: ", discretemath.handshaking_theorem(vertex_input, None, degree_input))
                else:
                    print("The degree count is: ", discretemath.handshaking_theorem(vertex_input, edge_input, None))
            elif mth_cmd_input == "LE":
                x_0 = float(input("Enter the initial value: "))
                r = float(input("Enter the rate of change: "))
                iterate = int(input("Enter the value to iterate over: "))
                print(discretemath.logistic_equation(x_0, r, iterate))
            elif mth_cmd_input == "AF":
                m_input = int(input("Enter the value of m: "))
                n_input = int(input("Enter the value of n: "))
                print(discretemath.ackermanns_function(m_input, n_input))
            else:
                print("\nPlease enter a math command!\n")
    elif data_input.upper() == "B":
        while True:
            usr_input = input("Enter something to translate to binary (leave empty and press enter to exit): ")
            if usr_input == empty_str:
                break
            else:
                encrypti.bin_translator(usr_input)
    elif data_input.upper() == "H":
        while True:
            usr_input = input("Enter something to translate to hexadecimal (leave empty and press enter to exit): ")
            if usr_input == empty_str:
                break
            else:
                encrypti.hex_translator(usr_input)
    elif data_input.upper() == "F":
        mini_games.flip_a_coin()
    elif data_input == "Roll":
        mini_games.roll_dice()
    elif data_input == "FGC":
        try:
            current_grade = float(input("Enter your current grade: "))
            goal = int(input("Enter your overall grade goal: "))
            final_weight = int(input("Enter the weight of the final: "))
            print("You need a {0} percent on the final to get a {1} in the class.".format(round(final_grade_calculator(
                current_grade, goal, final_weight), 2), goal))
        except ValueError:
            print("Please enter an integer or a float!")
    elif data_input == "CC":
        string_input = input("Enter the string to be encoded: ")
        n_input = int(input("Enter the number of letters that the string should be shifted: "))
        encrypti.caesar_cipher(n_input, string_input)
    elif data_input == "Logic":
        print("\nLogic Commands: \n---------------------------\np or q: poq\np and q: paq\nnot p: np\np xor q: pxq\n"
              "if p then q: iptq\np nor q: pnq")
        while True:
            logic_operator_input = input("\nEnter a logic operation(empty to exit): ")
            if logic_operator_input == empty_str:
                break
            elif logic_operator_input == "poq":
                try:
                    p_input = int(input("Enter the truth value for p: "))
                    q_input = int(input("Enter the truth value for q: "))
                    print("The truth value of {0} or {1} is {2}".format(p_input, q_input, discretemath.p_or_q(p_input,
                                                                                                              q_input)))
                except ValueError:
                    print("Please enter an acceptable truth value, i.e. 0 or 1!")
            elif logic_operator_input == "paq":
                try:
                    p_input = int(input("Enter the truth value for p: "))
                    q_input = int(input("Enter the truth value for q: "))
                    print("The truth value of {0} and {1} is {2}".format(p_input, q_input, discretemath.p_and_q(
                                                                                            p_input, q_input)))
                except ValueError:
                    print("Please enter an acceptable truth value, i.e. 0 or 1!")
            elif logic_operator_input == "np":
                try:
                    p_input = int(input("Enter the truth value for p: "))
                    print("The truth value of not {0} is {1}".format(p_input, discretemath.not_p(p_input)))
                except ValueError:
                    print("Please enter an acceptable truth value, i.e. 0 or 1!")
            elif logic_operator_input == "iptq":
                try:
                    p_input = int(input("Enter the truth value for p: "))
                    q_input = int(input("Enter the truth value for q: "))
                    print("The truth value of if {0} then {1} is {2}".format(p_input, q_input, discretemath.if_p_then_q(
                                                                            p_input, q_input)))
                except ValueError:
                    print("Please enter an acceptable truth value, i.e. 0 or 1!")
            elif logic_operator_input == "pnq":
                try:
                    p_input = int(input("Enter the truth value for p: "))
                    q_input = int(input("Enter the truth value for q: "))
                    print("The truth value of {0} nor {1} is {2}".format(p_input, q_input,
                                                                         discretemath.p_nor_q(p_input, q_input)))
                except ValueError:
                    print("Please enter an acceptable truth value, i.e. 0 or 1!")
    else:
        print("\nPlease enter a command from the command list!")
