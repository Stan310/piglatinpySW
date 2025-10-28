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
        self.assertEqual(None, translation)