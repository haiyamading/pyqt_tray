import sys
from PyQt4 import QtGui
from PyQt4 import QtCore
from yapsy.PluginManager import PluginManager

class SystemTrayIcon(QtGui.QSystemTrayIcon):

    def __init__(self, icon, parent=None):
        QtGui.QSystemTrayIcon.__init__(self, icon, parent)
        self.createContext(parent)

    def createContext(self,parent):
        self.plugins = []
        menu = QtGui.QMenu(parent)

        # Load the plugins from the plugin directory.
        manager = PluginManager()
        manager.setPluginPlaces(["plugins"])
        manager.collectPlugins()

        # Loop round the plugins and print their names.
        self.plugins = manager.getAllPlugins()
        for plugin in self.plugins:
            print 'Loading plugin ', plugin.plugin_object.name()
            plugin.plugin_object.addAction( menu )

        # Exit
        menu.addSeparator()
        exitAction = menu.addAction("Exit")
        exitAction.triggered.connect( QtGui.qApp.quit )
        self.setContextMenu(menu)

def main():
    app = QtGui.QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(False)

    w = QtGui.QWidget()
    trayIcon = SystemTrayIcon(QtGui.QIcon("Buddha-Statue.ico"), w)

    trayIcon.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
 