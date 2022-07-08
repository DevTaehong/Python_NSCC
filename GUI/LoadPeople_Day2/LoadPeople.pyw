import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.QtGui import QPixmap

#ADD IMPORT STATEMENT FOR YOUR GENERATED UI.PY FILE HERE
import Ui_LoadPeople
#      ^^^^^^^^^^^ Change this!

#CHANGE THE SECOND PARAMETER (Ui_ChangeMe) TO MATCH YOUR GENERATED UI.PY FILE
class MyForm(QMainWindow, Ui_LoadPeople.Ui_MainWindow):
#                         ^^^^^^^^^^^   Change this!
    my2dList = []   #Declaring a GLOBALLY scoped 2d list variable


    # DO NOT MODIFY THIS CODE
    def __init__(self, parent=None):    #EVERYTHING IN THIS FUNCTION OCCURS BEFORE THE FORM IS SEEN ON SCREEN
        super(MyForm, self).__init__(parent)
        self.setupUi(self)
    # END DO NOT MODIFY

        # self.actionSave.setEnabled(False)

        # ADD SLOTS HERE, indented to this level (ie. inside def __init__)
        self.pushButtonLoadPeople.clicked.connect(self.LoadButton_Clicked)
        self.listWidgetNames.currentRowChanged.connect(self.ListRow_Changed)
        self.actionSave.triggered.connect(self.SaveMenu_Triggered)

    # ADD SLOT FUNCTIONS HERE
    # These are the functions your slots will point to
    # Indent to this level (ie. inside the class, at same level as def __init__)
    def LoadButton_Clicked(self):
        # print("Yup")      #This was a functionality test!
        #1. Read a file & Store the file in memory
        if len(self.my2dList) == 0:     #Use logic to check WHETHER to reload from file (ie. don't do it if the list is already filled)
            self.ReadFromFileIntoMemory()

        # print(self.my2dList) #  Testing purposes only
        
        #2. Retrieve file contents from memory and load into the listWidget
        self.LoadFromMemoryIntoListWidget()

        #Example of hiding something using code (Names label)
        self.labelNamesList.setVisible(False)
        self.frameDisplayArea.setEnabled(False)

        image = QPixmap("UISamples\DisplayImage\images\smiley.png")
        #set the label with the selected pixmap
        self.labelPicture.setPixmap(image)


    def ListRow_Changed(self, newRowIndex): #newRowIndex is a parameter we set up, value is received from the currentRowChanged signal
        # Need to get the SELECTED row's name and age
        # From where? Memory
        # print(self.my2dList[newRowIndex][1])
        self.lineEditFirstName.setText(self.my2dList[newRowIndex][0])
        self.lineEditAge.setText(self.my2dList[newRowIndex][1])

        # print(self.listWidgetNames.currentRow())    #Alternative method of finding index of which row was selected

        self.labelNamesList.setVisible(True)

        #Example of setting text of a label to the result of a calculating function
        self.labelAnswer.setText(str(self.CalcSomeValue(7, 12)))

    def SaveMenu_Triggered(self):
        print("Save was clicked.")
        self.actionSave.setEnabled(False)

    #ADD HELPER FUNCTIONS HERE
    # These are the functions the slot functions will call, to 
    # contain the custom code that you'll write to make your progam work.
    # Indent to this level (ie. inside the class, at same level as def __init__)

    def LoadFromMemoryIntoListWidget(self):
        #Take whatever is in memory (in 2dlist) and load it into the onscreen list widget
        self.listWidgetNames.clear()
        for row in self.my2dList:
            self.listWidgetNames.addItem(row[0])


    def ReadFromFileIntoMemory(self):
        #Open the people file and read it's contents into memory
        #Use csv.reader to get the data
        import csv
        
        fileName = "Files/people.csv"
        accessMode = "r"        #Read mode

        with open(fileName, accessMode) as myFile:
            fileContents = csv.reader(myFile)   #Gives me something LIKE a 2d list containing the data in the file

            self.my2dList = []
            for row in fileContents:    #Loop through the fileContents NOT-QUITE-LIST
                self.my2dList.append(row)    #Create my own 2d list out of the csv reader object

    def CalcSomeValue(self, num1, num2):
        #Silly calculation function, takes two numbers, does some math, returns answer
        return num1 * num2 + 43

# DO NOT MODIFY THIS CODE
if __name__ == "__main__":
    app = QApplication(sys.argv)
    the_form = MyForm()
    the_form.show()
    sys.exit(app.exec_())
# END DO NOT MODIFY