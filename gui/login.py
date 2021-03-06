from PyQt5.QtGui import QMouseEvent
from PyQt5.uic.properties import QtGui

from gui import images_rc #don't remove - this is needed for image rendering

from PyQt5 import uic, QtCore
from PyQt5.QtCore import QObject
from PyQt5.QtWidgets import QPushButton, QLabel, QLineEdit

from gui.common import Common
from gui.register import Register
from service.database_service import authenticate
from service.utils import get_formatted_msg, maskUnmask


class Login(QObject):

    def __init__(self, parent=None):
        super(Login, self).__init__(parent)

        self.window = uic.loadUi("gui/ui_files/login.ui")

        register_button = self.window.findChild(QPushButton, 'register_button')
        register_button.clicked.connect(self.open_register)

        register_button = self.window.findChild(QPushButton, 'login_button')
        register_button.clicked.connect(self.attempt_login)

        self.username_input = self.window.findChild(QLineEdit, 'username_input')
        self.password_input = self.window.findChild(QLineEdit, 'password_input')
        self.password_input.installEventFilter(self)

        self.otp_input = self.window.findChild(QLineEdit, 'otp_input')

        self.register = Register(parent=self)

    def eventFilter(self, source, event):
        maskUnmask(self, source, event)
        return super(Login, self).eventFilter(source, event)

    def open_register(self):
        self.register.window.show()
        self.window.hide()

    def attempt_login(self):
        username, password, otp_value = self.get_entered_credentials()

        if authenticate(username, password, otp_value):
            Common(username, password, parent=self).show()

            self.window.hide()
        else:
            self.show("Authentication Unsuccessful", "red")

    def show(self, msg=None, color="green"):
        if msg is not None:
            self.window.findChild(QLabel, 'result_msg').setText(get_formatted_msg(msg, color))
        self.window.show()

    def get_entered_credentials(self):
        return self.username_input.text(), self.password_input.text(), self.otp_input.text()