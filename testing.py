import unittest

def to_add(first_number,second_number):
    return first_number+second_number

class TestAddFunction(unittest.TestCase):
    def test_add_positive_numbers(self):
        self.assertEqual(to_add(2, 3), 5)
    def test_add_negative_numbers(self):
        self.assertEqual(to_add(-2, -3), -5) 
    def test_add_zero_to_number(self):
        self.assertEqual(to_add(5, 0), 5) 

if __name__ == '__main__':
    unittest.main()

#assert statement
def to_divide(third_number,fourth_number):
    assert fourth_number!=0
    return third_number/fourth_number
print(to_divide(10,2))
print(to_divide(10,0))
