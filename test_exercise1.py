import pytest
import mock
from exercise1 import pig_latinify

#####################
# STRING VARIABLES ##
#####################

word_starting_with_vowel = ["apple"]
word_starting_with_consonant = ["scratch"]
word_containing_alphanumeric = ["HE90LLO"]
word_containing_nothing = [""]
word_with_no_vowels = ["rhythm"]

###################
# TEST FUNCTIONS ##
###################

def test_basic():
    """
    Basic test cases from assignment hand out
    """
    assert pig_latinify("dog") == "ogday"
    assert pig_latinify("scratch") == "atchscray"
    assert pig_latinify("is") == "isyay"
    assert pig_latinify("apple") == "appleyay"


def test_word_containing_alphanumeric():
    """
    Tests alphanumeric input
    """
    for word in word_containing_alphanumeric:
        try:
            pig_latinify("HE90LLO")
        except TypeError:
            assert True

def test_word_with_no_vowels():
    """
    tests words with no vowels
    """
    for word in word_with_no_vowels:
        assert pig_latinify("rhythm") == "rhythmay"

