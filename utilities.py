from PySide2 import QtWidgets

class SingleInstanceClass:
    """https://python-3-patterns-idioms-test.readthedocs.io/en/latest/Singleton.html"""
    __instance = None

    def __new__(cls):
        if SingleInstanceClass.__instance is None:
            SingleInstanceClass.__instance = object.__new__(cls)
        return SingleInstanceClass.__instance


def show_msg_box(text):
    """Message box with information of need to create company acc"""
    msg = QtWidgets.QMessageBox()
    msg.setText(text)
    msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
    msg.exec_()






