import unittest
from translator import englishToFrench, frenchToEnglish

class TestTranslator(unittest.TestCase):

    def test_english_to_french(self):
        self.assertEqual(englishToFrench('Hello'), 'Bonjour')
        self.assertEqual(englishToFrench(''), None)

    def test_french_to_english(self):
        self.assertEqual(frenchToEnglish('Bonjour'), 'Hello')
        self.assertEqual(frenchToEnglish(''), None)


if __name__ == '__main__':
    unittest.main()