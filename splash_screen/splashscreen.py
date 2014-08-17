#!/usr/bin/env python
from PyQt4.QtCore import *
from PyQt4.QtGui import *


class MySplashScreen(QSplashScreen):
    def __init__(self, animation, flags):
        # run event dispatching in another thread
        QSplashScreen.__init__(self, QPixmap(), flags)
        self.movie = QMovie(animation)
        self.connect(self.movie, SIGNAL('frameChanged(int)'),
             SLOT('onNextFrame()'))
        self.movie.start()

    @pyqtSlot()
    def onNextFrame(self):
        pixmap = self.movie.currentPixmap()
        self.setPixmap(pixmap)
        self.setMask(pixmap.mask())


