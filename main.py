import sys
import json
from PyQt6 import QtWidgets, QtGui
from PyQt6.QtCore import Qt
from MainWindow import Ui_MainWindow
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


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

        # Настройки таблицы
        table = self.tableWidget
        table.setFocusPolicy(Qt.FocusPolicy.NoFocus)  # Убирает выделение элемента при нажатии
        delegate = AlignDelegate(table)  # Выравнивание
        table.setItemDelegate(delegate)  # таблицы по центру

        l_list = self.listWidget
        l_list.clicked.connect(self.item_clicked)

        beam_list = [3, 3, 3, 3, 4]
        self.create_table(8, 16, beam_list, 2, 1, 1)
        self.topology = self.open_file('Hennesy.txt')

        # self.Open.triggered.connect(self.menu_open())

    def menu_open(self):  # Не работает
        file = QtWidgets.QFileDialog.getOpenFileName(self, "Open Image", "/home/jana", "Text Files (*.txt)")
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
        left_list = self.listWidget
        with open(file) as content:
            topology = json.load(content)
        for key in topology['alley']:
            left_list.addItem(key)
        return topology

    def item_clicked(self):
        right_list = self.listWidget_2
        item = self.listWidget.currentItem()
        alley = self.topology['alley'][item.text()]
        self.create_table(alley['rows'], alley['columns'], alley['list_of_balks'], alley['start_level'],
                          alley['start_cell'], alley['local_direction'])
        right_list.clear()
        right_list.addItem("Photo: " + str(self.topology['photo']))
        right_list.addItem("Uniq bar: " + str(self.topology['uniq_bar']))
        right_list.addItem("Extra bar: " + str(self.topology['extra_bar']))
        right_list.addItem("Extra cells: " + str(self.topology['extra_cells']))
        right_list.addItem("Count of barcodes: " + str(alley['count_of_barcodes']))

    def clear_table(self):
        table = self.tableWidget
        delegate = WhiteColorDelegate(table)
        table.setItemDelegate(delegate)
        for col in range(table.columnCount()):
            table.setItemDelegateForColumn(col, delegate)
        table.resizeColumnsToContents()

        table.setRowCount(0)
        table.setColumnCount(0)


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()


if __name__ == '__main__':
    main()
