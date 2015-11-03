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
    if word.isalpha() == False:
        return AssertionError
    elif word[0] in ("a", "e", "i", "o", "u"):
        result = word + "yay"
    else:
        while word[0] not in ("a", "e", "i", "o", "u"):
            word = word[1:] + word[0]
            result = word + "ay"
    print(result)

#pig_latinify()