import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QTextEdit, QListWidget

class NoteManager(QWidget):
    def __init__(self):
        super().__init__()
        self.notes = []
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Pengelola Catatan')

        self.textEdit = QTextEdit(self)
        self.textEdit.setPlaceholderText('Masukkan catatan baru...')

        self.listWidget = QListWidget(self)

        self.btnAdd = QPushButton('Tambahkan Catatan', self)
        self.btnAdd.clicked.connect(self.addNote)

        self.btnDelete = QPushButton('Hapus Catatan', self)
        self.btnDelete.clicked.connect(self.deleteNote)

        layout = QVBoxLayout()
        layout.addWidget(self.textEdit)
        layout.addWidget(self.listWidget)
        layout.addWidget(self.btnAdd)
        layout.addWidget(self.btnDelete)

        self.setLayout(layout)
        self.show()

    def addNote(self):
        note = self.textEdit.toPlainText()
        if note:  # Pastikan catatan tidak kosong
            self.notes.append(note)
            self.listWidget.addItem(note)
            self.textEdit.clear()

    def deleteNote(self):
        selectedItems = self.listWidget.selectedItems()
        if not selectedItems: return
        for item in selectedItems:
            note = item.text()
            row = self.listWidget.row(item)
            del self.notes[row]
            self.listWidget.takeItem(row)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = NoteManager()
    sys.exit(app.exec_())
