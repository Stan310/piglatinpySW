from unittest import TestCase
from translator import PigLatinTranslator

class TestPigLatinTranslator(TestCase):


    def test_get_phrase(self):
    # Test method example
        translator = PigLatinTranslator("hello world")
        phrase = translator.get_phrase()
        self.assertEqual("hello world", phrase)

    def test_translate_empty_phrase(self):
        translator = PigLatinTranslator("")
        translation = translator.translate()
        self.assertEqual("nil", translation)

    def test_translate_phrase_starting_with_vowel_ending_with_y(self):
        translator = PigLatinTranslator("any")
        translation = translator.translate()
        self.assertEqual("anynay", translation)

    def test_translate_phrase_starting_with_e_ending_with_y(self):
        translator = PigLatinTranslator("enemy")
        translation = translator.translate()
        self.assertEqual("enemynay", translation)

    def test_translate_phrase_starting_with_vowel_ending_with_vowel_not_y(self):
        translator = PigLatinTranslator ("umbrella")
        translation = translator.translate()
        self.assertEqual("umbrellayay", translation)

    def test_translate_phrase_starting_with_consonant(self):
        translator = PigLatinTranslator("pig")
        translation = translator.translate()
        self.assertEqual("igpay", translation)

    def test_translate_phrase_starting_with_more_consonants(self):
        translator = PigLatinTranslator("gni")
        translation = translator.translate()
        self.assertEqual("ignay", translation)


    def test_translate_phrase_starting_with_even_more_consonants(self):
        translator = PigLatinTranslator("spring")
        translation = translator.translate()
        self.assertEqual("ingspray", translation)

    def test_translate_consonants_only(self):
        translator = PigLatinTranslator("fly")
        translation = translator.translate()
        self.assertEqual("flyay", translation)

    def test_translate_phrase_with_more_words(self):
        translator = PigLatinTranslator("hello world")
        translation = translator.translate()
        self.assertEqual("ellohay orldway", translation)


    def test_translate_phrase_with_more_and_composite_words(self):
        translator = PigLatinTranslator("hello well-being")
        translation = translator.translate()
        self.assertEqual("ellohay ellway-eingbay", translation)

    def test_translate_phrase_with_more_and_punctuation(self):
        translator = PigLatinTranslator("hello well-being.")
        translation = translator.translate()
        self.assertEqual("ellohay ellway-eingbay.", translation)

    def test_translate_phrase_with_more_and_more_punctuation(self):
        translator = PigLatinTranslator("hello, well-being.")
        translation = translator.translate()
        self.assertEqual("ellohay, ellway-eingbay.", translation)