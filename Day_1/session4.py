a = 5
b = 6

print((a + b)/2)

abc = None

if(abc != "" and abc != None):
    print(abc * 5)

import unittest
class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        # YOur own Code
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('FOO'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()