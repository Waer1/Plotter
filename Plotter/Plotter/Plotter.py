from PyQt5 import QtWidgets, uic, QtGui
from PyQt5.QtWidgets import QMainWindow,QPushButton, QLineEdit
import sys
from Plot import Plot
from ShowErrors import ShowError


## constructor to import the ui and plot it
class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()
        uic.loadUi('Plotter.ui', self)   
        ## connect plot Button with it function
        self.findChild(QPushButton,"PlotButton").clicked.connect(self.Plot)
        
        ## connect Clear Button with it function
        self.findChild(QPushButton,"Clear_Button").clicked.connect(self.Clear)
        
        ## text box that have the expression
        self.expression = self.findChild(QLineEdit,"Function")
        
        ## text box that have the Minmum value
        self.Min = self.findChild(QLineEdit,"MinValue")
        
        ## text box that have the Maxmum value
        self.Max = self.findChild(QLineEdit,"MaxValue")


    def Plot(self):
        try:
            ## create object of the Plot class that Draw the function
            Experssion = Plot(self.expression.text(), self.Min.text(),self.Max.text())
            ## Plot the function
            Experssion.PlotExpression()
        except ValueError as errmsg:
            ## while constructing or drawing if any error rised i recive it here and out message with its value
            ShowError(self, errmsg.args[0])
            self.Clear()
            return

    ## Clear function that reset the all feilds to empty 
    def Clear(self):
        self.expression.setText("")
        self.Min.setText("")
        self.Max.setText("")


if __name__ == "__main__":
    application = QtWidgets.QApplication(sys.argv)
    MainScreen = UI()
    MainScreen.show()
    sys.exit(application.exec_())
