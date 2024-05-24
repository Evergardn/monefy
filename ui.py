import sys
import math
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QDialog, QLineEdit, QHBoxLayout, QInputDialog, QColorDialog
from PySide6.QtGui import QPainter, QColor, QBrush, QPixmap, QFont
from PySide6.QtCore import Qt, Signal
from dialogs import *
from services.get_balance_from_db import get_balance
from buttons.food import AddFoodDialog

class CircleWidget(QWidget):
    outer_color = QColor("#aaa8ab")
    circle_color = QColor("#FFEBD8")

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Monefy")
        self.setStyleSheet("background-color: #FFEBD8;")
        self.setGeometry(100, 100, 700, 700)
        self.segment_data = {}

        self.income_label = QLabel("0,00 грн.", self)
        self.income_label.setStyleSheet("color: #60c48e; font-size: 12pt;")
        self.income_label.setFont(QFont("Inter", 14, QFont.Thin))
        self.income_label.setAlignment(Qt.AlignCenter)

        self.expenses_label = QLabel("0,00 грн.", self)
        self.expenses_label.setStyleSheet("color: rgb(202, 128, 131); font-size: 12pt;")
        self.expenses_label.setFont(QFont("Inter", 14, QFont.Thin))
        self.expenses_label.setAlignment(Qt.AlignCenter)

        self.balance_amount = 0.00
        self.balance_label = QLabel(f"Баланс: 0.00 грн.", self)
        self.balance_label.setStyleSheet("background-color: #60c48e; color: #d2d5d3; font-size: 12pt;")
        self.balance_label.setFont(QFont("Inter", 14, QFont.Thin))
        self.balance_label.setAlignment(Qt.AlignCenter)
        self.balance_label.move(250, 650)
        self.balance_label.resize(200, 30)

        self.add_balance = QPushButton(f'+', self)
        self.add_balance.setStyleSheet("color: black; font-size: 12pt;")
        self.add_balance.setGeometry(455, 650, 30, 30)
        self.add_balance.clicked.connect(self.balance)

        self.remove_balance = QPushButton(f'-', self)
        self.remove_balance.setStyleSheet("color: black; font-size: 12pt;")
        self.remove_balance.setGeometry(215, 650, 30, 30)
        self.remove_balance.clicked.connect(self.rem_balance)

        button_properties = [
            ("img/food.png", "food_button"),
            ("img/property.png", "property_button"),
            ("img/cafe.png", "cafe_button"),
            ("img/hygiene.png", "hygiene_button"),
            ("img/sport.png", "sport_button"),
            ("img/health.png", "health_button"),
            ("img/connection.png", "connection_button"),
            ("img/pet.png", "pet_button"),
            ("img/present.png", "present_button"),
            ("img/clothes.png", "clothes_button"),
            ("img/taxi.png", "taxi_button"),
            ("img/fun.png", "fun_button"),
            ("img/transport.png", "transport_button"),
            ("img/car.png", "car_button"),
        ]

        self.create_circle_buttons(button_properties, radius=230, button_size=75)

    def create_circle_buttons(self, button_properties, radius, button_size):
        center_x = self.width() // 2
        center_y = self.height() // 2
        angle_step = 360 / len(button_properties)

        for i, (icon_path, name) in enumerate(button_properties):
            angle = math.radians(i * angle_step)
            x = center_x + int(radius * math.cos(angle)) - button_size // 2
            y = center_y + int(radius * math.sin(angle)) - button_size // 2

            button = QPushButton(self)
            button.setObjectName(name)
            button.setGeometry(x, y, button_size, button_size)
            button.setStyleSheet(
                f"QPushButton {{"
                f"   background-image: url({icon_path});"
                f"   border-radius: 10px;"
                f"}}"
                f"QPushButton:pressed {{"
                f"   background-color: rgba(0, 0, 0, 0.3);"
                f"}}"
            )
            button.clicked.connect(self.handle_click_button)

    def handle_click_button(self):
        button = self.sender()
        button_name = button.objectName()
        print(f'Button {button_name} was clicked')
        if button_name == 'food_button':
            dialog = AddFoodDialog(self)
            dialog.exec()

    def resizeEvent(self, event):
        self.update_label_positions()
        super().resizeEvent(event)

    def update_label_positions(self):
        inner_circle_radius = 100
        center_x = self.width() // 2
        center_y = self.height() // 2

        self.income_label.resize(150, 30)
        self.income_label.move(center_x - self.income_label.width() // 2, center_y - self.income_label.height())

        self.expenses_label.resize(150, 30)
        self.expenses_label.move(center_x - self.expenses_label.width() // 2, center_y)


    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        self.drawOuterCircle(painter)
        self.drawInnerCircle(painter)

    def drawOuterCircle(self, painter):
        painter.setBrush(QBrush(self.outer_color))
        painter.setPen(Qt.NoPen)
        outer_circle_radius = 150
        outer_circle_x = (self.width() - outer_circle_radius * 2) / 2
        outer_circle_y = (self.height() - outer_circle_radius * 2) / 2
        painter.drawEllipse(outer_circle_x, outer_circle_y, outer_circle_radius * 2, outer_circle_radius * 2)

    def drawInnerCircle(self, painter):
        painter.setBrush(QBrush(self.circle_color))
        painter.setPen(Qt.NoPen)
        inner_circle_radius = 100
        inner_circle_x = (self.width() - inner_circle_radius * 2) / 2
        inner_circle_y = (self.height() - inner_circle_radius * 2) / 2
        painter.drawEllipse(inner_circle_x, inner_circle_y, inner_circle_radius * 2, inner_circle_radius * 2)

    def balance(self):
        dialog = AddBalanceDialog()
        dialog.balance_added.connect(self.update_balance)
        dialog.exec()

    def rem_balance(self):
        dialog = RemoveBalanceDialog()
        dialog.balance_removed.connect(self.update_balance)
        dialog.exec()

    def update_balance(self, amount, operation):
        if operation == 'add':
            income_amount = float(self.income_label.text().replace(',', '.').replace(' грн.', ''))
            income_amount += amount
            self.income_label.setText(f"{income_amount:.2f} грн.")

            self.balance_amount += amount
        elif operation == 'remove':
            expenses_amount = float(self.expenses_label.text().replace(',', '.').replace(' грн.', ''))
            expenses_amount += abs(amount)
            self.expenses_label.setText(f"{expenses_amount:.2f} грн.")

            self.balance_amount -= amount

        self.balance_label.setText(f"Баланс: {self.balance_amount:.2f} грн.")