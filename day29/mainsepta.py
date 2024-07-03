# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class Ui_Dialog(object):
    def setupUi(self, Dialog):


        Dialog.setObjectName("Dialog")
        Dialog.resize(1047, 823)
        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(360, 130, 351, 521))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.tabelcatatan = QtWidgets.QTableWidget(self.layoutWidget)
        self.tabelcatatan.setObjectName("tabelcatatan")
        self.tabelcatatan.setColumnCount(1)
        self.tabelcatatan.setRowCount(0)
        self.tabelcatatan.setHorizontalHeaderLabels(["Catatan"])
        self.gridLayout.addWidget(self.tabelcatatan, 3, 0, 1, 2)
        self.tambahcatatan = QtWidgets.QPushButton(self.layoutWidget)
        self.tambahcatatan.setObjectName("tambahcatatan")
        self.gridLayout.addWidget(self.tambahcatatan, 4, 1, 1, 1)
        self.inputteks = QtWidgets.QLineEdit(self.layoutWidget)
        self.inputteks.setObjectName("inputteks")
        self.gridLayout.addWidget(self.inputteks, 2, 0, 1, 2)
        self.pencaricatatan = QtWidgets.QPushButton(self.layoutWidget)
        self.pencaricatatan.setObjectName("pencaricatatan")
        self.gridLayout.addWidget(self.pencaricatatan, 2, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 2)
        self.hapuscatatanyangdipilih = QtWidgets.QPushButton(self.layoutWidget)
        self.hapuscatatanyangdipilih.setObjectName("hapuscatatanyangdipilih")
        self.gridLayout.addWidget(self.hapuscatatanyangdipilih, 4, 0, 1, 1)

        self.retranslateUi(Dialog)
        self.hapuscatatanyangdipilih.clicked.connect(self.hapus_catatan_yang_dipilih)
        self.tambahcatatan.clicked.connect(self.tambah_catatan)
        self.pencaricatatan.clicked.connect(self.cari_catatan)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.tambahcatatan.setText(_translate("Dialog", "Tambah"))
        self.pencaricatatan.setText(_translate("Dialog", "Cari"))
        self.label.setText(_translate("Dialog", "SEMUA CATATAN"))
        self.hapuscatatanyangdipilih.setText(_translate("Dialog", "Hapus"))

    def tambah_catatan(self):
        text = self.inputteks.text()
        if text:
            row_count = self.tabelcatatan.rowCount()
            self.tabelcatatan.insertRow(row_count)
            self.tabelcatatan.setItem(row_count, 0, QtWidgets.QTableWidgetItem(text))
            self.inputteks.clear()

    def cari_catatan(self):
        search_text = self.inputteks.text()
        for row in range(self.tabelcatatan.rowCount()):
            item = self.tabelcatatan.item(row, 0)
            if item and search_text.lower() in item.text().lower():
                item.setSelected(True)
            else:
                item.setSelected(False)

    def hapus_catatan_yang_dipilih(self):
        selected_rows = self.tabelcatatan.selectionModel().selectedRows()
        for index in sorted(selected_rows):
            self.tabelcatatan.removeRow(index.row())

class DialogApp(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super(DialogApp, self).__init__(parent)
        self.setupUi(self)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    dialog = DialogApp()
    dialog.show()
    sys.exit(app.exec_())
