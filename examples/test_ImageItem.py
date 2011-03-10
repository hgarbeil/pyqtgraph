# -*- coding: utf-8 -*-
## Add path to library (just for examples; you do not need this)
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))

from pyqtgraph.GraphicsView import *
from pyqtgraph.graphicsItems import *
from numpy import random
from PyQt4 import QtCore, QtGui
from scipy.ndimage import *

app = QtGui.QApplication([])

## Create window with GraphicsView widget
win = QtGui.QMainWindow()
view = GraphicsView()
#view.useOpenGL(True)
win.setCentralWidget(view)
win.show()

## Allow mouse scale/pan
view.enableMouse()

## ..But lock the aspect ratio
view.setAspectLocked(True)

## Create image item
img = ImageItem()
view.scene().addItem(img)

## Set initial view bounds
view.setRange(QtCore.QRectF(0, 0, 200, 200))

## Create random image
## this is a large image--use view.scaleToImage(img) to improve video framerate
data = random.random((5, 1000, 1000))
i = 0

def updateData():
    global img, data, i

    ## Display the data
    img.updateImage(data[i])
    i = (i+1) % data.shape[0]
    

# update image data every 20ms (or so)
t = QtCore.QTimer()
QtCore.QObject.connect(t, QtCore.SIGNAL('timeout()'), updateData)
t.start(20)



#app.exec_()
