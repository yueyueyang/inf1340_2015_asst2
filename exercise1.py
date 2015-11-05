vowels = "aeiou"

#main translator function
def pig_latinify(word):

    #convert string to all lowercase
    word = word.lower()
    #if string is empty -> error
    if not word:
        result = "Please enter a word."
    #if string has numbers -> error
    elif not word.isalpha():
        result = "Please only enter alphabetic characters."
    #check if the first letter is a vowel
    elif word[0] in ("a", "e", "i", "o", "u"):
        result = word + "yay"
    #there is a vowel in the word somewhere other than the first letter
    elif check_for_any_vowels(word) == 1:
            index = get_first_vowel_position(word)
            word = word[index:] + word[0:index]
            result = word + "ay"
    #there are no vowels in the word
    else:
        if check_for_any_vowels(word) == 0:
            result = word[::-1] + "ay"
    print result

#figures out where the first vowel is
def get_first_vowel_position(word):
    no_vowel = False
    if not no_vowel:
        for c in word:
            if c in vowels:
                return word.index(c)

#checks if function has vowels in it
def check_for_any_vowels(word):
    for c in vowels:
        if c in word:
            return 1
    return 0

pig_latinify("apple")