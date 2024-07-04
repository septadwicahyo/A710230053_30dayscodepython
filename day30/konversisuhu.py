# konversisuhu.py
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QVBoxLayout, QWidget, QPushButton, QComboBox

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Konversi Suhu")
        self.setGeometry(100, 100, 300, 200)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()

        # Input Label dan Line Edit
        self.input_label = QLabel("Masukkan Suhu:")
        self.input_field = QLineEdit()

        # ComboBox untuk memilih satuan suhu
        self.scale_combo = QComboBox()
        self.scale_combo.addItems(["Celsius", "Fahrenheit", "Kelvin"])

        # Tombol untuk melakukan konversi
        self.convert_button = QPushButton("Konversi")
        self.convert_button.clicked.connect(self.convert_temperature)

        # Label untuk menampilkan hasil konversi
        self.result_label = QLabel("Hasil Konversi:")

        # Menyusun widget dalam layout
        self.layout.addWidget(self.input_label)
        self.layout.addWidget(self.input_field)
        self.layout.addWidget(self.scale_combo)
        self.layout.addWidget(self.convert_button)
        self.layout.addWidget(self.result_label)

        self.central_widget.setLayout(self.layout)

    def convert_temperature(self):
        # Membaca input suhu
        try:
            input_value = float(self.input_field.text())
        except ValueError:
            self.result_label.setText("Input tidak valid! Masukkan angka.")
            return

        # Membaca skala suhu yang dipilih
        scale = self.scale_combo.currentText()

        # Melakukan konversi suhu
        if scale == "Celsius":
            fahrenheit = (input_value * 9/5) + 32
            kelvin = input_value + 273.15
            self.result_label.setText(f"Celsius: {input_value:.2f} °C\n"
                                       f"Fahrenheit: {fahrenheit:.2f} °F\n"
                                       f"Kelvin: {kelvin:.2f} K")
        elif scale == "Fahrenheit":
            celsius = (input_value - 32) * 5/9
            kelvin = celsius + 273.15
            self.result_label.setText(f"Fahrenheit: {input_value:.2f} °F\n"
                                       f"Celsius: {celsius:.2f} °C\n"
                                       f"Kelvin: {kelvin:.2f} K")
        elif scale == "Kelvin":
            celsius = input_value - 273.15
            fahrenheit = (celsius * 9/5) + 32
            self.result_label.setText(f"Kelvin: {input_value:.2f} K\n"
                                       f"Celsius: {celsius:.2f} °C\n"
                                       f"Fahrenheit: {fahrenheit:.2f} °F")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
