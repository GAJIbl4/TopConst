import sys
import json

import PyQt6.QtGui
from PyQt6 import QtWidgets, QtGui, QtCore
from MainWindow import Ui_MainWindow
from create_alley import Ui_create_alley
from PyQt6.QtWidgets import QTableWidgetItem, QMessageBox, QFileDialog


class AlignDelegate(QtWidgets.QStyledItemDelegate):  # Делегат центрирования по ячейкам
    def initStyleOption(self, option, index):
        super(AlignDelegate, self).initStyleOption(option, index)
        option.displayAlignment = QtCore.Qt.AlignmentFlag.AlignCenter


class ColorDelegate(QtWidgets.QStyledItemDelegate):  # Делегат цвета балки
    def initStyleOption(self, option, index):
        super(ColorDelegate, self).initStyleOption(option, index)
        option.backgroundBrush = QtGui.QColor('red')


class WhiteColorDelegate(QtWidgets.QStyledItemDelegate):  # Делегат цвета балки
    def initStyleOption(self, option, index):
        super(WhiteColorDelegate, self).initStyleOption(option, index)
        option.backgroundBrush = QtGui.QColor('white')


class TopConst(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super(TopConst, self).__init__(*args, **kwargs)
        self.new_alley = None
        self.setupUi(self)
        self.left_list = self.left_list
        self.topology = None
        self.topology_file = None
        self.current_alley = None
        self.buffer = {'alley': {}}

        # Настройки меню
        self.open.setShortcut('Ctrl+O')
        self.create_topology.setShortcut('Ctrl+N')

        # Настройки основной таблицы
        table = self.tableWidget
        table.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)  # Убирает выделение элемента при нажатии
        delegate = AlignDelegate(table)  # Выравнивание
        table.setItemDelegate(delegate)  # таблицы по центру
        self.upper_table.setItemDelegate(delegate)

        # Настройка верхней таблицы
        up_table = self.upper_table
        value = 60
        header = (up_table.width() - (3 * value)) // 3
        up_table.setColumnWidth(0, header)
        up_table.setColumnWidth(1, value)
        up_table.setColumnWidth(2, header)
        up_table.setColumnWidth(3, value)
        up_table.setColumnWidth(4, header)
        up_table.setColumnWidth(5, value)
        up_table.setSpan(2, 1, 1, 5)
        self.check_box = QtWidgets.QCheckBox()
        self.check_box.setStyleSheet("margin-left:24%;")
        up_table.setCellWidget(3, 1, self.check_box)

        # Привязка функций
        self.delete_button.clicked.connect(self.delete_alley)
        self.left_list.itemClicked.connect(self.item_clicked)
        self.left_list.itemChanged.connect(self.item_changed)
        self.create_button.clicked.connect(self.create_alley_window)
        self.open.triggered.connect(self.menu_open)
        self.alley_change_button.clicked.connect(self.alley_change)
        self.check_box.toggled.connect(self.photo_checkbox_change)

        # Настройка контекстного меню левого списка
        self.act_copy = PyQt6.QtGui.QAction("Copy")
        self.act_paste = PyQt6.QtGui.QAction("Paste")
        self.act_copy.setShortcut('Ctrl+C')
        self.act_paste.setShortcut('Ctrl+V')
        self.act_copy.triggered.connect(self.copy_alley)
        self.act_paste.triggered.connect(self.paste_alley)
        self.listWidget.addAction(self.act_copy)
        self.listWidget.addAction(self.act_paste)

    def copy_alley(self):
        if self.listWidget.selectedItems():
            self.buffer = {'alley': {}}
            for alley in self.listWidget.selectedItems():
                alley_name = alley.text()
                self.buffer['alley'][alley_name] = self.topology['alley'][alley_name]

    def paste_alley(self):
        if self.buffer:
            self.listWidget.itemChanged.disconnect(self.item_changed)
            i = self.listWidget.count()
            items = [self.left_list.item(x).text() for x in range(i)]

            for alley_name in self.buffer['alley'].keys():
                self.topology['alley'][alley_name + '_copy'] = self.buffer['alley'][alley_name]

                if alley_name + '_copy' not in items:
                    self.listWidget.addItem(alley_name + '_copy')
                    item = self.listWidget.item(i)
                    item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                    item.setFlags(item.flags() | QtCore.Qt.ItemFlag.ItemIsEditable)
                i += 1

            with open(self.topology_file, 'w') as fd:
                json.dump(self.topology, fd)
            fd.close()
            self.listWidget.itemChanged.connect(self.item_changed)

    def menu_open(self):  # Кнопка "Открыть" в меню
        self.topology_file = QFileDialog.getOpenFileName(self, "Open Topology", "", "Text Files (*.txt)")[0]
        if self.topology_file:
            self.topology = self.open_file(str(self.topology_file))
        else:
            return

    def add_beam(self, col):  # Добавляет одну балку
        table = self.tableWidget

        table.insertColumn(col)
        table.horizontalHeader().resizeSection(col, 10)
        delegate = ColorDelegate(table)
        table.setItemDelegateForColumn(col, delegate)

    def add_beams(self, beam_list, local_dir):  # Добавляет ВСЕ балки
        count = 1
        self.add_beam(count)

        if local_dir == 0:
            for n in beam_list:
                count += n + 1
                self.add_beam(count)
        else:
            for n in beam_list[::-1]:
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
        for row in range(row_count - 1, 0, -1):
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
        self.add_beams(beam_list, local_direction)

    def open_file(self, file):
        table = self.upper_table
        self.clear_table()
        self.listWidget.clear()

        TopConst.setWindowTitle(self, file)  # В названии окна будет местоположение файла с топологией
        with open(file) as content:
            topology = json.load(content)
        i = 0
        # Вырубаем обработчик событий от греха подальше, точнее от ложных срабатываний
        self.listWidget.itemChanged.disconnect(self.item_changed)
        for key in topology['alley']:  # Закидываем аллеи в список слева
            self.listWidget.addItem(key)
            item = self.listWidget.item(i)
            item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
            item.setFlags(item.flags() | QtCore.Qt.ItemFlag.ItemIsEditable)
            i += 1
        # Включаем обработчик событий обратно
        self.listWidget.itemChanged.connect(self.item_changed)

        # Очистка верхней таблицы
        table.setItem(0, 1, QTableWidgetItem(""))
        table.setItem(0, 3, QTableWidgetItem(""))
        table.setItem(0, 5, QTableWidgetItem(""))
        table.setItem(1, 1, QTableWidgetItem(""))
        table.setItem(1, 3, QTableWidgetItem(""))
        table.setItem(1, 5, QTableWidgetItem(""))
        table.setItem(2, 1, QTableWidgetItem(""))
        table.setItem(3, 3, QTableWidgetItem(str(topology['uniq_bar'])))

        if topology['photo'] == 2:
            self.check_box.setCheckState(QtCore.Qt.CheckState.Checked)
        elif topology['photo'] == 0:
            self.check_box.setCheckState(QtCore.Qt.CheckState.Unchecked)
        else:
            self.check_box.setCheckState(QtCore.Qt.CheckState.Unchecked)

        return topology

    def item_clicked(self):
        table = self.upper_table
        item = self.listWidget.currentItem()
        self.current_alley = item.text()
        alley = self.topology['alley'][item.text()]
        self.create_table(alley['rows'], alley['columns'], alley['list_of_balks'], alley['start_level'],
                          alley['start_cell'], alley['local_direction'])

        table.setItem(0, 1, QTableWidgetItem(str(alley['rows'])))
        table.setItem(0, 3, QTableWidgetItem(str(alley['columns'])))
        table.setItem(0, 5, QTableWidgetItem(str(alley['start_level'])))
        table.setItem(1, 1, QTableWidgetItem(str(alley['start_cell'])))
        table.setItem(1, 3, QTableWidgetItem(str(alley['count_of_barcodes'])))
        table.setItem(1, 5, QTableWidgetItem(str(alley['local_direction'])))
        table.setItem(2, 1, QTableWidgetItem(str(alley['list_of_balks'])))

    def item_changed(self):
        print('CHANGED')
        if self.listWidget.currentItem():
            alley = self.topology['alley'][self.current_alley]
            self.topology["alley"].pop(self.current_alley)
            self.topology['alley'][self.listWidget.currentItem().text()] = alley
            with open(self.topology_file, 'w') as fd:
                json.dump(self.topology, fd)
            fd.close()

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
            for item in left_list.selectedItems():
                alley = item.text()
                row = left_list.row(item)
                self.topology["alley"].pop(alley)
                left_list.takeItem(row)
            with open(self.topology_file, 'w') as fd:
                json.dump(self.topology, fd)
            fd.close()

    def alley_change(self):
        left_list = self.listWidget
        up_table = self.upper_table
        if left_list.selectedItems():
            current_alley = self.topology['alley'][left_list.selectedItems()[0].text()]
            if sum(eval(up_table.item(2, 1).text())) < int(up_table.item(0, 3).text()):
                QMessageBox.warning(self, "Error", "Не хватает балок!")
            elif sum(eval(up_table.item(2, 1).text())) > int(up_table.item(0, 3).text()):
                QMessageBox.warning(self, "Error", "Не хватает ячеек!")
            else:
                current_alley['rows'] = int(up_table.item(0, 1).text())
                current_alley['columns'] = int(up_table.item(0, 3).text())
                current_alley['start_level'] = int(up_table.item(0, 5).text())
                current_alley['start_cell'] = int(up_table.item(1, 1).text())
                current_alley['count_of_barcodes'] = int(up_table.item(1, 3).text())
                current_alley['local_direction'] = int(up_table.item(1, 5).text())
                current_alley['list_of_balks'] = eval(up_table.item(2, 1).text())
                self.create_table(current_alley['rows'], current_alley['columns'], current_alley['list_of_balks'],
                                  current_alley['start_level'], current_alley['start_cell'],
                                  current_alley['local_direction'])
                self.topology['uniq_bar'] = eval(up_table.item(3, 3).text())

                with open(self.topology_file, 'w') as fd:
                    json.dump(self.topology, fd)
                fd.close()
        else:
            QMessageBox.information(self, "Ошибка!", "Сначала аллею выбери, потом жми!")

    def photo_checkbox_change(self):
        if self.topology:
            if self.check_box.isChecked() is True:
                self.topology['photo'] = 2
            elif self.check_box.isChecked() is False:
                self.topology['photo'] = 0

            with open(self.topology_file, 'w') as fd:
                json.dump(self.topology, fd)
            fd.close()

    def create_alley_window(self):
        if not self.topology_file:
            QMessageBox.warning(self, "Error", "Не выбран файл с топологией")
        else:
            if not self.new_alley:
                self.new_alley = CreateAlleyWindow(self)
                self.new_alley.show()
            else:
                self.new_alley.show()


class CreateAlleyWindow(QtWidgets.QDialog, Ui_create_alley):
    def __init__(self, parent):
        super(CreateAlleyWindow, self).__init__(parent)
        self.setupUi(self)
        self.settings_dict = None
        self.alley_index = None

        self.alley_buttonbox.rejected.connect(self.close)
        self.alley_buttonbox.accepted.connect(self.accept_button)

    def accept_button(self):
        table = self.new_pallet_table

        for i in range(table.rowCount() - 1):
            if not table.item(i, 1).text():
                QMessageBox.warning(self, "Error", "Некоторые поля пусты")
                return

        self.parse_settings()

        if sum(self.settings_dict['list_of_balks']) != self.settings_dict['columns']:
            QMessageBox.warning(self, "Error", "Ошибка в количестве балок и/или в количестве паллет")
            return
        else:
            self.parent().topology['alley'][self.alley_index] = self.settings_dict
            items = [self.parent().left_list.item(x).text() for x in range(0, self.parent().left_list.count())]
            if self.alley_index not in items:
                self.parent().listWidget.itemChanged.disconnect(self.parent().item_changed)

                self.parent().left_list.addItem(self.alley_index)
                n = self.parent().left_list.count()
                self.parent().left_list.item(n - 1).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

                self.parent().listWidget.itemChanged.connect(self.parent().item_changed)

            with open(self.parent().topology_file, 'w') as fd:
                json.dump(self.parent().topology, fd)
            fd.close()

            self.close()

    def parse_settings(self):
        table = self.new_pallet_table

        self.alley_index = table.item(0, 1).text()
        cols = int(table.item(2, 1).text())
        self.settings_dict = {'rows': int(table.item(1, 1).text()),
                              'columns': cols,
                              'list_of_balks': eval(table.item(3, 1).text()),
                              'start_level': int(table.item(4, 1).text()),
                              'start_cell': int(table.item(5, 1).text()),
                              'count_of_barcodes': int(table.item(6, 1).text()),
                              'local_direction': int(table.item(7, 1).text()),
                              'extra_cells': []}


def main():
    sys.excepthook = my_excepthook
    app = QtWidgets.QApplication(sys.argv)
    window = TopConst()
    window.show()
    app.exec()


def my_excepthook(type_error, value, t_back):
    QMessageBox.critical(TopConst(), "CRITICAL ERROR", str(value))
    sys.__excepthook__(type_error, value, t_back)


if __name__ == '__main__':
    main()
