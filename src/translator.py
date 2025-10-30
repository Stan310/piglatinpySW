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
            return self.phrase + "yay"
        elif first_letter in CONSONANTS:
            return self.phrase[1:-1] + self.phrase[-1] + self.phrase[0] + "ay"

    def translate_word_starting_with_vowel(word):
        last_letter = word[-1]