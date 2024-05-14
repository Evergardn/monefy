from PySide6.QtWidgets import QWidget, QLabel, QPushButton
from PySide6.QtGui import QPainter, QColor, QBrush
from PySide6.QtCore import Qt
 
class CircleWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Monefy")
        self.setGeometry(100, 100, 700, 700)
        self.setStyleSheet("background-color: #FFEBD8;")
        self.user_id = None

        self.income_label = QLabel("0,00 грн.", self)
        self.income_label.setStyleSheet("color: #4a8763; font-size: 12pt;")
        self.income_label.setAlignment(Qt.AlignCenter)
        self.income_label.move(310, 280)
        self.income_label.resize(100, 30)

        self.expenses_label = QLabel("0,00 грн.", self)
        self.expenses_label.setStyleSheet("color: rgb(202, 128, 131); font-size: 12pt;")
        self.expenses_label.setAlignment(Qt.AlignCenter)
        self.expenses_label.move(310, 330)
        self.expenses_label.resize(100, 30)


        self.balance_amount = 0.00
        self.balance_label = QLabel(f"Баланс: {self.balance_amount:.2f} грн.", self)
        self.balance_label.setStyleSheet("background-color: rgb(176, 229, 196); color: white; font-size: 12pt;")
        self.balance_label.setAlignment(Qt.AlignCenter)
        self.balance_label.move(295, 650)
        self.balance_label.resize(150, 30)

        self.add_balance = QPushButton(f'+', self)
        self.add_balance.setStyleSheet("color: black; font-size: 12pt;")
        self.add_balance.setGeometry(450, 650, 50, 50)
        self.add_balance.resize(30, 30)

        self.remove_balance = QPushButton(f'-', self)
        self.remove_balance.setStyleSheet("color: black; font-size: 12pt;")
        self.remove_balance.setGeometry(260, 650, 50, 50)
        self.remove_balance.resize(30, 30)

        self.food_button = QPushButton(self)
        self.food_button.setGeometry(50, 40, 75, 75)
        self.food_button.setStyleSheet(
    "QPushButton {"
    "   background-image: url(img/food.png);"
    "   border-radius: 10px;"
    "}"
    "QPushButton:pressed {"
    "   background-color: rgba(0, 0, 0, 0.3);"
    "}"
)

        self.property_button = QPushButton(self)
        self.property_button.setGeometry(50, 160, 75, 75)
        self.property_button.setStyleSheet(
    "QPushButton {"
    "   background-image: url(img/property.png);"
    "   border-radius: 10px;"
    "}"
    "QPushButton:pressed {"
    "   background-color: rgba(0, 0, 0, 0.3);"
    "}"
)

        self.cafe_button = QPushButton(self)
        self.cafe_button.setGeometry(50, 290, 75, 75)
        self.cafe_button.setStyleSheet(
    "QPushButton {"
    "   background-image: url(img/cafe.png);"
    "   border-radius: 10px;"
    "}"
    "QPushButton:pressed {"
    "   background-color: rgba(0, 0, 0, 0.3);"
    "}"
)

        self.hygiene_button = QPushButton(self)
        self.hygiene_button.setGeometry(50, 420, 75, 75)
        self.hygiene_button.setStyleSheet(
    "QPushButton {"
    "   background-image: url(img/hygiene.png);"
    "   border-radius: 10px;"
    "}"
    "QPushButton:pressed {"
    "   background-color: rgba(0, 0, 0, 0.3);"
    "}"
)
        self.sport_button = QPushButton(self)
        self.sport_button.setGeometry(50, 540, 75, 75)
        self.sport_button.setStyleSheet(
    "QPushButton {"
    "   background-image: url(img/sport.png);"
    "   border-radius: 10px;"
    "}"
    "QPushButton:pressed {"
    "   background-color: rgba(0, 0, 0, 0.3);"
    "}"
)

        self.health_button = QPushButton(self)
        self.health_button.setGeometry(220, 540, 75, 75)
        self.health_button.setStyleSheet(
    "QPushButton {"
    "   background-image: url(img/health.png);"
    "   border-radius: 10px;"
    "}"
    "QPushButton:pressed {"
    "   background-color: rgba(0, 0, 0, 0.3);"
    "}"
)

        self.connection_button = QPushButton(self)
        self.connection_button.setGeometry(390, 540, 75, 75)
        self.connection_button.setStyleSheet(
    "QPushButton {"
    "   background-image: url(img/connection.png);"
    "   border-radius: 10px;"
    "}"
    "QPushButton:pressed {"
    "   background-color: rgba(0, 0, 0, 0.3);"
    "}"
)

        self.pet_button = QPushButton(self)
        self.pet_button.setGeometry(550, 540, 75, 75)
        self.pet_button.setStyleSheet(
    "QPushButton {"
    "   background-image: url(img/pet.png);"
    "   border-radius: 10px;"
    "}"
    "QPushButton:pressed {"
    "   background-color: rgba(0, 0, 0, 0.3);"
    "}"
)

        self.present_button = QPushButton(self)
        self.present_button.setGeometry(550, 420, 75, 75)
        self.present_button.setStyleSheet(
    "QPushButton {"
    "   background-image: url(img/present.png);"
    "   border-radius: 10px;"
    "}"
    "QPushButton:pressed {"
    "   background-color: rgba(0, 0, 0, 0.3);"
    "}"
)

        self.clothes_button = QPushButton(self)
        self.clothes_button.setGeometry(550, 300, 75, 75)
        self.clothes_button.setStyleSheet(
    "QPushButton {"
    "   background-image: url(img/clothes.png);"
    "   border-radius: 10px;"
    "}"
    "QPushButton:pressed {"
    "   background-color: rgba(0, 0, 0, 0.3);"
    "}"
)

        self.taxi_button = QPushButton(self)
        self.taxi_button.setGeometry(550, 180, 75, 75)
        self.taxi_button.setStyleSheet(
    "QPushButton {"
    "   background-image: url(img/taxi.png);"
    "   border-radius: 10px;"
    "}"
    "QPushButton:pressed {"
    "   background-color: rgba(0, 0, 0, 0.3);"
    "}"
)

        self.fun_button = QPushButton(self)
        self.fun_button.setGeometry(550, 40, 77, 77)
        self.fun_button.setStyleSheet(
    "QPushButton {"
    "   background-image: url(img/fun.png);"
    "   border-radius: 10px;"
    "}"
    "QPushButton:pressed {"
    "   background-color: rgba(0, 0, 0, 0.3);"
    "}"
)

        self.transport_button = QPushButton(self)
        self.transport_button.setGeometry(390, 40, 75, 75)
        self.transport_button.setStyleSheet(
    "QPushButton {"
    "   background-image: url(img/transport.png);"
    "   border-radius: 10px;"
    "}"
    "QPushButton:pressed {"
    "   background-color: rgba(0, 0, 0, 0.3);"
    "}"
)

        self.car_button = QPushButton(self)
        self.car_button.setGeometry(220, 40, 75, 75)
        self.car_button.setStyleSheet(
    "QPushButton {"
    "   background-image: url(img/car.png);"
    "   border-radius: 10px;"
    "}"
    "QPushButton:pressed {"
    "   background-color: rgba(0, 0, 0, 0.3);"
    "}"
)

        self.circle_color = QColor("#FFEBD8")
        self.outer_color = QColor("#aaa8ab")

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        painter.setBrush(QBrush(self.outer_color))
        painter.setPen(Qt.NoPen)
        painter.drawEllipse(210, 173, 300, 300)

        painter.setBrush(QBrush(self.circle_color))
        painter.setPen(Qt.NoPen)
        inner_circle_radius = 100
        inner_circle_x = 360
        inner_circle_y = 323
        painter.drawEllipse(inner_circle_x - inner_circle_radius, inner_circle_y - inner_circle_radius,
                             inner_circle_radius * 2, inner_circle_radius * 2)
