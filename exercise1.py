vowels = "aeiou"


def pig_latinify(word):
    """
    Main translator function.
    :param : string from function call
    :return: word in pig latin
    :raises:

    """

    # convert string to all lowercase
    word = word.lower()
    # if string has numbers -> error
    if not word.isalpha():
        result = "Please only enter alphabetic characters."
    # check if the first letter is a vowel
    elif word[0] in ("a", "e", "i", "o", "u"):
        result = word + "yay"
    # there is a vowel in the word somewhere other than the first letter
    elif check_for_any_vowels(word) == 1:
            index = get_first_vowel_position(word)
            word = word[index:] + word[0:index]
            result = word + "ay"
    # there are no vowels in the word
    else:
        if check_for_any_vowels(word) == 0:
            result = word + "ay"
    return result


def get_first_vowel_position(word):
    """
    Figures out where the first vowel is
    :param : word from pig_latinify
    :return: index of vowel
    :raises:

    """
    no_vowel = False
    if not no_vowel:
        for c in word:
            if c in vowels:
                return word.index(c)

def check_for_any_vowels(word):
        """
    Figures out if the word has any vowels
    :param : word from pig_latinify
    :return: 1 if any vowels, 0 if no vowerls
    :raises:

    """
        for c in vowels:
            if c in word:
                return 1
        return 0

#pig_latinify("apple")