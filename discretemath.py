# This docstring is for the class docstring, whenever the function point.__doc__ is ran, this will show up.
# This docstring should list the classes, functions, objects and exceptions that are imported when the module is imported.
# This docstring should also have one-line summaries for each item.

"""
Classes:

        Discretemath

Functions:
        
        cartesian_product(A, B)                         # Used
        binomial_theorem(x, y, n)                       # Used
        set_theory(A_element_count, B_element_count)    # Used
        prime_factorization(n)                          # Used
        nCr(n, r)                                       # Used
        nPr(n, r)                                       # Used
        GCD(a, b)                                       # Used
        LCM(a, b)                                       # Used
        isTruthValue(n)                                 # Used
        p_or_q(p, q)                                    # Used
        p_and_q(p, q)                                   # Used
        not_p(p)                                        # Used
        p_xor_q(p, q)                                   # Used
        p_nor_q(p, q)                                   # Used
        if_p_then_q(p, q)                               # Used
        powerSet(iterable)                              # Used
        create_power_set(aLi)                           # Used
        a_divides_b(a, b)                               # Used
        eulers_form(v, e)                               # Used
        handshaking_theorem(v=None, e=None, deg=None)   # Used
        S(n, k)                                         # Used
        number_of_functions(A, B, ftype="normal")       # Used  
        logistic_equation(x_0, r, iterate)              # Used
        ackermanns_function(m, n)                       # Used

Objects:

        A = {0}
        B = {0}
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
        feigenbaum_constant = 4.669
        constant_of_chaos = 3.57

Description:

        This module is for Discrete Mathematics, from set theory to prime factorization, this module has all of the tools you need
        to learn Discrete Mathematics. This module includes functions like binomial theorem, prime factorization, nCr, nPr, GCD, 
        LCM, and Set Theory.
        
"""

import numpy as np
import time
import math as m
from itertools import chain, combinations

A = {0}
B = {0}
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
feigenbaum_constant = 4.669
constant_of_chaos = 3.57

def isEven(n):
    if n % 2 == 0:
        return True
    else:
        return False


# Cartesian Product
def cartesian_product(A, B):
    A = sorted(A)
    B = sorted(B)
    print("Processing", end='')
    for i in range(4):
        time.sleep(1)
        print(".", end='')
    print()
    time.sleep(1)
    for a in A:
        print()
        for b in B:
            print("({0}, {1})".format(a, b), end="\t")
    print("\n")


# Binomial Theorem
def binomial_theorem(x, y, n):
    """
    The binomial theorem is defined as (x + y)^n = sum_k=0^n(nCr(n, k))*x^(n-k)*y^k = sum_k=0^n(nCr(n, k))x^n*y^(n-k).
    The binomial theorem tells us how to expand expressions of the form (x + y)^n.
    This function will run through the binomial theorem and return the expansion.

    (x, y and n: int) -> int

    returns f

    >>> binomial_theorem(1, 5, 5)
    poly1d([   1,   25,  250, 1250, 3125, 3125])
    """
    f = 1
    for i in range(n):
        fx_i = np.poly1d([x, y])
        f *= fx_i
    return f


# Set Theory
def set_theory(A_element_count, B_element_count):
    """
    This function does various set theory problems

    (A_element_count, B_element_count: int) -> None

    returns None
    """
    a = ''
    b = ''
    for i in range(A_element_count):
        A_element = int(input("Enter element {0}: ".format(i + 1)))
        a += str(A_element)
        A.add(A_element)
        if 0 in A:
            A.remove(0)
        else:
            pass

    for i in range(B_element_count):
        B_element = int(input("Enter element {0}: ".format(i + 1)))
        b += str(B_element)
        B.add(B_element)
        if 0 in B:
            B.remove(0)
        else:
            pass

    print("\nA is the set {0}\nB is the set {1}".format(A, B))
    print()
    print("The union of the set A and the set B is {0}".format(A.union(B)))
    print()
    if A.intersection(B) == set():
        print("The intersection of the set A and the set B has no elements\n")
    else:
        print("The intersection of the set A and the set B is {0}\n".format(A.intersection(B)))
    print("The powerset of A is {0}".format(create_power_set(powerSet(a))))
    print()
    print("The powerset of B is {0}".format(create_power_set(powerSet(b))))
    print()

    print("Cartesian Product: ")
    print()
    cartesian_product(A, B)


# Prime Factorization
def prime_factorization(n):
    """
    This function finds the prime factorization of a number.

    returns None
    """
    lower = 2
    for num in range(lower, n + 1):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                if num not in primes:
                    primes.append(num)
    print("The prime factorizations of {0} is: ".format(n), end="")
    i = 0
    while n > 1:
        if n % primes[i] == 0:
            n /= primes[i]
            print(primes[i], end=" ")
            continue
        else:
            i += 1
    print()


# Combinations
def nCr(n, r):
    """
    Using the function C(n,r) = n! / r!(n-r)!
    We write a function that can instantly figure out the
    value for n choose r.

    (n, r: int) -> int

    returns int(value)

    >>> nCr(10, 2)
    45
    """
    value = m.factorial(n) / (m.factorial(r) * m.factorial(n - r))
    return int(value)


# Permutations
def nPr(n, r):
    """
    Using the function P(n,r) = n! / (n-r)!
    We write a function that can instantly figure out the
    value for n permutation r.

    (n, r: int) -> int

    returns int(value)

    >>> nPr(10, 2)
    90
    """
    value = m.factorial(n) / (m.factorial(n - r))
    return int(value)


# Greatest Common Divisor
def GCD(a, b):
    """
    This function finds the greatest common divisor for a and b.

    (a, b: int) -> int

    returns gcd

    >>> GCD(69, 43)
    1
    """
    while b != 0:
	    r = a % b
	    a = b
	    b = r
    return a


# Least Common Multiplier
def LCM(a, b):
    """
    This function finds the least common multiplier for a and b.

    (a, b: int) -> float

    returns lcm

    >>> LCM(10, 20)
    20.0
    """
    lcm = (a * b) / GCD(a, b)
    return lcm


# Check if it's a truth value (0 or 1)
def isTruthValue(n):
    """
    This function checks if the value n is a
    truth value (either 0 or 1).

    (n: int) -> bool

    returns True or False

    >>> isTruthValue(1)
    True
    >>> isTruthValue(9)
    False
    """
    if (n == 0) or (n == 1):
        return True
    else:
        return False 


# P or Q
def p_or_q(p, q):
    """
    This function returns the value for p or q.
    0 = False or inactive
    1 = True or active

    (p, q: int) -> int

    returns 0 or 1

    >>> p_or_q(0, 0)
    0
    """
    if isTruthValue(p) and isTruthValue(q) == True:
        return p or q
    else:
        raise ValueError("An integer greater than 1 or less than 0 is not a truth value!")


# P and Q
def p_and_q(p, q):
    """
    This function returns the value for p and q.
    0 = False or inactive
    1 = True or active

    (p, q: int) -> int

    returns 0 or 1
    
    >>> p_and_q(0, 0)
    0
    """
    if isTruthValue(p) and isTruthValue(q) == True:
        return p and q
    else:
        raise ValueError("An integer greater than 1 or less than 0 is not a truth value!")


# Not P
def not_p(p):
    """
    This function returns the value for not p.
    0 = False or inactive
    1 = True or active

    (p: int) -> int

    returns 0 or 1
    
    >>> not_p(1)
    0
    """
    if isTruthValue(p) is True:
        if p is False:
            return 1
        else:
            return 0
    else:
        raise ValueError("An integer greater than 1 or less than 0 is not a truth value!")


# P xor Q
def p_xor_q(p, q):
    """
    This function returns the value for p xor q.
    0 = False or inactive
    1 = True or active

    (p, q: int) -> int

    returns 0 or 1
    
    >>> p_xor_q(0, 0)
    0
    """
    if isTruthValue(p) and isTruthValue(q) is True:
        return p ^ q
    else:
        raise ValueError("An integer greater than 1 or less than 0 is not a truth value!")


# P nor Q     
def p_nor_q(p, q):
    if isTruthValue(p) and isTruthValue(q) is True:
        return not p and not q
    else:
        raise ValueError("An integer greater than 1 or less than 0 is not a truth value!")


# If P, then Q. P implies Q
def if_p_then_q(p, q):
    """
    This function returns the value for if p then q.
    0 = False or inactive
    1 = True or active

    (p, q: int) -> int

    returns 0 or 1

    >>> if_p_then_q(1, 1)
    """
    if isTruthValue(p) and isTruthValue(q) is True:
        if p == 0:
            return 1
        if p == 1:
            if q == 1:
                return 1
            else:
                return 0
    else:
        raise ValueError("An integer greater than 1 or less than 0 is not a truth value!")


# Initiate Power Set
def powerSet(iterable):
    """
    Initiate the Power Set
    """
    try:
        assert type(iterable) == str
    except AssertionError:
        if type(iterable) == set:
            raise TypeError("<class 'set'> does not work with powerset custom function.")
        if type(iterable) == tuple:
            raise TypeError("<class 'tuple'> does not work with powerset custom function.")
        if type(iterable) == list:
            raise TypeError("<class 'list'> does not work with powerset custom function.")
        if type(iterable) == dict:
            raise TypeError("<class 'dict'> does not work with powerset custom function.")
        else:
            iterable = str(iterable)
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s) + 1))


# Create Power Set
def create_power_set(aLi):
    """
    Create the Power Set as a list

    (aLi: list) -> list

    returns powerList

    >>> aLi = '123'
    >>> psetLi = list(powerSet(aLi))
    >>> create_power_set(psetLi)
    [('0',), ('1',), ('2',), ('3',), ('1', '2'), ('1', '3'), ('2', '3'), ('1', '2', '3')]
    """
    powerList = [(tuple('0', ))]
    for item in aLi:
        powerList.append(item)
    powerList.remove(())
    return powerList


# A divides B
def a_divides_b(a, b):
    """
    a divides b means that there exists
    an integer 'n' such that b = a * n.

    (x, y: int) -> int and/or bool

    returns False or b//a and True

    >>> a_divides_b(1, -2)
    '-2
    True'
    """
    assert type(a) and type(b) is int
    if b % a != 0:
        return False
    else:
        return f"{b // a}\n{True}"


# Euler's Formula
def eulers_form(v, e):
    """
    Let G be a connected planar simple graph with e edges and v vertices.
    Let r be the number of regions in a planar representation of G.
    Then r = e - v + 2.

    (v, e: int) -> int

    returns r
    """
    assert e >= v - 2, "e must be greater than or equal to v - 2!"
    r = e - v + 2
    return r


# Handshaking Theorem
def handshaking_theorem(v=None, e=None, deg=None):
    """
    Let G = (V, E) be an undirected graph, then 2*|E| = sum_{v \in V} deg(v)

    (v, e, deg: int) -> int

    returns v, e, deg # Depends on what is defined

    >>> handshaking_theorem(None, 16, 4)
    8
    """
    if v is None:
        if isEven(e) is True and isEven(deg) is True:
            v = (2 * e) / deg
            return int(v)
        else:
            raise OSError("Unfortunately, this function hasn't implemented odd degrees or odd amount of edges yet!")
    elif e is None:
        if isEven(v) is True and isEven(deg) is True:
            e = (v * deg) / 2
            return int(e)
        else:
            raise OSError("Unfortunately, this function hasn't implemented odd degrees or odd amount of edges yet!")
    else:
        if isEven(v) is True and isEven(e) is True:
            deg = (2 * e) / v
            return int(deg)
        else:
            raise OSError("Unfortunately, this function hasn't implemented odd degrees or odd amount of edges yet!")


# Stirling's Number of the second kind
def S(n, k):
    """
    This function represents Stirling's Number,
    Stirling's Number is used for various things in combinatorics,
    The main thing that this equation is used for is to find the number
    of onto functions there are from f:A ---> B.
    
    Desmos Code: 
    S\left(n,k\right)=
    \frac{1}{k!}\sum_{i=0}^{k}\left(-1\right)^{i}\operatorname{nCr}\left(k,i\right)\left(k-i\right)^{n}

    (n, k: int) -> float

    returns x

    >>> S(9, 3)
    3025.0
    """
    x = 0
    prod = 1 / m.factorial(k)
    for i in range(k):
        summation = m.pow(-1, i) * nCr(k, i) * m.pow((k - i), n)
        x += summation
    x *= prod
    return x


# Number of Functions from A to B
def number_of_functions(A, B, ftype="normal"):
    """
    This function finds the number of functions from A to B given the type
    of function, the size of A and the size of B.

    (A, B: int) -> int

    returns int

    >>> number_of_functions(3, 4, "one-to-one")
    24.0
    >>> number_of_functions(4, 3, "one-to-one")
    0
    """
    if ftype == "normal":
        return B ** A
    if ftype == "one-to-one":
        if A < B:
            return m.factorial(B) / m.factorial(B - A)
        elif A == B:
            return m.factorial(B)
        else:
            return 0
    if ftype == "onto":
        return m.factorial(B) * S(A, B)
    if ftype == "one-to-one correspondence":
        if A == B:
            return m.factorial(A)
        else:
            return f"These set's do not make a one-to-one correspondence!"


# May's Logicstic Equation
def logistic_equation(x_0, r, iterate):
    """
    May's Logistic Equation simulates chaos

    (x_0, r: float, iterate: int) -> list

    returns li

    >>> logistic_equation(0.4, constant_of_chaos, 10)
    [0.8567999999999999, 0.43801672320000024, 0.8787843220277705, 0.38028510146788536, 0.8413359847579203,
    0.4765583914683468, 0.8905382528323319, 0.34800314687657047, 0.8100221352068512, 0.5493740041839721,
    0.8837970815277028]
    """
    x = 0
    li = []
    x_1 = r * x_0 * (1 - x_0)
    x_i = x_1
    li.append(x_i)
    for i in range(iterate):
        x_n = r * x_i * (1 - x_i)
        x_i = x_n
        li.append(x_i)
    for item in li:
        x += item
    return li


# Ackermann's function
def ackermanns_function(m, n):
    """
    In computability theory, the Ackermann function,
    named after Wilhelm Ackermann, is one of the simplest
    and earliest-discovered examples of a total computable
    function that is not primitive recursive because it grows
    at too quick of a rate.

    (m, n: int) -> int

    returns n + 1

    >> ackermanns_function(2, 3)
    9
    """
    if m == 0:
        return n + 1
    if n == 0:
        return ackermanns_function(m - 1, 1)
    else:
        return ackermanns_function(m - 1, ackermanns_function(m, n - 1))


if __name__ == "__main__":
    print(np.array([[0, 0, p_and_q(0, 0), not_p(0), p_or_q(0, not_p(0))], 
                    [0, 1, p_and_q(0, 1), not_p(0), p_or_q(0, not_p(0))], 
                    [1, 0, p_and_q(1, 0), not_p(0), p_or_q(1, not_p(0))],
                    [1, 1, p_and_q(1, 1), not_p(1), p_or_q(1, not_p(1))]]))
    print(binomial_theorem(1, 1, 10))
    print(GCD(0, 45))

