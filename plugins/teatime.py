import sys
from PyQt4 import QtGui
from PyQt4 import QtCore

from yapsy.IPlugin import IPlugin

class TeaTime(IPlugin):
    def __init__(self):
        self.timer = QtTeaTime(None)
    def name(self):
        return "Tea Time"
    def addAction(self,menu):
        self.timer.setParent(menu)
        self.timer.addAction(menu,self.name())
     

class QtTeaTime(QtCore.QObject):
    def __init__(self, parent=None):
        QtCore.QObject.__init__(self, parent)
        
    def addAction(self,menu,name):
        self.action = menu.addAction( name )
        self.action.triggered.connect( self.run )   

    def run(self):
        value, ret = QtGui.QInputDialog.getInt( None, "Tea Time", "Time (min):", 4, 0, 60, 1 )
        
        if ret :
            self.action.setText( "Brewing Tea ..." )
            self.action.setEnabled(False)
            print("Plugin TeaTimer: waiting for ", value * 60 * 1000 )
            QtCore.QTimer.singleShot( value * 60 * 1000, self.done )
            
    def done(self):
        self.action.setText( "Tea Time" )
        self.action.setEnabled(True)
        QtGui.QMessageBox.information( None, 'Tea Time', 'mmmmmmmhh', QtGui.QMessageBox.Ok )
