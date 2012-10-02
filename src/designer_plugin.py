"""
File: designer_plugin.py
      Example of how designer.py can be used to easily generate Qt4 Designer
      plugins.
Copyright: 2011-2012 Feth Arezki <feth dot arezki at majerti dot fr>
           2011-2012 Julien Miotte <mike dot perdide at gmail dot com>
License: This file is released under the GPLv3
         http://www.gnu.org/licenses/gpl-3.0.txt
"""
# Althought the following import isn't use here, if it's missing Qt4 Designer
# won't aknowledge this as a plugin
from PyQt4 import QtDesigner

# Importing the plugin wrapper
from designer import plugin

# Below, list all the widget classes imports.
# If in launcher_designer.py the PYTHONPATH is set to the directory containing
# the widget classes, the import can be done like:
from widget_class import PyWidgetClass

# It can also be done like the following (for instance if module is installed):
#from module.widgets.widget_class import PyWidgetClass

# The _include part must be thought through carefully, since it will be used in
# the generated (from the .ui) python file. It depends on where you'll keep the
# .ui of the widget that will include the plugin.
_INCLUDE = 'module.widgets.base_class'
ANALOG_CLOCK = plugin(PyWidgetClass, "widgetClass", _INCLUDE)
