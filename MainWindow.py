# Form implementation generated from reading ui file '.\main.ui'
#
# Created by: PyQt6 UI code generator 6.1.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 440)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(1000, 440))
        MainWindow.setMaximumSize(QtCore.QSize(1000, 440))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(".\\logo.jpg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(193, 143, 797, 261))
        self.tableWidget.setTextElideMode(QtCore.Qt.TextElideMode.ElideMiddle)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(QtCore.Qt.PenStyle.SolidLine)
        self.tableWidget.setRowCount(9)
        self.tableWidget.setColumnCount(30)
        self.tableWidget.setObjectName("tableWidget")
        item = QtWidgets.QTableWidgetItem()
        item.setBackground(QtGui.QColor(0, 255, 0))
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setBackground(QtGui.QColor(0, 255, 0))
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(30)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(2)
        self.tableWidget.verticalHeader().setVisible(False)
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(13, 143, 170, 231))
        self.listWidget.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.ActionsContextMenu)
        self.listWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.listWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.SizeAdjustPolicy.AdjustIgnored)
        self.listWidget.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.DoubleClicked)
        self.listWidget.setDragEnabled(False)
        self.listWidget.setSelectionMode(QtWidgets.QAbstractItemView.SelectionMode.ExtendedSelection)
        self.listWidget.setTextElideMode(QtCore.Qt.TextElideMode.ElideMiddle)
        self.listWidget.setViewMode(QtWidgets.QListView.ViewMode.ListMode)
        self.listWidget.setObjectName("listWidget")
        self.upper_table = QtWidgets.QTableWidget(self.centralwidget)
        self.upper_table.setGeometry(QtCore.QRect(13, 10, 911, 120))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.upper_table.setFont(font)
        self.upper_table.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.upper_table.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.upper_table.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.upper_table.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.upper_table.setTextElideMode(QtCore.Qt.TextElideMode.ElideMiddle)
        self.upper_table.setShowGrid(True)
        self.upper_table.setRowCount(4)
        self.upper_table.setColumnCount(6)
        self.upper_table.setObjectName("upper_table")
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        item.setFlags(QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.upper_table.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        item.setFlags(QtCore.Qt.ItemFlag.ItemIsUserCheckable|QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.upper_table.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        item.setFlags(QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.upper_table.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        item.setFlags(QtCore.Qt.ItemFlag.ItemIsUserCheckable|QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.upper_table.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        item.setFlags(QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.upper_table.setItem(0, 4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        item.setFlags(QtCore.Qt.ItemFlag.ItemIsSelectable|QtCore.Qt.ItemFlag.ItemIsEditable|QtCore.Qt.ItemFlag.ItemIsDragEnabled|QtCore.Qt.ItemFlag.ItemIsUserCheckable|QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.upper_table.setItem(0, 5, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        item.setFlags(QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.upper_table.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.upper_table.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        item.setFlags(QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.upper_table.setItem(1, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.upper_table.setItem(1, 3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        item.setFlags(QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.upper_table.setItem(1, 4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        item.setFlags(QtCore.Qt.ItemFlag.ItemIsSelectable|QtCore.Qt.ItemFlag.ItemIsEditable|QtCore.Qt.ItemFlag.ItemIsDragEnabled|QtCore.Qt.ItemFlag.ItemIsUserCheckable|QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.upper_table.setItem(1, 5, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        item.setFlags(QtCore.Qt.ItemFlag.ItemIsUserCheckable|QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.upper_table.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.upper_table.setItem(2, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.upper_table.setItem(2, 3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.upper_table.setItem(2, 4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        item.setFlags(QtCore.Qt.ItemFlag.ItemIsUserCheckable|QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.upper_table.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        item.setFlags(QtCore.Qt.ItemFlag.ItemIsSelectable|QtCore.Qt.ItemFlag.ItemIsEditable|QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.upper_table.setItem(3, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        item.setFlags(QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.upper_table.setItem(3, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.upper_table.setItem(3, 3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.upper_table.setItem(3, 4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.upper_table.setItem(3, 5, item)
        self.upper_table.horizontalHeader().setVisible(False)
        self.upper_table.horizontalHeader().setDefaultSectionSize(150)
        self.upper_table.horizontalHeader().setMinimumSectionSize(30)
        self.upper_table.horizontalHeader().setStretchLastSection(True)
        self.upper_table.verticalHeader().setVisible(False)
        self.create_button = QtWidgets.QPushButton(self.centralwidget)
        self.create_button.setGeometry(QtCore.QRect(20, 380, 61, 23))
        self.create_button.setObjectName("create_button")
        self.delete_button = QtWidgets.QPushButton(self.centralwidget)
        self.delete_button.setGeometry(QtCore.QRect(100, 380, 61, 23))
        self.delete_button.setObjectName("delete_button")
        self.alley_change_button = QtWidgets.QPushButton(self.centralwidget)
        self.alley_change_button.setGeometry(QtCore.QRect(930, 10, 61, 120))
        self.alley_change_button.setObjectName("alley_change_button")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 21))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.open = QtGui.QAction(MainWindow)
        self.open.setCheckable(False)
        self.open.setObjectName("open")
        self.create_topology = QtGui.QAction(MainWindow)
        self.create_topology.setObjectName("create_topology")
        self.menu.addAction(self.open)
        self.menu.addAction(self.create_topology)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Topology Constructor"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "1"))
        self.listWidget.setSortingEnabled(True)
        __sortingEnabled = self.upper_table.isSortingEnabled()
        self.upper_table.setSortingEnabled(False)
        item = self.upper_table.item(0, 0)
        item.setText(_translate("MainWindow", "Rows"))
        item = self.upper_table.item(0, 2)
        item.setText(_translate("MainWindow", "Columns"))
        item = self.upper_table.item(0, 4)
        item.setText(_translate("MainWindow", "Start level"))
        item = self.upper_table.item(1, 0)
        item.setText(_translate("MainWindow", "Start cell"))
        item = self.upper_table.item(1, 2)
        item.setText(_translate("MainWindow", "Count of barcodes"))
        item = self.upper_table.item(1, 4)
        item.setText(_translate("MainWindow", "Local direction"))
        item = self.upper_table.item(2, 0)
        item.setText(_translate("MainWindow", "List of balks"))
        item = self.upper_table.item(3, 0)
        item.setText(_translate("MainWindow", "Photo"))
        item = self.upper_table.item(3, 2)
        item.setText(_translate("MainWindow", "Uniq bar"))
        self.upper_table.setSortingEnabled(__sortingEnabled)
        self.create_button.setText(_translate("MainWindow", "Добавить"))
        self.delete_button.setText(_translate("MainWindow", "Удалить"))
        self.alley_change_button.setText(_translate("MainWindow", "ВЖУХ"))
        self.menu.setTitle(_translate("MainWindow", "Файл"))
        self.open.setText(_translate("MainWindow", "Открыть топологию"))
        self.create_topology.setText(_translate("MainWindow", "Создать топологию"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
