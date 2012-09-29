"""
File: ui_atomic.py
      Associating QWidget, QFrames, ... to their interfaces (UIs).
Copyright: 2011-2012 Feth Arezki <feth dot arezki at majerti dot fr>
           2011-2012 Julien Miotte <mike dot perdide at gmail dot com>
License: This file is released under the GPLv3
         http://www.gnu.org/licenses/gpl-3.0.txt
"""
from .util.ui_wrapper import ui_wrapper

from .tiny_header_ui import Ui_tiny_header
from .ui_base import TinyHeader

PyTinyHeader = ui_wrapper('PyTinyHeader', Ui_tiny_header, TinyHeader)
