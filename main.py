import sys
import json
from PyQt6 import QtWidgets, QtGui
from PyQt6.QtCore import Qt
from MainWindow import Ui_MainWindow
from create_alley import Ui_create_alley
from PyQt6.QtWidgets import QTableWidgetItem, QMessageBox


class AlignDelegate(QtWidgets.QStyledItemDelegate):  # Делегат центрирования по ячейкам
    def initStyleOption(self, option, index):
        super(AlignDelegate, self).initStyleOption(option, index)
        option.displayAlignment = Qt.AlignmentFlag.AlignCenter


class ColorDelegate(QtWidgets.QStyledItemDelegate):  # Делегат цвета балки
    def initStyleOption(self, option, index):
        super(ColorDelegate, self).initStyleOption(option, index)
        option.backgroundBrush = QtGui.QColor('red')


class WhiteColorDelegate(QtWidgets.QStyledItemDelegate):  # Делегат цвета балки
    def initStyleOption(self, option, index):
        super(WhiteColorDelegate, self).initStyleOption(option, index)
        option.backgroundBrush = QtGui.QColor('white')


class CreateAlleyWindow(QtWidgets.QMainWindow, Ui_create_alley):
    def __init__(self, parent=None):
        super(CreateAlleyWindow, self).__init__(parent)
        self.setupUi(self)

        self.cancel_btn.clicked.connect(lambda: self.close())
        self.create_alley_btn.clicked.connect(self.create_alley)

    def create_alley(self):
        table = self.single_create_table
        empty_flag = True
        for i in range(table.rowCount() - 1):
            if table.item(i, 1).text():
                empty_flag = False
            else:
                empty_flag = True
                break

        if empty_flag is True:
            QMessageBox.warning(self, "Error", "Fields are empty")
        else:
            alley_index = table.item(0, 1).text()
            rows = table.item(0, 2).text()
            cols = table.item(0, 3).text()
            start_level = table.item(0, 4).text()
            start_cell = table.item(0, 5).text()
            count_of_barcodes = table.item(0, 6).text()
            local_direction = table.item(0, 7).text()
            alley_index = 113
            self.topology['alley'][str(alley_index)] = {'rows': rows,
                                                        'columns': cols,
                                                        'list_of_balks': [3 for _ in range(cols // 3)],
                                                        'extra_cells': [],
                                                        'count_of_barcodes': count_of_barcodes,
                                                        'start_level': start_level,
                                                        'start_cell': (cols - 1) * ((alley_index + 1) % 2) + 1,
                                                        'local_direction': alley_index % 2}


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

        # Настройки меню
        self.open.setShortcut('Ctrl+O')

        # Настройки таблицы
        table = self.tableWidget
        table.setFocusPolicy(Qt.FocusPolicy.NoFocus)  # Убирает выделение элемента при нажатии
        delegate = AlignDelegate(table)  # Выравнивание
        table.setItemDelegate(delegate)  # таблицы по центру
        self.upper_table.setItemDelegate(delegate)

        # Привязка функций
        self.delete_button.clicked.connect(self.delete_alley)
        self.listWidget.clicked.connect(self.item_clicked)
        self.create_button.clicked.connect(self.create_alley_window)
        self.open.triggered.connect(self.menu_open)

        self.topology = self.open_file("Hennessy.txt")

    def menu_open(self):
        file = QtWidgets.QFileDialog.getOpenFileName(self, "Open Topology", "", "Text Files (*.txt)")[0]
        self.topology = self.open_file(str(file))

    def add_beam(self, col):  # Добавляет одну балку
        table = self.tableWidget

        table.insertColumn(col)
        table.horizontalHeader().resizeSection(col, 10)
        delegate = ColorDelegate(table)
        table.setItemDelegateForColumn(col, delegate)

    def add_beams(self, beam_list):  # Добавляет ВСЕ балки
        count = 1
        self.add_beam(count)

        for n in beam_list:
            count += n + 1
            self.add_beam(count)

    def table_headers(self, col_count, row_count, start_level, start_cell, local_direction):
        table = self.tableWidget

        # Горизонтальные заголовки
        if local_direction == 0:
            num = start_cell - col_count + 2
            for col in range(1, col_count):
                table.setItem(0, col, QTableWidgetItem(str(num)))
                num += 1
        elif local_direction == 1:
            num = col_count + start_cell - 2
            for col in range(1, col_count):
                table.setItem(0, col, QTableWidgetItem(str(num)))
                num -= 1

        # Вертикальные заголовки
        row_num = start_level
        for row in range(row_count-1, 0, -1):
            table.setItem(row, 0, QTableWidgetItem(str(row_num)))
            row_num += 1

    def create_table(self, row_count, col_count, beam_list, start_level, start_cell, local_direction):
        table = self.tableWidget

        # Очищаем таблицу от старых значений
        self.clear_table()
        row_count += 1
        col_count += 1

        # Параметры таблицы
        table.setRowCount(row_count)
        table.setColumnCount(col_count)

        self.table_headers(col_count, row_count, start_level, start_cell, local_direction)
        self.add_beams(beam_list)

    def open_file(self, file):
        table = self.upper_table
        self.clear_table()
        self.listWidget.clear()
        self.listWidget_2.clear()

        MainWindow.setWindowTitle(self, file)
        with open(file) as content:
            topology = json.load(content)
        for key in topology['alley']:
            self.listWidget.addItem(key)

        self.upper_table.setRowCount(0)
        self.upper_table.setRowCount(1)
        table.setItem(0, 0, QTableWidgetItem("Photo: " + str(topology['photo'])))
        table.setItem(0, 1, QTableWidgetItem("Uniq bar: " + str(topology['uniq_bar'])))
        table.setItem(0, 2, QTableWidgetItem("Extra bar: " + str(topology['extra_bar'])))
        table.setItem(0, 3, QTableWidgetItem("Extra cells: " + str(topology['extra_cells'])))

        return topology

    def item_clicked(self):
        right_list = self.listWidget_2
        item = self.listWidget.currentItem()
        alley = self.topology['alley'][item.text()]
        self.create_table(alley['rows'], alley['columns'], alley['list_of_balks'], alley['start_level'],
                          alley['start_cell'], alley['local_direction'])
        right_list.clear()
        right_list.addItem("Rows = " + str(alley['rows']))
        right_list.addItem("Columns = " + str(alley['columns']))
        right_list.addItem("Start level = " + str(alley['start_level']))
        right_list.addItem("Start cell = " + str(alley['start_cell']))
        right_list.addItem("Count of barcodes: " + str(alley['count_of_barcodes']))
        right_list.addItem("Local direction = " + str(alley['local_direction']))

    def clear_table(self):
        table = self.tableWidget
        delegate = WhiteColorDelegate(table)
        table.setItemDelegate(delegate)
        for col in range(table.columnCount()):
            table.setItemDelegateForColumn(col, delegate)
        table.resizeColumnsToContents()
        table.setRowCount(0)
        table.setColumnCount(0)

    def delete_alley(self):
        left_list = self.listWidget
        if left_list.selectedItems():
            alley = left_list.selectedItems()[0].text()
            row = left_list.selectedIndexes()[0].row()
            self.topology["alley"].pop(alley)
            left_list.takeItem(row)

    def create_alley_window(self):
        dialog = CreateAlleyWindow(self)
        dialog.show()


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()


if __name__ == '__main__':
    main()
