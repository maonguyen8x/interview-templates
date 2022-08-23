from curses.ascii import isupper
import unittest
from coding_challenge import say_hello


class CodingChallengeTests(unittest.TestCase):
    """ Unit tests for the coding challenge """

    def test_say_hello(self):
        """Dummy test (delete me)"""
        self.assertEqual(say_hello(), 'Hello')
        # This test will fail if method: say_helllo()  doesn't return anything
        self.assertIsNotNone(say_hello())
        # This test will fail if the method: say_helllo() instance is not the same as that of the class "str"
        self.assertIsInstance(say_hello(), str)
        # Returns True if the string is in uppercase
        # else returns False
        self.assertTrue(say_hello(), 'Hello'.isupper())
        self.assertTrue(say_hello(), 'Hello'.islower())
        # Returns True if say_hello() is capitalize
        self.assertTrue(say_hello().capitalize)
        # Returns False if say_hello() is difference from 'Hello'
        self.assertNotEqual(say_hello(), 'Hi')
        self.assertNotEqual(say_hello(), False)
        self.assertNotEqual(say_hello(), True)


if __name__ == '__main__':
    unittest.main()
