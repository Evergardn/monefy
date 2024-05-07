from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QDialog, QLineEdit, QHBoxLayout
from PySide6.QtGui import QPainter, QColor, QBrush, QPen, QPixmap
from PySide6.QtCore import Qt, Signal
import sqlite3
import logger

class AddFunDialog(QDialog):
    fun_added = Signal(float)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Расходы")
        self.setFixedSize(200, 100)

        self.bel = QLabel("Введите сумму:", self)
        self.bel.setStyleSheet("color: black;")
        self.vue_label = QLabel("Стоимость:", self)
        self.vue_input = QLineEdit(self)
        self.vue_input.setStyleSheet("color: black;")
        self.a_button = QPushButton("Добавить", self)
        self.a_button.setStyleSheet("color: black;")

        layout = QVBoxLayout(self)
        layout.addWidget(self.bel)
        layout.addWidget(self.vue_label)
        layout.addWidget(self.vue_input)
        layout.addWidget(self.a_button)

        self.a_button.clicked.connect(self.add_fun_to_db)

    def add_fun_to_db(self):
        value_text = self.vue_input.text()
        if value_text:
            try:
                value = float(value_text.replace(',', '.'))
                self.fun_added.emit(value)
                self.accept()

                conn = sqlite3.connect('cash.db')
                cursor = conn.cursor()
                cursor.execute('INSERT INTO expenses (Type, Quantity, Time) VALUES (?, ?, datetime("now", "localtime"))', ('fun', value))
                conn.commit()
                conn.close()
            except ValueError as e:
                logger.error(e)