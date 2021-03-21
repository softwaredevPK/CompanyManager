from PySide2 import QtWidgets
from typing import Tuple


class SingleInstanceClass:
    """https://python-3-patterns-idioms-test.readthedocs.io/en/latest/Singleton.html"""
    __instance = None

    def __new__(cls):
        if SingleInstanceClass.__instance is None:
            SingleInstanceClass.__instance = object.__new__(cls)
        return SingleInstanceClass.__instance


def show_msg_box(text: Tuple[str, Exception]):
    """Function used to show msg_box"""
    text = str(text)
    msg = QtWidgets.QMessageBox()
    msg.setText(text)
    msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
    msg.exec_()


class MessageError(Exception):
    """Error with message to show in Msgbox"""




