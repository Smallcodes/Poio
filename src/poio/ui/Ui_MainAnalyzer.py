# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainAnalyzer.ui'
#
# Created: Thu May 24 14:45:21 2012
#      by: PyQt4 UI code generator 4.8.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(957, 838)
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "PoioAnalyzer", None, QtGui.QApplication.UnicodeUTF8))
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.centralWidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_7 = QtGui.QLabel(self.centralWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setSizeIncrement(QtCore.QSize(1, 0))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setText(QtGui.QApplication.translate("MainWindow", "Files:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout.addWidget(self.label_7, 12, 1, 1, 2)
        self.line = QtGui.QFrame(self.centralWidget)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.gridLayout.addWidget(self.line, 11, 1, 1, 6)
        self.buttonAddFiles = QtGui.QPushButton(self.centralWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonAddFiles.sizePolicy().hasHeightForWidth())
        self.buttonAddFiles.setSizePolicy(sizePolicy)
        self.buttonAddFiles.setText(QtGui.QApplication.translate("MainWindow", "Add files...", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonAddFiles.setObjectName(_fromUtf8("buttonAddFiles"))
        self.gridLayout.addWidget(self.buttonAddFiles, 14, 1, 1, 1)
        self.buttonRemoveFiles = QtGui.QPushButton(self.centralWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonRemoveFiles.sizePolicy().hasHeightForWidth())
        self.buttonRemoveFiles.setSizePolicy(sizePolicy)
        self.buttonRemoveFiles.setText(QtGui.QApplication.translate("MainWindow", "Remove files", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonRemoveFiles.setObjectName(_fromUtf8("buttonRemoveFiles"))
        self.gridLayout.addWidget(self.buttonRemoveFiles, 14, 2, 1, 1)
        self.listFiles = QtGui.QListView(self.centralWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listFiles.sizePolicy().hasHeightForWidth())
        self.listFiles.setSizePolicy(sizePolicy)
        self.listFiles.setSizeIncrement(QtCore.QSize(1, 0))
        self.listFiles.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.listFiles.setObjectName(_fromUtf8("listFiles"))
        self.gridLayout.addWidget(self.listFiles, 13, 1, 1, 2)
        self.lineeditQuickSearch = QtGui.QLineEdit(self.centralWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(4)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineeditQuickSearch.sizePolicy().hasHeightForWidth())
        self.lineeditQuickSearch.setSizePolicy(sizePolicy)
        self.lineeditQuickSearch.setObjectName(_fromUtf8("lineeditQuickSearch"))
        self.gridLayout.addWidget(self.lineeditQuickSearch, 14, 4, 1, 3)
        self.buttonClearAllSearches = QtGui.QPushButton(self.centralWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonClearAllSearches.sizePolicy().hasHeightForWidth())
        self.buttonClearAllSearches.setSizePolicy(sizePolicy)
        self.buttonClearAllSearches.setText(QtGui.QApplication.translate("MainWindow", "Clear All Searches", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonClearAllSearches.setObjectName(_fromUtf8("buttonClearAllSearches"))
        self.gridLayout.addWidget(self.buttonClearAllSearches, 3, 2, 1, 1)
        self.buttonSearch = QtGui.QPushButton(self.centralWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(4)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonSearch.sizePolicy().hasHeightForWidth())
        self.buttonSearch.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.buttonSearch.setFont(font)
        self.buttonSearch.setText(QtGui.QApplication.translate("MainWindow", "Search", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonSearch.setObjectName(_fromUtf8("buttonSearch"))
        self.gridLayout.addWidget(self.buttonSearch, 3, 4, 1, 3)
        self.buttonSaveSearches = QtGui.QPushButton(self.centralWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonSaveSearches.sizePolicy().hasHeightForWidth())
        self.buttonSaveSearches.setSizePolicy(sizePolicy)
        self.buttonSaveSearches.setText(QtGui.QApplication.translate("MainWindow", "Save Searches...", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonSaveSearches.setObjectName(_fromUtf8("buttonSaveSearches"))
        self.gridLayout.addWidget(self.buttonSaveSearches, 3, 3, 1, 1)
        self.texteditInterlinear = PoioIlTextEdit(self.centralWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.texteditInterlinear.sizePolicy().hasHeightForWidth())
        self.texteditInterlinear.setSizePolicy(sizePolicy)
        self.texteditInterlinear.setSizeIncrement(QtCore.QSize(2, 0))
        self.texteditInterlinear.setFrameShadow(QtGui.QFrame.Sunken)
        self.texteditInterlinear.setObjectName(_fromUtf8("texteditInterlinear"))
        self.gridLayout.addWidget(self.texteditInterlinear, 13, 3, 1, 4)
        self.label_8 = QtGui.QLabel(self.centralWidget)
        self.label_8.setSizeIncrement(QtCore.QSize(2, 0))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setText(QtGui.QApplication.translate("MainWindow", "Result:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout.addWidget(self.label_8, 12, 3, 1, 1)
        self.label_9 = QtGui.QLabel(self.centralWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        self.label_9.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_9.setText(QtGui.QApplication.translate("MainWindow", "Quick Search:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.gridLayout.addWidget(self.label_9, 14, 3, 1, 1)
        self.tabWidget = QtGui.QTabWidget(self.centralWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.verticalLayout = QtGui.QVBoxLayout(self.tab)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label_2 = QtGui.QLabel(self.tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setSizeIncrement(QtCore.QSize(1, 0))
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Utterances:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)
        self.lineeditSearchUtterances = QtGui.QLineEdit(self.tab)
        self.lineeditSearchUtterances.setSizeIncrement(QtCore.QSize(2, 0))
        self.lineeditSearchUtterances.setObjectName(_fromUtf8("lineeditSearchUtterances"))
        self.gridLayout_2.addWidget(self.lineeditSearchUtterances, 0, 1, 1, 1)
        self.label_3 = QtGui.QLabel(self.tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setSizeIncrement(QtCore.QSize(1, 0))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "Words:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_2.addWidget(self.label_3, 1, 0, 1, 1)
        self.lineeditSearchWords = QtGui.QLineEdit(self.tab)
        self.lineeditSearchWords.setSizeIncrement(QtCore.QSize(2, 0))
        self.lineeditSearchWords.setObjectName(_fromUtf8("lineeditSearchWords"))
        self.gridLayout_2.addWidget(self.lineeditSearchWords, 1, 1, 1, 1)
        self.label_4 = QtGui.QLabel(self.tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setSizeIncrement(QtCore.QSize(1, 0))
        self.label_4.setText(QtGui.QApplication.translate("MainWindow", "Morphemes:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout_2.addWidget(self.label_4, 2, 0, 1, 1)
        self.lineeditSearchMorphemes = QtGui.QLineEdit(self.tab)
        self.lineeditSearchMorphemes.setSizeIncrement(QtCore.QSize(2, 0))
        self.lineeditSearchMorphemes.setObjectName(_fromUtf8("lineeditSearchMorphemes"))
        self.gridLayout_2.addWidget(self.lineeditSearchMorphemes, 2, 1, 1, 1)
        self.label_5 = QtGui.QLabel(self.tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setSizeIncrement(QtCore.QSize(1, 0))
        self.label_5.setText(QtGui.QApplication.translate("MainWindow", "Glosses:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout_2.addWidget(self.label_5, 3, 0, 1, 1)
        self.lineeditSearchGlosses = QtGui.QLineEdit(self.tab)
        self.lineeditSearchGlosses.setSizeIncrement(QtCore.QSize(2, 0))
        self.lineeditSearchGlosses.setObjectName(_fromUtf8("lineeditSearchGlosses"))
        self.gridLayout_2.addWidget(self.lineeditSearchGlosses, 3, 1, 1, 1)
        self.label_6 = QtGui.QLabel(self.tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setSizeIncrement(QtCore.QSize(1, 0))
        self.label_6.setText(QtGui.QApplication.translate("MainWindow", "Translations:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout_2.addWidget(self.label_6, 4, 0, 1, 1)
        self.lineeditSearchTranslations = QtGui.QLineEdit(self.tab)
        self.lineeditSearchTranslations.setSizeIncrement(QtCore.QSize(2, 0))
        self.lineeditSearchTranslations.setObjectName(_fromUtf8("lineeditSearchTranslations"))
        self.gridLayout_2.addWidget(self.lineeditSearchTranslations, 4, 1, 1, 1)
        self.groupBox = QtGui.QGroupBox(self.tab)
        self.groupBox.setTitle(QtGui.QApplication.translate("MainWindow", "Search Options", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.radiobuttonAnd = QtGui.QRadioButton(self.groupBox)
        self.radiobuttonAnd.setText(QtGui.QApplication.translate("MainWindow", "AND", None, QtGui.QApplication.UnicodeUTF8))
        self.radiobuttonAnd.setChecked(True)
        self.radiobuttonAnd.setObjectName(_fromUtf8("radiobuttonAnd"))
        self.verticalLayout_4.addWidget(self.radiobuttonAnd)
        self.radiobuttonOr = QtGui.QRadioButton(self.groupBox)
        self.radiobuttonOr.setText(QtGui.QApplication.translate("MainWindow", "OR", None, QtGui.QApplication.UnicodeUTF8))
        self.radiobuttonOr.setObjectName(_fromUtf8("radiobuttonOr"))
        self.verticalLayout_4.addWidget(self.radiobuttonOr)
        self.checkboxInvert = QtGui.QCheckBox(self.groupBox)
        self.checkboxInvert.setText(QtGui.QApplication.translate("MainWindow", "NOT", None, QtGui.QApplication.UnicodeUTF8))
        self.checkboxInvert.setObjectName(_fromUtf8("checkboxInvert"))
        self.verticalLayout_4.addWidget(self.checkboxInvert)
        self.checkboxContained = QtGui.QCheckBox(self.groupBox)
        self.checkboxContained.setText(QtGui.QApplication.translate("MainWindow", "contained matches", None, QtGui.QApplication.UnicodeUTF8))
        self.checkboxContained.setObjectName(_fromUtf8("checkboxContained"))
        self.verticalLayout_4.addWidget(self.checkboxContained)
        self.gridLayout_2.addWidget(self.groupBox, 0, 3, 5, 1)
        self.line_2 = QtGui.QFrame(self.tab)
        self.line_2.setFrameShape(QtGui.QFrame.VLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.gridLayout_2.addWidget(self.line_2, 0, 2, 5, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.gridLayout.addWidget(self.tabWidget, 2, 1, 1, 6)
        self.buttonAlignCenter = QtGui.QToolButton(self.centralWidget)
        self.buttonAlignCenter.setText(QtGui.QApplication.translate("MainWindow", "...", None, QtGui.QApplication.UnicodeUTF8))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/pixmaps/aligncenter.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonAlignCenter.setIcon(icon)
        self.buttonAlignCenter.setIconSize(QtCore.QSize(24, 24))
        self.buttonAlignCenter.setCheckable(True)
        self.buttonAlignCenter.setAutoRaise(True)
        self.buttonAlignCenter.setObjectName(_fromUtf8("buttonAlignCenter"))
        self.gridLayout.addWidget(self.buttonAlignCenter, 12, 6, 1, 1)
        self.buttonAlignLeft = QtGui.QToolButton(self.centralWidget)
        self.buttonAlignLeft.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.buttonAlignLeft.setText(QtGui.QApplication.translate("MainWindow", "...", None, QtGui.QApplication.UnicodeUTF8))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/pixmaps/alignleft.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonAlignLeft.setIcon(icon1)
        self.buttonAlignLeft.setIconSize(QtCore.QSize(24, 24))
        self.buttonAlignLeft.setCheckable(True)
        self.buttonAlignLeft.setChecked(True)
        self.buttonAlignLeft.setAutoRaise(True)
        self.buttonAlignLeft.setObjectName(_fromUtf8("buttonAlignLeft"))
        self.gridLayout.addWidget(self.buttonAlignLeft, 12, 5, 1, 1)
        self.buttonClearThisSearch = QtGui.QPushButton(self.centralWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonClearThisSearch.sizePolicy().hasHeightForWidth())
        self.buttonClearThisSearch.setSizePolicy(sizePolicy)
        self.buttonClearThisSearch.setText(QtGui.QApplication.translate("MainWindow", "Clear This Search", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonClearThisSearch.setObjectName(_fromUtf8("buttonClearThisSearch"))
        self.gridLayout.addWidget(self.buttonClearThisSearch, 3, 1, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout)
        MainWindow.setCentralWidget(self.centralWidget)
        self.statusBar = QtGui.QStatusBar(MainWindow)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        MainWindow.setStatusBar(self.statusBar)
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 957, 23))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        self.menuFiel = QtGui.QMenu(self.menuBar)
        self.menuFiel.setTitle(QtGui.QApplication.translate("MainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFiel.setObjectName(_fromUtf8("menuFiel"))
        self.menuEdit = QtGui.QMenu(self.menuBar)
        self.menuEdit.setTitle(QtGui.QApplication.translate("MainWindow", "Edit", None, QtGui.QApplication.UnicodeUTF8))
        self.menuEdit.setObjectName(_fromUtf8("menuEdit"))
        self.menuAbout = QtGui.QMenu(self.menuBar)
        self.menuAbout.setTitle(QtGui.QApplication.translate("MainWindow", "About", None, QtGui.QApplication.UnicodeUTF8))
        self.menuAbout.setObjectName(_fromUtf8("menuAbout"))
        MainWindow.setMenuBar(self.menuBar)
        self.actionQuit = QtGui.QAction(MainWindow)
        self.actionQuit.setText(QtGui.QApplication.translate("MainWindow", "Quit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionQuit.setObjectName(_fromUtf8("actionQuit"))
        self.actionAddFiles = QtGui.QAction(MainWindow)
        self.actionAddFiles.setText(QtGui.QApplication.translate("MainWindow", "Add Files...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAddFiles.setObjectName(_fromUtf8("actionAddFiles"))
        self.actionRemoveFiles = QtGui.QAction(MainWindow)
        self.actionRemoveFiles.setText(QtGui.QApplication.translate("MainWindow", "Remove Files", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRemoveFiles.setObjectName(_fromUtf8("actionRemoveFiles"))
        self.actionNewProject = QtGui.QAction(MainWindow)
        self.actionNewProject.setText(QtGui.QApplication.translate("MainWindow", "New Project", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNewProject.setObjectName(_fromUtf8("actionNewProject"))
        self.actionSaveProject = QtGui.QAction(MainWindow)
        self.actionSaveProject.setText(QtGui.QApplication.translate("MainWindow", "Save Project", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSaveProject.setObjectName(_fromUtf8("actionSaveProject"))
        self.actionSaveProjectAs = QtGui.QAction(MainWindow)
        self.actionSaveProjectAs.setText(QtGui.QApplication.translate("MainWindow", "Save Project As...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSaveProjectAs.setObjectName(_fromUtf8("actionSaveProjectAs"))
        self.actionEditWordClasses = QtGui.QAction(MainWindow)
        self.actionEditWordClasses.setText(QtGui.QApplication.translate("MainWindow", "Edit Word Classes...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionEditWordClasses.setObjectName(_fromUtf8("actionEditWordClasses"))
        self.actionSearches = QtGui.QAction(MainWindow)
        self.actionSearches.setText(QtGui.QApplication.translate("MainWindow", "Searches...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSearches.setObjectName(_fromUtf8("actionSearches"))
        self.actionAboutPoioAnalyzer = QtGui.QAction(MainWindow)
        self.actionAboutPoioAnalyzer.setText(QtGui.QApplication.translate("MainWindow", "About PoioAnalyzer...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAboutPoioAnalyzer.setObjectName(_fromUtf8("actionAboutPoioAnalyzer"))
        self.actionQuickSearch = QtGui.QAction(MainWindow)
        self.actionQuickSearch.setText(QtGui.QApplication.translate("MainWindow", "Quick Search", None, QtGui.QApplication.UnicodeUTF8))
        self.actionQuickSearch.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+F", None, QtGui.QApplication.UnicodeUTF8))
        self.actionQuickSearch.setObjectName(_fromUtf8("actionQuickSearch"))
        self.menuFiel.addAction(self.actionNewProject)
        self.menuFiel.addAction(self.actionSaveProject)
        self.menuFiel.addAction(self.actionSaveProjectAs)
        self.menuFiel.addSeparator()
        self.menuFiel.addAction(self.actionQuit)
        self.menuEdit.addAction(self.actionAddFiles)
        self.menuEdit.addAction(self.actionRemoveFiles)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionEditWordClasses)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionSearches)
        self.menuEdit.addAction(self.actionQuickSearch)
        self.menuAbout.addAction(self.actionAboutPoioAnalyzer)
        self.menuBar.addAction(self.menuFiel.menuAction())
        self.menuBar.addAction(self.menuEdit.menuAction())
        self.menuBar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.tabWidget, self.lineeditSearchUtterances)
        MainWindow.setTabOrder(self.lineeditSearchUtterances, self.lineeditSearchWords)
        MainWindow.setTabOrder(self.lineeditSearchWords, self.lineeditSearchMorphemes)
        MainWindow.setTabOrder(self.lineeditSearchMorphemes, self.lineeditSearchGlosses)
        MainWindow.setTabOrder(self.lineeditSearchGlosses, self.lineeditSearchTranslations)
        MainWindow.setTabOrder(self.lineeditSearchTranslations, self.radiobuttonAnd)
        MainWindow.setTabOrder(self.radiobuttonAnd, self.radiobuttonOr)
        MainWindow.setTabOrder(self.radiobuttonOr, self.checkboxInvert)
        MainWindow.setTabOrder(self.checkboxInvert, self.checkboxContained)
        MainWindow.setTabOrder(self.checkboxContained, self.buttonClearThisSearch)
        MainWindow.setTabOrder(self.buttonClearThisSearch, self.buttonClearAllSearches)
        MainWindow.setTabOrder(self.buttonClearAllSearches, self.buttonSaveSearches)
        MainWindow.setTabOrder(self.buttonSaveSearches, self.buttonSearch)
        MainWindow.setTabOrder(self.buttonSearch, self.listFiles)
        MainWindow.setTabOrder(self.listFiles, self.texteditInterlinear)
        MainWindow.setTabOrder(self.texteditInterlinear, self.buttonAlignLeft)
        MainWindow.setTabOrder(self.buttonAlignLeft, self.buttonAlignCenter)
        MainWindow.setTabOrder(self.buttonAlignCenter, self.buttonAddFiles)
        MainWindow.setTabOrder(self.buttonAddFiles, self.buttonRemoveFiles)
        MainWindow.setTabOrder(self.buttonRemoveFiles, self.lineeditQuickSearch)

    def retranslateUi(self, MainWindow):
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QtGui.QApplication.translate("MainWindow", "Search 1", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QtGui.QApplication.translate("MainWindow", "New Search...", None, QtGui.QApplication.UnicodeUTF8))

from PoioIlTextEdit import PoioIlTextEdit
import poioanalyzer_rc
