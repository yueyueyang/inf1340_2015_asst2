import pytest
import mock
from exercise1 import pig_latinify

word_starting_with_vowel = ["apple"]
word_starting_with_consonant = ["scratch"]
word_containing_alphanumeric = ["HE90LLO"]
word_containing_nothing = [""]
word_with_no_vowels = ["rhythm"]


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

def test_word_containing_nothing():
    for word in word_containing_nothing:
        assert pig_latinify("") == "Please enter a word."


def test_word_with_no_vowels():
    for word in word_containing_nothing:
        assert pig_latinify("rhythm") == "mhtyhray"

if __name__ == "__main__":
    test_word_containing_alphanumeric()
    test_word_starting_with_consonant()
    test_word_starting_with_vowel()
    test_word_starting_with_vowel_2()
    test_word_containing_nothing()
    test_word_with_no_vowels()