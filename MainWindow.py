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
        MainWindow.resize(1070, 450)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(".\\../../Users/GAJIb/.designer/backup/logo.jpg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(0, -1, -1, -1)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.upper_table = QtWidgets.QTableWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.upper_table.sizePolicy().hasHeightForWidth())
        self.upper_table.setSizePolicy(sizePolicy)
        self.upper_table.setMinimumSize(QtCore.QSize(570, 90))
        self.upper_table.setMaximumSize(QtCore.QSize(570, 92))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        self.upper_table.setFont(font)
        self.upper_table.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.upper_table.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.upper_table.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.upper_table.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.upper_table.setTextElideMode(QtCore.Qt.TextElideMode.ElideMiddle)
        self.upper_table.setShowGrid(True)
        self.upper_table.setGridStyle(QtCore.Qt.PenStyle.SolidLine)
        self.upper_table.setRowCount(3)
        self.upper_table.setColumnCount(8)
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
        self.upper_table.setItem(0, 6, item)
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
        self.upper_table.horizontalHeader().setVisible(False)
        self.upper_table.horizontalHeader().setCascadingSectionResizes(True)
        self.upper_table.horizontalHeader().setDefaultSectionSize(110)
        self.upper_table.verticalHeader().setVisible(False)
        self.upper_table.verticalHeader().setCascadingSectionResizes(True)
        self.upper_table.verticalHeader().setSortIndicatorShown(False)
        self.horizontalLayout.addWidget(self.upper_table)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint)
        self.horizontalLayout_3.setContentsMargins(0, -1, -1, -1)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.unique_filter_table = QtWidgets.QTableWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.unique_filter_table.sizePolicy().hasHeightForWidth())
        self.unique_filter_table.setSizePolicy(sizePolicy)
        self.unique_filter_table.setMaximumSize(QtCore.QSize(180, 92))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.unique_filter_table.setFont(font)
        self.unique_filter_table.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.ActionsContextMenu)
        self.unique_filter_table.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.unique_filter_table.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.unique_filter_table.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.unique_filter_table.setRowCount(3)
        self.unique_filter_table.setColumnCount(2)
        self.unique_filter_table.setObjectName("unique_filter_table")
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.NoBrush)
        item.setBackground(brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.NoBrush)
        item.setForeground(brush)
        item.setFlags(QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.unique_filter_table.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.unique_filter_table.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.unique_filter_table.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.unique_filter_table.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.unique_filter_table.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.unique_filter_table.setItem(2, 1, item)
        self.unique_filter_table.horizontalHeader().setVisible(False)
        self.unique_filter_table.horizontalHeader().setDefaultSectionSize(90)
        self.unique_filter_table.verticalHeader().setVisible(False)
        self.horizontalLayout_3.addWidget(self.unique_filter_table)
        self.extra_filter_table = QtWidgets.QTableWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.extra_filter_table.sizePolicy().hasHeightForWidth())
        self.extra_filter_table.setSizePolicy(sizePolicy)
        self.extra_filter_table.setMaximumSize(QtCore.QSize(180, 92))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        self.extra_filter_table.setFont(font)
        self.extra_filter_table.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.ActionsContextMenu)
        self.extra_filter_table.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.extra_filter_table.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.extra_filter_table.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.extra_filter_table.setRowCount(3)
        self.extra_filter_table.setColumnCount(2)
        self.extra_filter_table.setObjectName("extra_filter_table")
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setBold(False)
        font.setWeight(50)
        item.setFont(font)
        item.setFlags(QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.extra_filter_table.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.extra_filter_table.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.extra_filter_table.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.extra_filter_table.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.extra_filter_table.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.extra_filter_table.setItem(2, 1, item)
        self.extra_filter_table.horizontalHeader().setVisible(False)
        self.extra_filter_table.horizontalHeader().setDefaultSectionSize(90)
        self.extra_filter_table.verticalHeader().setVisible(False)
        self.horizontalLayout_3.addWidget(self.extra_filter_table)
        self.horizontalLayout.addLayout(self.horizontalLayout_3)
        self.alley_change_button = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.alley_change_button.sizePolicy().hasHeightForWidth())
        self.alley_change_button.setSizePolicy(sizePolicy)
        self.alley_change_button.setMinimumSize(QtCore.QSize(95, 92))
        self.alley_change_button.setLayoutDirection(QtCore.Qt.LayoutDirection.RightToLeft)
        self.alley_change_button.setObjectName("alley_change_button")
        self.horizontalLayout.addWidget(self.alley_change_button)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.verticalLayout.addItem(spacerItem)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint)
        self.formLayout.setObjectName("formLayout")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setMinimumSize(QtCore.QSize(0, 200))
        self.tableWidget.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SelectionMode.NoSelection)
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
        self.tableWidget.verticalHeader().setDefaultSectionSize(30)
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.tableWidget)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint)
        self.verticalLayout_3.setContentsMargins(-1, 0, 0, 0)
        self.verticalLayout_3.setSpacing(8)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.left_list = QtWidgets.QListWidget(self.centralwidget)
        self.left_list.setMaximumSize(QtCore.QSize(200, 16777215))
        self.left_list.setSizeIncrement(QtCore.QSize(0, 0))
        self.left_list.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.ActionsContextMenu)
        self.left_list.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.left_list.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.SizeAdjustPolicy.AdjustIgnored)
        self.left_list.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.DoubleClicked)
        self.left_list.setDragEnabled(False)
        self.left_list.setSelectionMode(QtWidgets.QAbstractItemView.SelectionMode.ExtendedSelection)
        self.left_list.setTextElideMode(QtCore.Qt.TextElideMode.ElideMiddle)
        self.left_list.setViewMode(QtWidgets.QListView.ViewMode.ListMode)
        self.left_list.setObjectName("left_list")
        self.verticalLayout_3.addWidget(self.left_list)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.create_button = QtWidgets.QPushButton(self.centralwidget)
        self.create_button.setObjectName("create_button")
        self.horizontalLayout_2.addWidget(self.create_button)
        self.delete_button = QtWidgets.QPushButton(self.centralwidget)
        self.delete_button.setObjectName("delete_button")
        self.horizontalLayout_2.addWidget(self.delete_button)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.formLayout.setLayout(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.verticalLayout_3)
        self.verticalLayout.addLayout(self.formLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1070, 26))
        self.menubar.setObjectName("menubar")
        self.file_menu = QtWidgets.QMenu(self.menubar)
        self.file_menu.setObjectName("file_menu")
        self.export_menu = QtWidgets.QMenu(self.menubar)
        self.export_menu.setObjectName("export_menu")
        self.help_menu = QtWidgets.QMenu(self.menubar)
        self.help_menu.setObjectName("help_menu")
        MainWindow.setMenuBar(self.menubar)
        self.open = QtGui.QAction(MainWindow)
        self.open.setCheckable(False)
        self.open.setObjectName("open")
        self.create_topology = QtGui.QAction(MainWindow)
        self.create_topology.setObjectName("create_topology")
        self.alley_table_export = QtGui.QAction(MainWindow)
        self.alley_table_export.setObjectName("alley_table_export")
        self.about_action = QtGui.QAction(MainWindow)
        self.about_action.setObjectName("about_action")
        self.file_menu.addAction(self.open)
        self.file_menu.addAction(self.create_topology)
        self.export_menu.addAction(self.alley_table_export)
        self.help_menu.addAction(self.about_action)
        self.menubar.addAction(self.file_menu.menuAction())
        self.menubar.addAction(self.export_menu.menuAction())
        self.menubar.addAction(self.help_menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Topology Constructor"))
        __sortingEnabled = self.upper_table.isSortingEnabled()
        self.upper_table.setSortingEnabled(False)
        item = self.upper_table.item(0, 0)
        item.setText(_translate("MainWindow", "Rows"))
        item = self.upper_table.item(0, 2)
        item.setText(_translate("MainWindow", "Columns"))
        item = self.upper_table.item(0, 4)
        item.setText(_translate("MainWindow", "Start level"))
        item = self.upper_table.item(0, 6)
        item.setText(_translate("MainWindow", "Photo"))
        item = self.upper_table.item(1, 0)
        item.setText(_translate("MainWindow", "Start cell"))
        item = self.upper_table.item(1, 2)
        item.setText(_translate("MainWindow", "Count of barcodes"))
        item = self.upper_table.item(1, 4)
        item.setText(_translate("MainWindow", "Local direction"))
        item = self.upper_table.item(2, 0)
        item.setText(_translate("MainWindow", "List of balks"))
        self.upper_table.setSortingEnabled(__sortingEnabled)
        __sortingEnabled = self.unique_filter_table.isSortingEnabled()
        self.unique_filter_table.setSortingEnabled(False)
        item = self.unique_filter_table.item(0, 0)
        item.setText(_translate("MainWindow", "Unique barcodes"))
        self.unique_filter_table.setSortingEnabled(__sortingEnabled)
        __sortingEnabled = self.extra_filter_table.isSortingEnabled()
        self.extra_filter_table.setSortingEnabled(False)
        item = self.extra_filter_table.item(0, 0)
        item.setText(_translate("MainWindow", "Extra barcodes"))
        self.extra_filter_table.setSortingEnabled(__sortingEnabled)
        self.alley_change_button.setText(_translate("MainWindow", "ВЖУХ"))
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
        self.left_list.setSortingEnabled(False)
        self.create_button.setText(_translate("MainWindow", "Добавить"))
        self.delete_button.setText(_translate("MainWindow", "Удалить"))
        self.file_menu.setTitle(_translate("MainWindow", "Файл"))
        self.export_menu.setTitle(_translate("MainWindow", "Экспорт"))
        self.help_menu.setTitle(_translate("MainWindow", "Помощь"))
        self.open.setText(_translate("MainWindow", "Открыть топологию"))
        self.create_topology.setText(_translate("MainWindow", "Создать топологию"))
        self.alley_table_export.setText(_translate("MainWindow", "Таблица аллей"))
        self.about_action.setText(_translate("MainWindow", "О программе"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
