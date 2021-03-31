from PySide2 import QtWidgets
from typing import Tuple
import xlwings as xw


xw._xlwindows.N_COM_ATTEMPTS = 5  # no of attempts changed 5 to avoid infinite loops in case of error


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


class ExcelApplicationContextManager:

    def __init__(self, app=None, visible=False, kill_app=False, display_alerts=None, ask_to_update_links=None, enable_events=None, screen_updating=False):
        """
        Context Manager used to work with Excel by xlwings.

        :param app: None/Instance of xlwings App
        :param visible: True/False
        :param kill_app: True/False
        :param display_alerts: True/False/None - None means default setting
        :param ask_to_update_links:  True/False/None - None means default setting
        :param enable_events:  True/False/None - None means default setting
        :param screen_updating: True/False
        """
        self.app = app
        self.visible = visible
        if app is None:
            self.new_app = True
        else:
            self.new_app = False
        self.alerts = display_alerts
        self.links = ask_to_update_links
        self.screen = screen_updating
        self.events = enable_events
        self.kill_app = kill_app
        self.def_alerts = None
        self.def_links = None
        self.def_events = None

    def __enter__(self):
        # below property and its setter are used to create visible_ property on xlwings app
        @property
        def visible_(self):
            return self.visible

        @visible_.setter
        def visible_(self, value):
            self.visible = value
            self.api.ScreenUpdating = value

        if self.new_app:
            self.app = xw.App(visible=self.visible)
        else:
            self.app.visible = self.visible

        # get default(user) values
        self.def_links = self.app.api.AskToUpdateLinks
        self.def_alerts = self.app.api.DisplayAlerts
        self.def_events = self.app.api.EnableEvents
        self.def_screen = self.app.api.ScreenUpdating

        # set values
        if self.alerts is not None:
            self.app.api.DisplayAlerts = self.alerts
        if self.links is not None:
            self.app.api.AskToUpdateLinks = self.links
        if self.events is not None:
            self.app.api.EnableEvents = self.events
        self.app.api.ScreenUpdating = self.screen
        if self.visible:  # visible means that screenupdating must be True
            self.app.api.ScreenUpdating = True

        # adding property method to app class, thanks that there is no need to remember to chance screen updating with visible (they are conencted)
        xw.App.visible_ = visible_

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.app.api.ScreenUpdating = self.def_screen
        self.app.api.EnableEvents = self.events
        self.app.api.AskToUpdateLinks = self.links
        self.app.api.DisplayAlerts = self.alerts
        if exc_tb is not None and exc_val is not None and exc_type is not None:
            if self.kill_app:
                self.app.kill()
        else:  # error occurred, so we wanna kill app, otherwise user could have many instances of it
            self.app.kill()
