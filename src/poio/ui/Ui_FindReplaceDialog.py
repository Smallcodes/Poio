# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FindReplaceDialog.ui'
#
# Created: Mon Aug 13 10:57:11 2012
#      by: PyQt4 UI code generator 4.9.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_FindReplaceDialog(object):
    def setupUi(self, FindReplaceDialog):
        FindReplaceDialog.setObjectName(_fromUtf8("FindReplaceDialog"))
        FindReplaceDialog.resize(342, 140)
        self.gridLayout = QtGui.QGridLayout(FindReplaceDialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.findReplaceForm = FindReplaceForm(FindReplaceDialog)
        self.findReplaceForm.setObjectName(_fromUtf8("findReplaceForm"))
        self.gridLayout.addWidget(self.findReplaceForm, 0, 0, 1, 1)

        self.retranslateUi(FindReplaceDialog)
        QtCore.QMetaObject.connectSlotsByName(FindReplaceDialog)

    def retranslateUi(self, FindReplaceDialog):
        FindReplaceDialog.setWindowTitle(QtGui.QApplication.translate("FindReplaceDialog", "Find/Replace", None, QtGui.QApplication.UnicodeUTF8))

from FindReplaceForm import FindReplaceForm
