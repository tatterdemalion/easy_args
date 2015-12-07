import sys
import unittest

from easy_args import args_get


class TestArgDecorators(unittest.TestCase):
    def test_parse(self):
        sys.argv = ['prog.py', 'hello', 'dude', 'name=John', 'lastname=Doe']
        with args_get as a:
            self.assertIsNotNone(a.args)
            self.assertIsNotNone(a.kwargs)
            self.assertEqual(a.name, 'John')
            self.assertIn('hello', a.args)

if __name__ == '__main__':
    unittest.main()
