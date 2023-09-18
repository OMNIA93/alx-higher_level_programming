import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    """Class TestBase"""

    def test_init(self):
        # Test the id value for the first instance of Base
        a = Base()
        self.assertEqual(a.id, 1)

        # Test the id value for the second instance of Base
        a1 = Base()
        self.assertEqual(a1.id, 2)

        # Test the id value for the third instance of Base
        a2 = Base()
        self.assertEqual(a2.id, 3)
    
        # Test the id value for the fourth instance of Base with a specific value
        a3 = Base(12)
        self.assertEqual(a3.id, 12)

        # Test the id value for the fifth instance of Base
        a4 = Base()
        self.assertEqual(a4.id, 4)

if __name__ == '__main__':
    unittest.main()
