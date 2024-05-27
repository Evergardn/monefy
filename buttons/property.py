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

        self.value_label = QLabel("Стоимость:", self)
        self.value_input = QLineEdit(self)
        self.value_input.setStyleSheet("color: black;")
        self.add_button = QPushButton("Добавить", self)
        self.add_button.setStyleSheet("color: black;")

        layout = QVBoxLayout(self)
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
                user_id = '2'
                type_to_check = 'property'

                cursor.execute('SELECT Type FROM expenses WHERE User_id = ?', (user_id,))
                existing_type = cursor.fetchone()

                if existing_type and existing_type[0] == type_to_check:
                    cursor.execute('UPDATE expenses SET Quantity = ?, Time = datetime("now", "localtime") WHERE User_id = ? AND Type = ?', (value, user_id, type_to_check))
                    print(f'{type_to_check.capitalize()} updated')
                else:
                    cursor.execute('INSERT INTO expenses (User_id, Type, Quantity, Time) VALUES (?, ?, ?, datetime("now", "localtime"))', (user_id, type_to_check, value))
                    print(f'{type_to_check.capitalize()} inserted')
                conn.commit()
                conn.close()
            except ValueError as e:
                logger.error(e)

        