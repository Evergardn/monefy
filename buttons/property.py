from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QDialog, QLineEdit, QHBoxLayout
from PySide6.QtGui import QPainter, QColor, QBrush, QPen, QPixmap
from PySide6.QtCore import Qt, Signal
import sqlite3
import logger

class AddPropertyDialog(QDialog):
    property_added = Signal(float)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Расходы")
        self.setFixedSize(200, 100)

        self.label = QLabel("Введите сумму:", self)
        self.label.setStyleSheet("color: black;")
        self.value_label = QLabel("Стоимость:", self)
        self.value_input = QLineEdit(self)
        self.value_input.setStyleSheet("color: black;")
        self.add_button = QPushButton("Добавить", self)
        self.add_button.setStyleSheet("color: black;")

        layout = QVBoxLayout(self)
        layout.addWidget(self.label)
        layout.addWidget(self.value_label)
        layout.addWidget(self.value_input)
        layout.addWidget(self.add_button)

        self.add_button.clicked.connect(self.add_property_to_db)

    def add_property_to_db(self):
        value_text = self.value_input.text()
        if value_text:
            try:
                value = float(value_text.replace(',', '.'))
                self.property_added.emit(value)
                self.accept()

                conn = sqlite3.connect('cash.db')
                cursor = conn.cursor()
                cursor.execute('INSERT INTO expenses (Type, Quantity, Time) VALUES (?, ?, datetime("now", "localtime"))', ('property', value))
                conn.commit()
                conn.close()
            except ValueError as e:
                logger.error(e)

        