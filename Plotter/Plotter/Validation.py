import re
import sys

## function used to check on all input and any probability to out error e.g DivisionByZero 
def validentries(expression , Min, Max):
        ## convert the string values to int
        Min = validateInt(Min) 
        Max = validateInt(Max)
        ## check that min is small than max
        validateMaxMinValues(Min,Max)
        return validateExpression(expression) , validateInt(Min), validateInt(Max)

## check for validation of expression
def validateExpression(expression):
    ## out all spaces first
    expression = expression.replace(" ", "")
    ## if no thing has been wroten or write only spacess
    if expression == "":
        raise ValueError("Empty Expression, No thing to Plot")
    
    ## match expression with regex
    toMatch = "(-)?(\d+$)|((-)?(\d+[+-])?(\d+[\*\/])?[xX](\^\d+)?([+-](\d+)?([\*\/][xX](\^\d+)?)?)*)*$"
    matched = re.match(toMatch, expression)
    if not matched:
        raise ValueError("Invalid Expression")
    
    expression = expression.replace('^', '**').replace('X', 'x')
    return expression

## return int of string or rasie error
def validateInt(strNum):
    try:
        num = int(strNum)
        return num
    except:
        raise ValueError("please enter valid min and max values ")

## Min & max Validation
def validateMaxMinValues(minValue, maxValue):
    if minValue >= maxValue:
        raise ValueError("Wrong in Max and Min Values")

##  DivisionByZero Validation
def validateDivisionByZero(expression, minValue, maxValue):
    if expression.find('/X') != -1 or expression.find('/x') != -1 and minValue <= 0 and maxValue >= 0:
        raise ValueError("Division By Zero!!!")
    return 1