"""
File: designer_plugin.py
      Example of how designer.py can be used to easily generate Qt4 Designer
      plugins.
Copyright: 2011-2012 Feth Arezki <feth dot arezki at majerti dot fr>
           2011-2012 Julien Miotte <mike dot perdide at gmail dot com>
License: This file is released under the GPLv3
         http://www.gnu.org/licenses/gpl-3.0.txt
"""
from PyQt4 import QtDesigner

LOGFILE = "/tmp/generic_qt4_plugins.log"

# For debugging purposes, we're wrapping all of this file inside a try: except:
import traceback
try:
    # Importing the plugin wrapper
    from designer import plugin

    # Below, list all the widget classes imports
    from analogclock import PyAnalogClock

    # The _include part must be thought carefully, since it will be used in the
    # generated (from the .ui) python file. It depends on where you'll keep the
    # .ui of the widget that will include the plugin.
    _INCLUDE = 'widgets.analogclock'
    ANALOG_CLOCK = plugin(PyAnalogClock, "analogClock", _INCLUD)

except Exception, e:
    with open(LOGFILE, "a") as handle:
        traceback.print_exc(file=handle)
