import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox

import Ui_ColorDemo

class MyForm(QMainWindow, Ui_ColorDemo.Ui_MainWindow):

    # DO NOT MODIFY THIS CODE
    def __init__(self, parent=None):
        super(MyForm, self).__init__(parent)
        self.setupUi(self)
    # END DO NOT MODIFY

        # ADD SLOTS HERE, indented to this level (ie. inside def __init__)
        #One slot each for, red, blue, green radios clicked, one for display button clicked
        self.radioRed.clicked.connect(self.RadioRed_Clicked)
        self.radioBlue.clicked.connect(self.RadioBlue_Clicked)
        self.radioGreen.clicked.connect(self.RadioGreen_Clicked)

        self.pushButtonDisplay.clicked.connect(self.DisplayButton_Clicked)

    # ADD SLOT FUNCTIONS HERE
    # These are the functions your slots will point to
    # Indent to this level (ie. inside the class, at same level as def __init__)
    
	#Slot function that runs when radio red is clicked
    def RadioRed_Clicked(self):
		#Call the function that sets the BG color, passing "red" as the parameter
        self.SetBackGroundColor("red")

	#Slot function that runs when radio blue is clicked
    def RadioBlue_Clicked(self):
		#Call the function that sets the BG color, passing "blue" as the parameter
        self.SetBackGroundColor("blue")

	#Slot function that runs when radio green is clicked
    def RadioGreen_Clicked(self):
		#Call the function that sets the BG color, passing "green" as the parameter
        self.SetBackGroundColor("green")

	#Slot function that runs when display button is clicked
    def DisplayButton_Clicked(self):
		#Ask the lineEdit control what value is in its text property (ie. user-entered value)
        message = self.lineEditMessage.text()
		
		#Silly demonstration of using IFs and lists to control which values the program won't accept
        if message.upper() not in ["BOOYA", "YIKES", "TICKLES"]:
            #Call the helper function to set the label's text, passing the value as a parm.
            self.SetMessageText(message)
        else:
            self.SetMessageText("Nope!")
       
    #ADD HELPER FUNCTIONS HERE
    # These are the functions the slot functions will call, to 
    # contain the custom code that you'll write to make your progam work.
    # Indent to this level (ie. inside the class, at same level as def __init__)

	#Helper function used to set the bg color of the groupbox, based on the color it gets passed.
    def SetBackGroundColor(self, color):
        self.groupBoxColors.setStyleSheet("background-color: {0}".format(color))

	#Helper function used to set text of the label to whatever string it gets passed.
    def SetMessageText(self, msg):
        self.labelMessage.setText(msg)

# DO NOT MODIFY THIS CODE
if __name__ == "__main__":
    app = QApplication(sys.argv)
    the_form = MyForm()
    the_form.show()
    sys.exit(app.exec_())
# END DO NOT MODIFY