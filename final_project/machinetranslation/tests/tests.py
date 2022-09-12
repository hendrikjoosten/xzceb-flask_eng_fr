import unittest

from translator import englishToFrench, frenchToEnglish

class TestEnglishToFrench(unittest.TestCase):
    def test1(self):
        self.assertIsNone(englishToFrench(None))
        self.assertEqual(englishToFrench('Hello'), 'Bonjour')
        self.assertNotEqual(englishToFrench('Bonjour'), 'Hello')

class TestFrenchToEnglish(unittest.TestCase):
    def test1(self):
        self.assertIsNone(frenchToEnglish(None))
        self.assertEqual(frenchToEnglish('Bonjour'), 'Hello')
        self.assertNotEqual(frenchToEnglish('Hello'), 'Bonjour')


if __name__ == '__main__':
    unittest.main()