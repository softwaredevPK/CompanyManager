from app import WelcomeWindow
import sys
from PySide2 import QtCore, QtGui, QtWidgets

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    window = WelcomeWindow()
    window.show()

    sys.exit(app.exec_())

