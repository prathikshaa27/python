def to_divide(third_number,fourth_number):
    assert fourth_number!=0
    return third_number/fourth_number
print(to_divide(10,2))
#print(to_divide(10,0))

import unittest

class TestExample(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("Setting up class...")

    @classmethod
    def tearDownClass(cls):
        print("Tearing down class")

    def setUp(self):
        print("Setting up test")

    def tearDown(self):
        print("Tearing down test")

    def test_example1(self):
        print("Running test example 1")
        self.assertEqual(1 + 1, 2)

    def test_example2(self):
        print("Running test example 2")
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()
