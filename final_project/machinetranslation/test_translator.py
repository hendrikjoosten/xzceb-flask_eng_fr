import unittest

from translator import englishToFrench, frenchToEnglish

class TestenglishToFrench(unittest.TestCase): 
    def test1(self): 
        self.assertNotEqual(englishToFrench(2), 4) 
        self.assertEqual(englishToFrench(3.0), 9.0)  


class TestfrenchToEnglish(unittest.TestCase): 
    def test1(self): 
        self.assertNotEqual(frenchToEnglish(2), 4) 
        self.assertEqual(frenchToEnglish(-3.1), -6.2) 

unittest.main()