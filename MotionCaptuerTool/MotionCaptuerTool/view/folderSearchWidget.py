# coding:utf-8

import os

try:
    from PySide.QtGui import *
    from PySide.QtCore import *
    from shiboken import wrapInstance
except:
    from PySide2.QtGui import *
    from PySide2.QtCore import *
    from PySide2.QtWidgets import *
    from shiboken2 import wrapInstance


class FolderSearchWidget(QWidget):
    
    def __init__(self, parent = None):
        super(FolderSearchWidget, self).__init__(parent)
        
        self.imagePath = FolderSearchWidget.getImagePath()
        
        layout = QHBoxLayout()
        self.setLayout(layout)
        
        self.pathLinedit = QLineEdit()
        self.searchButton = QPushButton()
        buttonImage = QPixmap(os.path.join(self.imagePath,'open.png'))
        buttonIcon  = QIcon(buttonImage)
        self.searchButton.setIcon(buttonIcon)
        
        layout.addWidget(self.pathLinedit)
        layout.addWidget(self.searchButton)
        layout.setContentsMargins(0,0,0,0)
        
        self.searchButton.clicked.connect(self.__openFolderDialog)
    
    def __openFolderDialog(self):
        oldDir = self.pathLinedit.text()
        selectedDir = QFileDialog.getExistingDirectory()
        if selectedDir:
            self.pathLinedit.setText(selectedDir)
        else:
            self.pathLinedit.setText(oldDir)
            
    def getDirectory(self):
        return self.pathLinedit.text()
        
    @classmethod
    def getRootPath(cls):
        path = os.path.dirname(__file__)
        return os.path.dirname(path)
    
    @classmethod
    def getImagePath(cls):
        return os.path.join(cls.getRootPath(),'view/images')

def main():
    app = QApplication([])
    widget = FolderSearchWidget()
    widget.show()
    app.exec_()
    
if __name__ == "__main__":
    main()
    
        
    
    
    
    