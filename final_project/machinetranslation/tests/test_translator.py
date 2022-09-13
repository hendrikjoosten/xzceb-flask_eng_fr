import unittest
from machinetranslation import translator

class TestTranslations(unittest.TestCase):
    def test_english_to_french_with_null_input(self):
        self.assertIsNone(translator.english_to_french(None))

    def test_english_to_french(self):
        self.assertEqual(translator.english_to_french("Hello"), "Bonjour")

    def test_french_to_english_with_null_input(self):
        self.assertIsNone(translator.french_to_english(None))

    def test_french_to_english(self):
        self.assertEqual(translator.french_to_english("Bonjour"), "Hello")

if __name__ == '__main__':
    unittest.main()