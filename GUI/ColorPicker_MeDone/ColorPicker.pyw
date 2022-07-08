import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox

#ADD IMPORT STATEMENT FOR YOUR GENERATED UI.PY FILE HERE
import Ui_ColorPicker
#      ^^^^^^^^^^^ Change this!

#CHANGE THE SECOND PARAMETER (Ui_ChangeMe) TO MATCH YOUR GENERATED UI.PY FILE
class MyForm(QMainWindow, Ui_ColorPicker.Ui_MainWindow):
#                         ^^^^^^^^^^^   Change this!

    # DO NOT MODIFY THIS CODE
    def __init__(self, parent=None):
        super(MyForm, self).__init__(parent)
        self.setupUi(self)
    # END DO NOT MODIFY

        # ADD SLOTS HERE, indented to this level (ie. inside def __init__)
        self.pushButtonDisplay.clicked.connect(self.DisplayButton_Clicked)
        self.radioBlue.clicked.connect(self.BlueButton_Clicked)
        self.radioGreen.clicked.connect(self.GreenButton_Clicked)
        self.radioRed.clicked.connect(self.RedButton_Clicked)


    # ADD SLOT FUNCTIONS HERE
    # These are the functions your slots will point to
    # Indent to this level (ie. inside the class, at same level as def __init__)
    def DisplayButton_Clicked(self):
        self.ChangeTheText()

    def BlueButton_Clicked(self):
        self.ChangeBGColor("blue")

    def GreenButton_Clicked(self):
        self.ChangeBGColor("green")

    def RedButton_Clicked(self):
        self.ChangeBGColor("red")

    
#Example Slot Function
#   def SaveButton_Clicked(self):
#       Make a call to the Save() helper function here

    #ADD HELPER FUNCTIONS HERE
    # These are the functions the slot functions will call, to 
    # contain the custom code that you'll write to make your progam work.
    # Indent to this level (ie. inside the class, at same level as def __init__)

    def ChangeTheText(self):
        self.labelDisplayMessage.setText("Taehong")

    def ChangeBGColor(self, color):
        self.groupBoxColors.setStyleSheet("background-color: {0}".format(color))


#Example Helper Function
#    def Save(self):
#       Implement the save functionality here

# DO NOT MODIFY THIS CODE
if __name__ == "__main__":
    app = QApplication(sys.argv)
    the_form = MyForm()
    the_form.show()
    sys.exit(app.exec_())
# END DO NOT MODIFY