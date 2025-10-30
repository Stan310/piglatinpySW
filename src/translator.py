from error import PigLatinError
CONSONANTS = "bcdfghjklmnpqrst"
VOWELS = "aeiouy"
class PigLatinTranslator:

    def __init__(self, phrase: str):
        """
        Creates a pig latin translator given a phrase.
        :param phrase: the phrase.
        :raise PigLatinError: for any error situation.
        """
        self.phrase = phrase
    def get_phrase(self) -> str:
        """
        Returns the phrase.
        :return: the phrase.
        """
        return self.phrase
    def translate(self) -> str:
        """
        Returns the Pig Latin translation of the phrase.
        :return: the translation.
        """
        if self.phrase == "":
            return "nil"
        first_letter = self.phrase[0]
        last_letter = self.phrase[-1]
        if first_letter in VOWELS and last_letter == "y":
            return self.phrase + "nay"
        elif first_letter in VOWELS and last_letter in "aeiou":
            return translate_phrase_starting_with_vowel(self.phrase)
        elif first_letter in CONSONANTS:
         return translate_phrase_starting_with_consonant(self.phrase)
        return "No translation"


def translate_phrase_starting_with_consonant(word):

    first_letter = word[0]
    substring = word[1:]
    return substring + first_letter + "ay"



def translate_phrase_starting_with_vowel(word):
    last_letter = word[-1]
    if last_letter == "y":
        return word + "nay"
    elif last_letter in VOWELS:
        return word + "yay"
    else:
        return word + "ay"
