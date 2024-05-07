from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QDialog, QLineEdit, QHBoxLayout
from PySide6.QtGui import QPainter, QColor, QBrush, QPen, QPixmap
from PySide6.QtCore import Qt, Signal
from PyQt5.QtCore import QObject, pyqtSlot
import sqlite3
import logger
from datetime import datetime

class AddBalanceDialog(QDialog):
    balance_added = Signal(float)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Добавить баланс")
        self.setFixedSize(200, 100)

        self.amount_label = QLabel("Сумма:", self)
        self.amount_label.setStyleSheet("color: black;")
        self.amount_input = QLineEdit(self)
        self.amount_input.setStyleSheet("color: black;")
        self.add_button = QPushButton("Добавить", self)
        self.add_button.setStyleSheet("color: black;")

        layout = QVBoxLayout(self)
        layout.addWidget(self.amount_label)
        layout.addWidget(self.amount_input)
        layout.addWidget(self.add_button)

        self.add_button.clicked.connect(self.add_balance_to_db)

    def add_balance_to_db(self):
        amount_text = self.amount_input.text()
        if amount_text:
            try:
                amount = float(amount_text.replace(',', '.'))
                self.balance_added.emit(amount)
                self.accept()

                conn = sqlite3.connect('cash.db')
                cursor = conn.cursor()
                cursor.execute('INSERT INTO balance (User_id, Amount, Time) VALUES (?, ?, ?)', (1, amount, datetime.now()))
                conn.commit()
                conn.close()
            except ValueError:
                pass

class RemoveBalanceDialog(QDialog):
    balance_removed = Signal(float)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Вычесть баланс")
        self.setFixedSize(200, 100)

        self.amount_label = QLabel("Сумма:", self)
        self.amount_label.setStyleSheet("color: black;")
        self.amount_input = QLineEdit(self)
        self.amount_input.setStyleSheet("color: black;")
        self.remove_button = QPushButton("Вычесть", self)
        self.remove_button.setStyleSheet("color: black;")

        layout = QVBoxLayout(self)
        layout.addWidget(self.amount_label)
        layout.addWidget(self.amount_input)
        layout.addWidget(self.remove_button)

        self.remove_button.clicked.connect(self.remove_balance_from_db)

    def remove_balance_from_db(self):
        amount_text = self.amount_input.text()
        if amount_text:
            try:
                amount = float(amount_text.replace(',', '.'))
                self.balance_removed.emit(amount)
                self.accept()

                conn = sqlite3.connect('cash.db')
                cursor = conn.cursor()
                cursor.execute('''
                    UPDATE balance
                    SET Amount = Amount - ?
                    WHERE rowid = (SELECT rowid FROM balance ORDER BY rowid DESC LIMIT 1)
                ''', (amount,))
                conn.commit()
                conn.close()
            except ValueError:
                pass