import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox

#ADD IMPORT STATEMENT FOR YOUR GENERATED UI.PY FILE HERE
import Ui_TaxCalculator
#      ^^^^^^^^^^^ Change this!

#CHANGE THE SECOND PARAMETER (Ui_ChangeMe) TO MATCH YOUR GENERATED UI.PY FILE
class MyForm(QMainWindow, Ui_TaxCalculator.Ui_MainWindow):
#                         ^^^^^^^^^^^   Change this!

    # DO NOT MODIFY THIS CODE
    def __init__(self, parent=None):
        super(MyForm, self).__init__(parent)
        self.setupUi(self)
    # END DO NOT MODIFY

        # ADD SLOTS HERE, indented to this level (ie. inside def __init__)
        self.pushButtonCalculateTax.clicked.connect(self.clicked_CalculateTax)


    # ADD SLOT FUNCTIONS HERE
    # These are the functions your slots will point to
    # Indent to this level (ie. inside the class, at same level as def __init__)
    def clicked_CalculateTax(self):
        self.calculateTax()
#Example Slot Function
#   def SaveButton_Clicked(self):
#       Make a call to the Save() helper function here

    #ADD HELPER FUNCTIONS HERE
    # These are the functions the slot functions will call, to 
    # contain the custom code that you'll write to make your progam work.
    # Indent to this level (ie. inside the class, at same level as def __init__)
    def calculateTax(self):
        provinHoldingTax = 0.06
        federalHoldingTax = 0.25
        deduction = 0.02
        weeklySalary = self.lineEditInputSalary.text()
        dependents = self.lineEditInputdependents.text()
        try:
            provinWhithheld = provinHoldingTax * float(weeklySalary)
            federalWhithheld = federalHoldingTax * float(weeklySalary)
            dependentDeduction = deduction * float(dependents) * float(weeklySalary)
            totalWithheld = provinWhithheld + federalWhithheld - dependentDeduction
            totalTakehomepay = float(weeklySalary) - totalWithheld
            self.labelDependentsDisplay.setText(dependents)
        except:
            pass
        
        try:
            self.labelProvincialTaxDisplay.setText("${0:.2f}".format(provinWhithheld))
            self.labelFederalTaxDisplay.setText("${0:.2f}".format(federalWhithheld))
            self.labelDeductionDisplay.setText("${0:.2f}".format(dependentDeduction))
            self.labelTotalWithheldDisplay.setText("${0:.2f}".format(totalWithheld))
            self.labelTakeHomePayDisplay.setText("${0:.2f}".format(totalTakehomepay))
        except:
            print("Enter valid values")
    
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