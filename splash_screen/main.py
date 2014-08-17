#!/usr/bin/env python

from multiprocessing import Pool
from splashscreen import *


class Form(QDialog):

    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        self.browser = QTextBrowser()
        self.setWindowTitle('Just a dialog')

# Put your initialization code here


def longInitialization(arg):
    time.sleep(arg)
    return 0
if __name__ == "__main__":
    import sys
    import time

    app = QApplication(sys.argv)

    # Create and display the splash screen
    splash = MySplashScreen('splash.png', Qt.WindowStaysOnTopHint)
#   splash.setMask(splash_pix.mask())
    #splash.raise_()
    splash.show()
    app.processEvents()

    # this event loop is needed for dispatching of Qt events
    initLoop = QEventLoop()
    pool = Pool(processes=1)
    pool.apply_async(longInitialization, [2],
    callback=lambda exitCode: initLoop.exit(exitCode))
    initLoop.exec_()

    form = Form()
    form.show()
    splash.finish(form)
    app.exec_()
