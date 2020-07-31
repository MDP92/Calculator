import unittest
from calculator import Calculator





class TestCalculator(unittest.TestCase):
    def test_list_int(self):

        key = '4+9'
        ob = Calculator()
        ob.onPress(key=key)



        ob.insertedString = '4-8'
        print(ob.insertedString)
        print(type(ob.insertedString))
        result = ob.DisplayRealTimeValue()
        self.assertEqual(result, -4)

#        result = ob.DisplayFinalValue()

#        self.assertEqual(result, 6)

if __name__ == '__main__':
    unittest.main()