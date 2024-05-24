from PySide6.QtWidgets import QDialog, QLabel, QPushButton, QLineEdit, QVBoxLayout
from PySide6.QtGui import QPainter, QColor, QBrush, QPixmap, QFont
from PySide6.QtCore import Signal
from services.add_to_db import add_data_to_db
from services.remove_from_db import remove_data_from_db
import functools

class AddBalanceDialog(QDialog):
    balance_added = Signal(float, str)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Добавить баланс")
        self.setFixedSize(200, 100)

        self.amount_label = QLabel("Сумма:", self)
        self.amount_label.setStyleSheet("color: #d2d5d3;")

        self.amount_input = QLineEdit(self)
        self.amount_input.setStyleSheet("color: #d2d5d3;")
        
        self.add_button = QPushButton("Добавить", self)
        self.add_button.setStyleSheet("color: #d2d5d3;")

        layout = QVBoxLayout(self)
        layout.addWidget(self.amount_label)
        layout.addWidget(self.amount_input)
        layout.addWidget(self.add_button)

        USER_ID = 2
        self.add_button.clicked.connect(functools.partial(self.handle_add_button_click, USER_ID))

    def handle_add_button_click(self, user_id):
        amount_text = self.amount_input.text()
        try:
            amount = float(amount_text)
            add_data_to_db(user_id, amount)
            self.balance_added.emit(amount, 'add')
            self.accept()
        except ValueError:
            print("Invalid amount entered.")


class RemoveBalanceDialog(QDialog):
    balance_removed = Signal(float, str)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Вычесть баланс")
        
        self.setFixedSize(200, 100)

        self.amount_label = QLabel("Сумма:", self)
        self.amount_label.setStyleSheet("color: #d2d5d3;")

        self.amount_input = QLineEdit(self)
        self.amount_input.setStyleSheet("color: #d2d5d3;")

        self.remove_button = QPushButton("Вычесть", self)
        self.remove_button.setStyleSheet("color: #d2d5d3;")

        layout = QVBoxLayout(self)
        layout.addWidget(self.amount_label)
        layout.addWidget(self.amount_input)
        layout.addWidget(self.remove_button)

        USER_ID = 2
        self.remove_button.clicked.connect(functools.partial(self.handle_remove_button_click, USER_ID))

    def handle_remove_button_click(self, user_id):
        amount_text = self.amount_input.text()
        try:
            amount = float(amount_text)
            remove_data_from_db(user_id, amount)
            self.balance_removed.emit(amount, 'remove')
            self.accept()
        except ValueError:
            print("Invalid amount entered.")

