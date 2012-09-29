"""
File: designer.py
      Generic tools to wrap a generated Qt ui into a QWidget, QFrame or other.
Copyright: 2011-2012 Feth Arezki <feth dot arezki at majerti dot fr>
           2011-2012 Julien Miotte <mike dot perdide at gmail dot com>
License: This file is released under the GPLv3
         http://www.gnu.org/licenses/gpl-3.0.txt
"""

from PyQt4.QtGui import QWidget, QFrame

def _init(self, parent=None):
    self.BASE_WIDGET.__init__(self, parent)

    self.setupUi(self)


_init.__name__ == '__init__'

def _ui(self):
    return self._ui

_ui.__name__ = 'ui'

def wrapper_attrs(ui_class, base_widget):
    return {'ui': _ui,
        '__init__': _init,
        'UI_CLASS': ui_class,
        'BASE_WIDGET': base_widget,
        }

def ui_wrapper(name, ui_class, base_widget, slots=(), signals=None):
    """
    slots: tuple of Slots
    """
    if signals is None:
        signals = {}
    class_dict = wrapper_attrs(ui_class, base_widget)

    for slot in slots:
        class_dict[slot.__name__] = slot

    return type(name, (base_widget, ui_class), class_dict)
