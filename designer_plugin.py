"""
File: designer_plugin.py
      Example of how designer.py can be used to easily generate Qt4 Designer
      plugins.
Copyright: 2011-2012 Feth Arezki <feth dot arezki at majerti dot fr>
           2011-2012 Julien Miotte <mike dot perdide at gmail dot com>
License: This file is released under the GPLv3
         http://www.gnu.org/licenses/gpl-3.0.txt
"""
from .ui_atomic import PyTinyHeader

from .designer import plugin

_ATOMIC_INCLUDE = '.ui_atomic'

HEADER_TINY = plugin(PyTinyHeader, "tiny_header", _ATOMIC_INCLUDE)
