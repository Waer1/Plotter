import unittest
import Validation as Validation

class MyTestCase(unittest.TestCase):
    def testvalidateExpression(self):
        self.assertRaises(ValueError, Validation.validateExpression, "")
        self.assertRaises(ValueError, Validation.validateExpression, "x+1-")
        self.assertRaises(ValueError, Validation.validateExpression, "-1+2/x^")
        self.assertEqual("3+2*x-3*x**2+4/x**3", Validation.validateExpression("1+2*x-3*X^2 + 4 / X^3"))

    def testvalidateInt(self):  
        self.assertRaises(ValueError, Validation.validateInt ,"")
        self.assertRaises(ValueError, Validation.validateInt, "xassa")
        self.assertRaises(ValueError, Validation.validateInt, "123x")

    def testValidateMaxMinValues(self):
        self.assertRaises(ValueError, Validation.validateMaxMinValues,-10, -20)
        self.assertRaises(ValueError, Validation.validateMaxMinValues, 10, 0)

    def testValidateDivisionByZero(self):
        self.assertRaises(ValueError, Validation.validateDivisionByZero,"1/x", -5, 10)        
        self.assertRaises(ValueError, Validation.validateDivisionByZero,"1/x^2", 0, 10)       
        self.assertRaises(ValueError, Validation.validateDivisionByZero,"10/x^3", -10, 10)       
        self.assertAlmostEqual(1,Validation.validateDivisionByZero,"1/x", 1, 10)      
        self.assertAlmostEqual(1, ValueError, Validation.validateDivisionByZero,"3+x-5*x^3", -100, 100)    

if __name__ == '__main__':
    unittest.main()
