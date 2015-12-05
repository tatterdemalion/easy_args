import sys
import unittest

from easy_args import parse


class TestArgDecorators(unittest.TestCase):
    def test_parse(self):
        sys.argv = ['prog.py', 'hello', 'dude', 'name=John', 'lastname=Doe']
        self.assertIn('hello', parse()[0])
        self.assertEqual(parse()[1]['lastname'], 'Doe')

if __name__ == '__main__':
    unittest.main()
