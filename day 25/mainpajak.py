import sys
from PyQt5.QtWidgets import QApplication, QDialog
from pajak import Ui_Dialog  # Assuming your UI class is named 'Ui_Dialog'

class DialogWindow(QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super(DialogWindow, self).__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.calculate_tax)

    def calculate_tax(self):
        harga = float(self.lineEditHarga.text())
        pajak_percentage = float(self.lineEditPajak.currentText().strip('%'))
        total = harga + (harga * pajak_percentage / 100)
        self.label_4.setText(f"Total Harga Beserta Pajak Anda: {total:.2f} rupiah")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DialogWindow()
    window.show()
    sys.exit(app.exec_())
