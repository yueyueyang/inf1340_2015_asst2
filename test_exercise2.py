#!/usr/bin/env python

""" Assignment 2, Exercise 2, INF1340, Fall, 2015. DNA Sequencing

Test module for exercise2.py

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"

from exercise2 import find, multi_find


def test_find_basic():
    """
    Test find function.
    """
    assert find("This is an ex-parrot", "parrot", 0, 20) == 14


def test_find_basic():
    """
    Test find function.
    """
    assert find("abcdefg", "cd", 0, 100) == 2


def test_find_basic():
    """
    Test find function.
    """
    assert find("123456789", "7", 3, 100) == 6


def test_find_basic():
    """
    Test find function.
    """
    assert find("The weather is nice today", "7", 0, 1000) == -1


def test_multi_find_basic():
    """
    Test multi_find function.
    """
    assert multi_find("Ni! Ni! Ni! Ni!", "Ni", 0, 20) == "0,4,8,12"


def test_multi_find_basic():
    """
    Test multi_find function.
    """
    assert multi_find("How are you today", "Ni", 0, 100) == ""


def test_multi_find_basic():
    """
    Test multi_find function.
    """
    assert multi_find("How are you today", "o", 0, 20) == "1,9,13"