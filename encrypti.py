"""
Classes:

        Encrypti

Functions:

        caesar_cipher(n, string)            # Used
        bin_translator(str)                 # Used
        hex_translator(str)                 # Used


Objects:

        capital_letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R",
                            "S", "T", "U", "V", "W", "X", "Y", "Z"]
        lowercase_letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r",
                            "s", "t", "u", "v", "w", "x", "y", "z"]
        lc = len(capital_letters) - 1
        ll = len(lowercase_letters) - 1


Description:

        This module includes caesar cipher, reverse cipher, binary translator, hexadecimal, randi encoding.
"""
import random as rand

capital_letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
                   "U", "V", "W", "X", "Y", "Z"]
lowercase_letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                     "u", "v", "w", "x", "y", "z"]

lc = len(capital_letters) - 1
ll = len(lowercase_letters) - 1


def caesar_cipher(n, string):
    """
    Caesar Cipher.

    returns None
    """
    if n > 26:
        n %= 26
    for letter in string:
        if letter in capital_letters:
            if ((capital_letters.index(letter)) + n) > lc:
                print(capital_letters[((capital_letters.index(letter)) + n) - len(capital_letters)], end="")
            else:
                print(capital_letters[(capital_letters.index(letter)) + n], end="")
        elif letter in lowercase_letters:
            if ((lowercase_letters.index(letter)) + n) > ll:
                print(lowercase_letters[((lowercase_letters.index(letter)) + n) - len(lowercase_letters)], end="")
            else:
                print(lowercase_letters[(lowercase_letters.index(letter)) + n], end="")
        else:
            print(letter, end="")
    print()


# Binary Translator
def bin_translator(str):
    """
    This function translates a string to binary.

    returns None
    """
    r = " "
    for s in str:
        dec_version = ord(s)
        if len(bin(dec_version)[2::]) < 8:
            bin_ver = "0" * (8 - len(bin(dec_version)[2::])) + bin(dec_version)[2::]
            print(bin_ver, end=" ")
        else:
            print(bin(dec_version)[2::], end=" ")
    print(r)


# Hexadecimal Translator
def hex_translator(str):
    """
    This function translates a string to hexadecimal.

    returns None
    """
    r = " "
    for s in str:
        dec_version = ord(s)
        print(dec_version, end=" ")
    print(r)


if __name__ == "__main__":
    bin_translator("Hello, World!")
