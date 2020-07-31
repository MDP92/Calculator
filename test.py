import unittest
from calculator import Calculator


class TestCalculator(unittest.TestCase):

    calculator = Calculator()

    def testOpenBracketsPress(self):
        self.calculator.buffer = ['(','(','(','(']
        self.calculator.openBrackets = ['(','(','(','(']
        key = '('
        self.calculator.onPress(key)
        self.assertEqual(self.calculator.buffer, ['(','(','(','(','('])
        self.assertEqual(len(self.calculator.openBrackets), 5)

    def testCloseBracketsPress(self):
        self.calculator.buffer = ['(','(',')',')']
        self.calculator.openBrackets = ['(','(']
        self.calculator.closeBrackets = [')',')']
        key = ')'
        self.calculator.onPress(key)
        self.assertEqual(self.calculator.buffer, ['(','(',')',')'])
        self.assertEqual(len(self.calculator.closeBrackets), 2)

    def testMultipliedPress(self):
        self.calculator.buffer = ['*','*']
        key = '*'
        self.calculator.onPress(key)
        self.assertEqual(self.calculator.buffer, ['*','*'])

    def testPlusPress(self):
        self.calculator.buffer = ['+']
        key = '+'
        self.calculator.onPress(key)
        self.assertEqual(self.calculator.buffer, ['+'])

    def testDividedPress(self):
        self.calculator.buffer = ['/']
        key = '/'
        self.calculator.onPress(key)
        self.assertEqual(self.calculator.buffer, ['/'])

    def testMinusPress(self):
        self.calculator.buffer = ['-']
        key = '-'
        self.calculator.onPress(key)
        self.assertEqual(self.calculator.buffer, ['-'])

    def testBackspacePress(self):
        self.calculator.buffer = ['4','.','3','-']
        key = 'Key.backspace'
        self.calculator.onPress(key)
        self.assertEqual(self.calculator.buffer, ['4','.','3'])

    def testDisplayExpression(self):
        self.calculator.buffer = ['7','.','1','*','4','-','8']
        expression = self.calculator.DisplayExpression()
        self.assertEqual(expression, '7.1*4-8')

    def testIntValue(self):
        self.calculator.insertedString = '4-8'
        realTimeResult = self.calculator.DisplayRealTimeValue()
        finalResult = self.calculator.DisplayFinalValue()
        self.assertEqual(realTimeResult, -4)
        self.assertEqual(finalResult, -4)

    def testFloatValue(self):
        self.calculator.insertedString = '5.3+7.9'
        realTimeResult = self.calculator.DisplayRealTimeValue()
        finalResult = self.calculator.DisplayFinalValue()
        self.assertEqual(realTimeResult, 13.2)
        self.assertEqual(finalResult, 13.2)

    def testNestedBrackets(self):
        self.calculator.insertedString = '(1.3+4.1)*(4/(8-14))'
        realTimeResult = self.calculator.DisplayRealTimeValue()
        finalResult = self.calculator.DisplayFinalValue()
        self.assertEqual(realTimeResult, -3.6)
        self.assertEqual(finalResult, -3.6)

    def testIncompleteExpression(self):
        self.calculator.insertedString = '4.3-'
        realTimeResult = self.calculator.DisplayRealTimeValue()
        finalResult = self.calculator.DisplayFinalValue()
        self.assertEqual(realTimeResult, None)
        self.assertEqual(finalResult, None)






if __name__ == '__main__':
    unittest.main()
