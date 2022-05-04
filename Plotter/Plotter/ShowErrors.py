from PyQt5.QtWidgets import QMessageBox

## show error msg when call it in Box
def ShowError(self, errMessage):
    QMessageBox.critical(self, "Error", errMessage)
