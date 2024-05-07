from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QDialog, QLineEdit, QHBoxLayout
from PySide6.QtGui import QPainter, QColor, QBrush, QPen, QPixmap
from PySide6.QtCore import Qt, Signal
import sqlite3
import logger

class AddSportDialog(QDialog):
    sport_added = Signal(float)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Добавить 'Веселье'")
        self.setFixedSize(200, 100)

        self.lbel = QLabel("Введите сумму:", self)
        self.lbel.setStyleSheet("color: black;")
        self.vaue_label = QLabel("Стоимость:", self)
        self.vaue_input = QLineEdit(self)
        self.vaue_input.setStyleSheet("color: black;")
        self.ad_button = QPushButton("Добавить", self)
        self.ad_button.setStyleSheet("color: black;")

        layout = QVBoxLayout(self)
        layout.addWidget(self.lbel)
        layout.addWidget(self.vaue_label)
        layout.addWidget(self.vaue_input)
        layout.addWidget(self.ad_button)

        self.ad_button.clicked.connect(self.add_sport_to_db)

    def add_sport_to_db(self):
        value_text = self.vaue_input.text()
        if value_text:
            try:
                value = float(value_text.replace(',', '.'))
                self.sport_added.emit(value)
                self.accept()

                conn = sqlite3.connect('cash.db')
                cursor = conn.cursor()
                cursor.execute('INSERT INTO expenses (Type, Quantity, Time) VALUES (?, ?, datetime("now", "localtime"))', ('sport', value))
                conn.commit()
                conn.close()
            except ValueError as e:
                logger.error(e)