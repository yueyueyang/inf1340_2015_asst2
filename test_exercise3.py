#!/usr/bin/env python

""" Assignment 2, Exercise 3, INF1340, Fall, 2015. DBMS

Test module for exercise3.py

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"

import pytest
import mock
from exercise3 import union, intersection, difference


###########
# TABLES ##
###########
GRADUATES = [["Number", "Surname", "Age"],
             [7274, "Robinson", 37],
             [7432, "O'Malley", 39],
             [9824, "Darkes", 38]]

MANAGERS = [["Number", "Surname", "Age"],
            [9297, "O'Malley", 56],
            [7432, "O'Malley", 39],
            [9824, "Darkes", 38]]

PROFESSORS = [["Number", "Surname", "Age", "Gender"],
             [7274, "Robinson", 37],
             [7432, "O'Malley", 39],
             [9824, "Darkes", 38],
             [4343, "Susan", 35]]

FACULTY_ADMINISTRATION = [["Number", "Name", "Age"],
             [7274, "Robinson", 37],
             [7432, "O'Malley", 39],
             [9824, "Darkes", 38]]

CLASSES = [["Number", "Surname", "Age"],
             ["Math", 1003, 55],
             ["English", 1340, 54],
             ["Science", 1341, 50]]

STUDENTS = [["Number", "Surname", "Age"],
             [7274, "Robinson", 37],
             [7432, "O'Malley", 39],
             [9824, "Darkes", 38]]


from exercise3 import union, intersection, difference


#####################
# HELPER FUNCTIONS ##
#####################


def is_equal(t1, t2):
    return sorted(t1) == sorted(t2)


###################
# TEST FUNCTIONS ##
###################


def test_intersection():
    """
    Test intersection function and show all unique rows from t1 and t2

    """
    result = [["Number", "Surname", "Age"],
              [7432, "O'Malley", 39],
              [9824, "Darkes", 38]]

    assert is_equal(result, intersection(GRADUATES, MANAGERS))

    result2 = []
    assert is_equal(result2, intersection(GRADUATES, CLASSES))

    result3 = [['Number', 'Surname', 'Age'], [7274, 'Robinson', 37], [7432, "O'Malley", 39], [9824, 'Darkes', 38]]
    assert is_equal(result3, intersection(GRADUATES, STUDENTS))

def test_union():
    """
    Test union operation and checks for duplicates.
    """

    result = [["Number", "Surname", "Age"],
              [7274, "Robinson", 37],
              [9297, "O'Malley", 56],
              [7432, "O'Malley", 39],
              [9824, "Darkes", 38]]

    assert is_equal(result, union(GRADUATES, MANAGERS))

    result2 = [["Number", "Surname", "Age"], [7274, "Robinson", 37], [7432, "O'Malley", 39], [9824, "Darkes", 38]]
    assert is_equal(result2, union(GRADUATES, STUDENTS))


def test_lengths_equal():
    """
    This is a function that tests if the table column lengths are equal
    """
    with pytest.raises(Exception):
        union(PROFESSORS, GRADUATES)


def test_names_equal():
    """
    A function that tests if the names of the columns are equal
    """
    with pytest.raises(Exception):
        union(FACULTY_ADMINISTRATION, GRADUATES)


def test_difference():
    """
    Test difference operation and shows all unique rows in Graduates
    """

    result = [["Number", "Surname", "Age"],
              [7274, "Robinson", 37]]
    assert is_equal(result, difference(GRADUATES, MANAGERS))

    result2 = []
    assert is_equal(result2, intersection(GRADUATES, CLASSES))



