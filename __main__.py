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

        dumpnamel = QLabel("Dump Name: ")
        self.dirDumpNameEntry = QLineEdit("dumpcsv")

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
        fbox.addRow(dumpnamel, self.dirDumpNameEntry)
        fbox.addRow(excl, self.excEntry)
        fbox.addRow(recl, self.recButton)
        fbox.addRow(runButton)
        fbox.addRow(statl1, self.statl2)
        
        self.window.setLayout(fbox)
        self.window.show()
        return

    def run(self):
        self.statl2.setText("<h2> Running <\h>")

        report = self.getAllFilesFromDir(self.dirEntry.text(), self.excEntry.text(), self.recButton.isChecked())
        self.printReport(self.dirDumpEntry.text(), self.dirDumpNameEntry.text(), report)

        self.statl2.setText("<h2> Finished, Check Dump Directory for report <\h>")

        return

    def getAllFilesFromDir(self, dir, exclusions, recursive):
        report = ""
        
        with os.scandir(dir) as directory:
            for file in directory:
                if file.is_file():
                    exclusionlist = exclusions.lower().split(',')
                    filetype = os.path.splitext(file.name)[1].lower()
                    if not filetype in exclusionlist:
                        #file is NOT a directory and can be used as is
                        report += file.name + "," + file.path + "," + filetype + "," + str(os.path.getsize(file.path) * 0.001) + "kb ," + str(os.path.getmtime(file.path)/86400) + "\n"
                elif not file.is_file() and recursive:
                    #file IS a directory, loop recursively.
                    #WARNING Could be expensive to do this as a recursion, might be best to find something else that accepts a "recurse flag" when looking through files.
                    report += self.getAllFilesFromDir(file.path, exclusions, recursive)

        return report


    def printReport(self, dumpDir, fileName, report):
        printable = "Name, Path, Extension, Size, Last Modified\n"
        printable += report

        f = open(os.path.join(dumpDir, fileName+".csv"), "w")
        f.write(printable)
        f.close()
        return
    


app = QApplication([])
window = QWidget()
reporter = Reporter(window)
sys.exit(app.exec())