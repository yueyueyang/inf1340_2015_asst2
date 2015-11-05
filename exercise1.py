#!/usr/bin/env python

""" Assignment 2, Exercise 1, INF1340, Fall, 2015. Pig Latin

This module converts English words to Pig Latin words

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"


def pig_latinify(word):
    """
    takes input from user
    check IF there is a vowel at beginning
        do this
    ELSE
        do this
    print result

    :param :
    :return:
    :raises:

    """
    word = word.lower()
    if not word:
        result = "Please enter a word."
    elif word.isalpha() == False:
        result = "Please only enter alphabetic characters."
    elif word[0] in ("a", "e", "i", "o", "u"):
        result = word + "yay"
    elif word[0] not in ("a", "e", "i", "o", "u"):
            word = word[1:] + word[0]
            result = word + "ay"
    else:
        if ("a", "e", "i", "o", "u") not in word:
            count = len(word)
            for i in range(count):
                result = word[count-i-1] + "ay"
    return result

print pig_latinify("rhythm")
