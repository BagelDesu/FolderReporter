import os
import sys

from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *

class Reporter:

    def __init__(self, window):
        self.window = window
        self.window.setWindowTitle("Reporter")
        self.window.setGeometry(100,100,750,250)
        fbox = QFormLayout()

        repl = QLabel(" Runs through the given directory and prints out a csv report of the items found. \n Exclusions, excludes the given file extensions, Multiple extensions can be added using comma seperation. \n Check Recusively, when checked will force the tool to look through all folders within the directory given.")
        repl.setAlignment(Qt.AlignmentFlag.AlignCenter)
        repl.setIndent(True)
        repl.setWordWrap(True)

        dirl = QLabel("Directory: ")
        self.dirEntry = QLineEdit("D:\\")

        dumpdirl = QLabel("Dump Directory: ")
        self.dirDumpEntry = QLineEdit("D:\\dump")
        
        excl = QLabel("Exclusions: ")
        self.excEntry = QLineEdit()

        recl = QLabel("Check Recursively :") 
        self.recButton = QCheckBox()
        self.recButton.setChecked(False)

        runButton = QPushButton(window)         #Add Button
        runButton.setText("Run")                #Button Name
        runButton.clicked.connect(self.run)     #Register Listener

        statl1 = QLabel("<h2>Status: </h2>")
        statl1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.statl2 = QLabel("<h2>Idle</h2>")
        self.statl2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        fbox.addRow(repl)
        fbox.addRow(dirl, self.dirEntry)
        fbox.addRow(dumpdirl, self.dirDumpEntry)
        fbox.addRow(excl, self.excEntry)
        fbox.addRow(recl, self.recButton)
        fbox.addRow(runButton)
        fbox.addRow(statl1, self.statl2)
        
        self.window.setLayout(fbox)
        self.window.show()
        return

    def run(self):
        self.statl2.setText("<h2> Running <\h>")


        #Entry Point over here.
        files = getAllFilesFromDir(self.dirEntry.text(), self.excEntry.text(), self.recButton.isChecked())
        
        #reportExitCode = printReport(self.dirDumpEntry.text(), files)

        #if reportExitCode == 0:
        #    self.statl2.setText("<h2> Done <\h>")
        #else:
        #    self.statl2.setText("<h2> Error Running Report. </h2>")

        self.statl2.setText("<h2> Finished, Check Dump Directory for report <\h>")

        return

    def getAllFilesFromDir(self, dir, exclusions, recursive):

        report = [{
            "fileName":"",
            "filePath":"",
            "fileSize":0,
            "lastModify":''
        }]

        with os.scandir(dir) as directory:
            for file in directory:
                if file.is_file():
                    # file is NOT directory and can be used as is
                else if not file.is_file() and recursive:
                    # file is a directory
                    getAllFilesFromDir(file.path, exclusions, recursive)
        
        return
    
    def printReport(self, dumpDir, report):
        return
    


app = QApplication([])
window = QWidget()
reporter = Reporter(window)
sys.exit(app.exec())