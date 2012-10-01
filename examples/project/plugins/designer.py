"""
File: designer.py
      Generic tools to generate designer plugins.
Copyright: 2011-2012 Feth Arezki <feth dot arezki at majerti dot fr>
           2011-2012 Julien Miotte <mike dot perdide at gmail dot com>
License: This file is released under the GPLv3
         http://www.gnu.org/licenses/gpl-3.0.txt
"""
import PyQt4


if hasattr(PyQt4, 'QtDesigner'):
    #that class is only available when loaded from designer
    plugin_class = PyQt4.QtDesigner.QPyDesignerCustomWidgetPlugin
else:
    #it is of no use, but avoid runtime errors.
    plugin_class = object

from os.path import basename
import logging
logging.basicConfig(filename='/tmp/pcoords.log', level=logging.DEBUG)
logger = logging.getLogger(__name__)


logger.debug("========== inside " + basename(__file__) + " ===========")

debug = logger.debug


class SimpleLauncherPlugin(plugin_class):
    """
    derived classes implement
    -createWidget
    -name
    -domXml

    -includeFile if file is not in ui_simple_widgets
    """
    ATTR_NAME = ""
    INCLUDEFILE="dummy_import"
    IS_CONTAINER = False
    WIDGET_CLASS = None
    WIDGET_NAME = "Dummy, don't use"
    def __init__(self, parent=None):
        debug("__init__")
        super(SimpleLauncherPlugin, self).__init__(parent)

        self._initialized = False

    def initialize(self, formEditor):
        if self._initialized:
            return

        self._initialized = True

    def isInitialized(self):
        return self._initialized

    def createWidget(self, parent):
        return self.WIDGET_CLASS(parent)

    def name(self):
        return self.WIDGET_NAME

    def isContainer(self):
        return self.IS_CONTAINER

    def group(self):
        return "Example plugins"

    def includeFile(self):
        return self.INCLUDEFILE

    def icon(self):
        return self._icon

    def toolTip(self):
        return self._toolTip

    def whatsThis(self):
        return self._whatsThis

    def domXml(self):
        domXml ='<widget class="%s" name="%s">\n' % (self.WIDGET_NAME,
                                                     self.ATTR_NAME)

        if self._toolTip:
            domXml += '<property name="toolTip">\n' \
                      '  <string>%s</string>\n' \
                      '</property>\n' % self._toolTip

        if self._whatsThis:
            domXml += '<property name="whatsThis">\n' \
                      '  <string>%s</string>\n' \
                      '</property>\n' % self._whatsThis

        domXml += '</widget>\n'
        debug(domXml)
        return domXml


def plugin(widget_class, attr_name, include, icon="", toolTip="",
           whatsThis="", bases=(SimpleLauncherPlugin,), container=False):
    widget_name = widget_class.__name__
    class_dict = {
        "ATTR_NAME": attr_name,
        "INCLUDEFILE": include,
        "IS_CONTAINER": container,
        "WIDGET_CLASS": widget_class,
        "WIDGET_NAME": widget_name,
        "_icon": icon,
        "_toolTip": toolTip,
        "_whatsThis": whatsThis
        }
    return type('%sPlugin' % widget_name, bases, class_dict)
