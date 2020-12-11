import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.QtGui import QPixmap
import csv

#ADD IMPORT STATEMENT FOR YOUR GENERATED UI.PY FILE HERE
import Ui_FinalProject
#      ^^^^^^^^^^^ Change this!

#CHANGE THE SECOND PARAMETER (Ui_ChangeMe) TO MATCH YOUR GENERATED UI.PY FILE
class MyForm(QMainWindow, Ui_FinalProject.Ui_MainWindow):
#                         ^^^^^^^^^^   Change this!
    countries = []
    listPopulation = []

    # DO NOT MODIFY THIS CODE
    def __init__(self, parent=None):
        super(MyForm, self).__init__(parent)
        self.setupUi(self)
    # END DO NOT MODIFY
        self.actionSave_To_File.setEnabled(False)
        self.labelPopulation.setVisible(False)
        self.labelTotalAreaIn.setVisible(False)
        self.comboBoxMilesOrKilometers.setVisible(False)
        self.groupBoxPopulationDensity.setVisible(False)
        self.labelPercentageText.setVisible(False)
        self.pushButtonUpdatePopulation.setVisible(False)
        self.lineEditInputUserUpdate.setVisible(False)
        
        # ADD SLOTS HERE, indented to this level (ie. inside def __init__)
        self.actionLoad_Countries.triggered.connect(self.LoadCountriesFromFile)
        self.listCountries.currentRowChanged.connect(self.DisplayCountryData)
        
    # ADD SLOT FUNCTIONS HERE
    # These are the functions your slots will point to
    # Indent to this level (ie. inside the class, at same level as def __init__)
    def LoadCountriesFromFile(self):
        self.actionLoad_Countries.setEnabled(False)
        self.loadCountries()

    def DisplayCountryData(self, selectedCountryIndex):
        self.labelPopulation.setVisible(True)
        self.labelTotalAreaIn.setVisible(True)
        self.comboBoxMilesOrKilometers.setVisible(True)
        self.groupBoxPopulationDensity.setVisible(True)
        self.labelPercentageText.setVisible(True)
        self.pushButtonUpdatePopulation.setVisible(True)
        self.lineEditInputUserUpdate.setVisible(True)
        self.Display_theData(selectedCountryIndex)
        

    
#Example Slot Function
#   def SaveButton_Clicked(self):
#       Make a call to the Save() helper function here

    #ADD HELPER FUNCTIONS HERE
    # These are the functions the slot functions will call, to 
    # contain the custom code that you'll write to make your progam work.
    # Indent to this level (ie. inside the class, at same level as def __init__)
    def loadCountries(self):
        with open("Files/countries.txt", "r") as myFile:
            fileData = csv.reader(myFile)

            for line in fileData:
                self.countries.append(line)

            for country in self.countries:
                self.listCountries.addItem(country[0])

            for row in range(len(self.countries)):
                self.listPopulation.append(int(self.countries[row][1]))
        
    def Display_theData(self, selectedCountryIndex):
        countryName = self.countries[selectedCountryIndex][0]
        population = self.countries[selectedCountryIndex][1]
        totalArea = self.countries[selectedCountryIndex][2]
        density = float(population) / float(totalArea)
        imageName = countryName.replace(" ", "_")
        image = QPixmap("Files/Flags/" + imageName +  ".png")
        sumOfPopulation = sum(self.listPopulation)


        self.labelCountryName.setText(countryName)
        self.lineEditInputUserUpdate.setText(population)
        self.labelAreaNumber.setText("{0:.1f}".format(float(totalArea)))
        self.labelPopulationDensity.setText("{0:.2f}".format(density))
        self.labelPicture.setPixmap(image)
        self.labelPercentageNumber.setText("{0:.4f}%".format(float(population) / sumOfPopulation * 100))

  
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