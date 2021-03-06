#!/usr/bin/env python

""" Assignment 2, Exercise 2, INF1340, Fall, 2015. DNA Sequencing

This module converts performs substring matching for DNA sequencing

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"


def find(input_string, substring, start, end):
    """
    Searching for the index of the object string.
    :param : input_string - from function call, larger string
    :param : substring - from function call, string that we are looking for
    :param : index where first character of substring can be found
    :return: index where the last character of substring can be found
    :raises:

    """
    # calculate the lengths of input string and substring.
    input_length = len(input_string)
    search_length = len(substring)

    # Test if the length between end and search is less than the length of start string.
    if end - search_length < start:
        return -1

    # Test if the length of start string is greater than the length of input string.
    if start > input_length:
        return -1

    # Test if the length of end is greater or equal to the length of input string.
    if end >= input_length:

        # Search for the occurrence of object string.
        for i in range(start, input_length):
            if input_string[i:i+search_length] == substring:
                return i
    return -1


def multi_find(input_string, substring, start, end):
    """
    Searching for the start,end indexes of the object string.
    :param : input_string - from function call, larger string
    :param : substring - from function call, string that we are looking for
    :param : 0 or more indexes where first character of substring can be found
    :param : 0 or more indexes where last character of substring can be found
    :return: index[start, end]
    :raises:

    """
    # calculate the lengths of input string and substring.
    input_length = len(input_string)
    search_length = len(substring)
    output_string = ""

    real_end = end

    # Test if the length between end and search is less than the length of the start string.
    if end - search_length < start:
        return output_string

    # Test if the length of start string is greater than the length of input string.
    if start > input_length:
        return output_string

    # Test if the length of end is greater or equal to the length of input string.
    if end >= input_length:
        real_end = input_length

    # Search for multi occurrence of object string.
    for i in range(start, real_end - search_length + 1):
        if input_string[i:i+search_length] == substring:
            output_string += "," + str(i)

    if output_string != "":
        output_string = output_string[1:]
    return output_string

#find()
#multi_find()

