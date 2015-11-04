#!/usr/bin/env python

""" Assignment 2, Exercise 1, INF1340, Fall, 2015. Pig Latin

Test module for exercise1.py

"""

import pytest
import mock
from exercise1 import pig_latinify

word_starting_with_vowel = ["apple"]
word_starting_with_consonant = ["scratch"]
word_containing_alphanumeric = ["HE90LLO"]


def test_word_starting_with_vowel():
    for word in word_starting_with_vowel:
            assert pig_latinify("apple") == "appleyay"


def test_word_starting_with_vowel_2():
    for word in word_starting_with_vowel:
            assert pig_latinify("is") == "isyay"


def test_word_starting_with_consonant():
    for word in word_starting_with_consonant:
            assert pig_latinify("scratch") == "atchscray"


def test_word_containing_alphanumeric():
    for word in word_containing_alphanumeric:
        try:
            pig_latinify("HE90LLO")
        except AssertionError:
            assert True

if __name__ == "__main__":
    test_word_containing_alphanumeric()
    test_word_starting_with_consonant()
    test_word_starting_with_vowel()
    test_word_starting_with_vowel_2()