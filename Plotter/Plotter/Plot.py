import matplotlib.pyplot as plt 
import numpy as np
import Validation as Validation
import re
import sys

class Plot:
    ## constructor that call the validation checks
    def __init__(self, exp, Min, Max):
        self.expression, self.minValue, self.maxValue = Validation.validentries(exp,Min,Max)


    ## evaluating the value exoression with x
    def Function(self, x):
        return eval(self.expression)

    ## loop throught range to get values of function
    def generateExpression(self):
        xList = []
        yList = []
        for i in range(self.minValue, self.maxValue):
            xList.append(i)
            try:
                Y = self.Function(i)
                yList.append(self.Function(i))
            except ZeroDivisionError:
                yList.append(float('inf'))

        return xList, yList

    ## the actual function that plot expression
    def PlotExpression(self):
        ## variable that hold x values and its corresponding y values
        xList, yList = self.generateExpression()
        plt.plot(xList, yList, color="black", linewidth=1, label = self.expression)
        plt.xlabel("X")
        plt.ylabel("Y = F(X)")
        plt.style.use("seaborn-dark")
        plt.show()
