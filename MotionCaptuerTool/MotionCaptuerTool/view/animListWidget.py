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
    
import animButton
reload(animButton)
from animButton import AnimButton

class AnimListWidget(QListWidget):
    
    def __init__(self, parent = None):
        super(AnimListWidget, self).__init__(parent)
        
        self.setDefault()
        self.childrenWidget = None
    
    def setDefault(self):
        self.setSelectionRectVisible(True)
        policy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        self.setSizePolicy(policy)
        self.itemSize = QSize(128,128)
        self.setGridSize(self.itemSize)

        self.setLayoutMode(self.Batched)
        self.setBatchSize(300)
        self.setResizeMode(self.Adjust)
        self.setViewMode(self.IconMode)
        
        self.setMinimumWidth(5)
        self.setMouseTracking(True)
        
        self.setSpacing(300)
    
    def setOption(self, fileType, operation):
        if self.childrenWidget:
            for item in self.childrenWidget:
                item.setOption(fileType, operation)
                
    def setSpeed(self, speed):
        if self.childrenWidget:
            for item in self.childrenWidget:
                item.setSpeed(speed)
        
    def setItems(self, widgets):
        if not widgets:
            print "Input items is None!!!"
            return
        self.clear()
        for widget in widgets:
            item = QListWidgetItem()
            item.setSizeHint(widget.sizeHint())
            self.addItem(item)
            self.setItemWidget(item, widget)
        
        self.childrenWidget = widgets
        
        
    def wheelEvent(self, event):
        stepSize = QSize(10,10)
        if self.childrenWidget == None:
            return
        
        if event.delta() > 0:
            if self.itemSize.width() > 128:
                return
            self.itemSize += stepSize
        else:
            if self.itemSize.width() < 64:
                return
            self.itemSize -= stepSize
            
        self.setGridSize(self.itemSize)
        for widget in self.childrenWidget:
            widget.setSize(self.itemSize)
        
def main():
    app = QApplication([])
    listWidget = AnimListWidget()
    
    buttons = []
    for i in range(10):
        animButton = AnimButton()
        basePath = "../reference/images"
        frames = os.listdir(basePath)
        animButton.setFrames(basePath, frames)
        animButton.setSize(QSize(128, 128))
        buttons.append(animButton)

        print i

    listWidget.setItems(buttons)
    listWidget.show()
    listWidget.setGeometry(100, 100, 800,300)
    app.exec_()
    
if __name__ == "__main__":
    main()
    