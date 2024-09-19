import unittest
from StringCalculator import add
class TestStringCalculator(unittest.TestCase):
        
        def test_expectZeroForEmptyInput(self):
                self.assertEqual(add(""), 0)
                
        def test_expectZeroForSingleZero(self):
                self.assertEqual(add("0"), 0)
                
        def test_expectSumForTwoNumberst(self):
                self.assertEqual(add("1,2"), 3)
                
        def test_ignoreNumbersGreaterThan1000(self):
                self.assertEqual(add("1,1001"), 1)
                
        def test_expectSumWithCustomDelimiter(self):
                self.assertEqual(add("//;\n1;2"), 3)
                
        def test_expectSumWithNewlineDelimiter(self):
                self.assertEqual(add("1\n2,3"),6);

        def test_negativeNumbersRaiseException(self):
                with self.assertRaises(ValueError) as context:
                    add("1,-2,-3") 
                self.assertIn("Negative numbers are not allowed", str(context.exception))

    # New test cases
        def test_ignoreInvalidDelimiter(self):
        # Test case TC8
                with self.assertRaises(ValueError):
                    add("//\n1 2")  # Invalid delimiter (spaces)

        def test_ignoreNumbersGreaterThan1000WithMultipleInputs(self):
        # Test case TC9
            self.assertEqual(add("5,100,2000"), 105)

        def test_negativeNumbersRaiseDetailedException(self):
        # Test case TC10
                 with self.assertRaises(ValueError) as context:
                    add("1,-5,3,-10")
                  self.assertIn("Negative numbers are not allowed: [-5, -10]", str(context.exception))

        def test_expectSumWithCustomDelimiterAmpersand(self):
        # Test case TC11
                  self.assertEqual(add("//&\n1&2&1000"), 1003)

        def test_newlineAsDelimiterWithTrailingComma(self):
        # Test case TC12
                 self.assertEqual(add("1,2,3,\n4"), 10)

        def test_emptyTokensCountAsZero(self):
        # Test case TC13
                 self.assertEqual(add("1,,2"), 3)

        def test_ignoreGreaterThan1000InCustomDelimiter(self):
        # Test case TC14
                 self.assertEqual(add("//;\n1;2;3;1001"), 6)

if __name__ == '__main__':
    unittest.main()


