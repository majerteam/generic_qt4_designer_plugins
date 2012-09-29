"""
File: ui_base.py
      Classes for our plugins.
Copyright: 2011-2012 Feth Arezki <feth dot arezki at majerti dot fr>
           2011-2012 Julien Miotte <mike dot perdide at gmail dot com>
License: This file is released under the GPLv3
         http://www.gnu.org/licenses/gpl-3.0.txt
"""
from PyQt4.QtGui import QWidget
from PyQt4.QtCore import pyqtProperty


class TinyHeader(QWidget):

    button_clicked = pyqtSignal(int, name='button_clicked')

    # Example of properties that can be set.
    @pyqtProperty(bool)
    def apparent(self):
        return self.isVisible()

    @apparent.setter
    def apparent(self, value):
        return self.setVisible(value)

    def setup_ui(self):
        # The following buttons are designed in the .ui file (using Qt4
        # Designer). The fact that they are reachable through self. and not
        # self._ui. or self.ui. is the work of ui_wrapper().
        self._buttons = (self.button_one,
                         self.button_two,
                         self.button_three)

        # Let's connect some signals
        for button in self._buttons:
            button.clicked.connect(self.button_clicked)

    def button_clicked(self):
        button = self.sender()

        # This could be used by connecting the TinyHeader widget on a slot of
        # the main window, with the signal "button_clicked(int)".
        self.button_clicked.emit(self._buttons.index(button))
