# =========================================================================== #
#                               test_example.py                               #
# =========================================================================== #

"""Unit Testing the 'example' module"""

# =========================================================================== #
#                                   Imports                                   #
# =========================================================================== #

import unittest
from rita import example

# =========================================================================== #
#                               Unit Test Case                                #
# =========================================================================== #

class TestExample(unittest.TestCase):
    def test_add(self) -> None:
        self.assertEqual(example.add(10, 5), 15)
        self.assertEqual(example.add(-1, 1), 0)
        self.assertEqual(example.add(-1, -1), -2)

    def test_subtract(self) -> None:
        self.assertEqual(example.subtract(10, 5), 5)
        self.assertEqual(example.subtract(-1, 1), -2)
        self.assertEqual(example.subtract(-1, -1), 0)
    
    def test_multiply(self) -> None:
        self.assertEqual(example.multiply(10, 5), 50)
        self.assertEqual(example.multiply(-1, 1), -1)
        self.assertEqual(example.multiply(-1, -1), 1)
    
    def test_divide(self) -> None:
        self.assertEqual(example.divide(10, 5), 2)
        self.assertEqual(example.divide(-1, 1), -1)
        self.assertEqual(example.divide(-1, -1), 1)
        self.assertEqual(example.divide(5, 2), 2.5)

        with self.assertRaises(ValueError):
            example.divide(10, 0)

# =========================================================================== #
#                               __name__ Guard                                #
# =========================================================================== #

if __name__ == "__main__":
    unittest.main()
