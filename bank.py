import sqlite3
conn = sqlite3.connect('cash.db')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS expenses (
        User_id INTEGER PRIMARY KEY AUTOINCREMENT,
        Type TEXT,
        Quantity REAL,
        Time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS balance (
        User_id INTEGER PRIMARY KEY AUTOINCREMENT,
        Amount REAL,
        Time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
''')
conn.commit()
conn.close()


from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QDialog, QLineEdit, QHBoxLayout
from PySide6.QtGui import QPainter, QColor, QBrush, QPen, QPixmap
from PySide6.QtCore import Qt, Signal, QDateTime
from balance import *
from buttons import cafe, car, clothes, connection, food, fun, health, hygiene, pet, present, property, sport, taxi, transport
 
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

        self.conn = sqlite3.connect('cash.db')
        self.cursor = self.conn.cursor()

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
        self.add_balance.clicked.connect(self.open_balance_dialog)

        self.remove_balance = QPushButton(f'-', self)
        self.remove_balance.setStyleSheet("color: black; font-size: 12pt;")
        self.remove_balance.setGeometry(260, 650, 50, 50)
        self.remove_balance.resize(30, 30)
        self.remove_balance.clicked.connect(self.open_remove_balance_dialog)

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
        self.food_button.clicked.connect(self.open_food_dialog)

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
        self.property_button.clicked.connect(self.open_property_dialog)

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
        self.cafe_button.clicked.connect(self.open_cafe_dialog)

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
        self.hygiene_button.clicked.connect(self.open_hygiene_dialog)

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
        self.sport_button.clicked.connect(self.open_sport_dialog)

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
        self.health_button.clicked.connect(self.open_health_dialog)

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
        self.connection_button.clicked.connect(self.open_connection_dialog)

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
        self.pet_button.clicked.connect(self.open_pet_dialog)

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
        self.present_button.clicked.connect(self.open_present_dialog)

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
        self.clothes_button.clicked.connect(self.open_clothes_dialog)

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
        self.taxi_button.clicked.connect(self.open_taxi_dialog)

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
        self.fun_button.clicked.connect(self.open_fun_dialog)

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
        self.transport_button.clicked.connect(self.open_transport_dialog)

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
        self.car_button.clicked.connect(self.open_car_dialog)

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

    def open_balance_dialog(self):
        dialog = AddBalanceDialog(self)
        dialog.balance_added.connect(self.update_balance)
        dialog.exec()

    def open_remove_balance_dialog(self):
        dialog = RemoveBalanceDialog(self)
        dialog.balance_removed.connect(self.less_balance)
        dialog.exec()

    def open_property_dialog(self):
        dialog = property.AddPropertyDialog(self)
        dialog.property_added.connect(self.update_property)
        dialog.exec()

    def open_sport_dialog(self):
        dialog = sport.AddSportDialog(self)
        dialog.sport_added.connect(self.update_sport)
        dialog.exec()

    def open_cafe_dialog(self):
        dialog = cafe.AddCafeDialog(self)
        dialog.cafe_added.connect(self.update_cafe)
        dialog.exec()

    def open_car_dialog(self):
        dialog = car.AddCarDialog(self)
        dialog.car_added.connect(self.update_car)
        dialog.exec()

    def open_clothes_dialog(self):
        dialog = clothes.AddClothesDialog(self)
        dialog.clothes_added.connect(self.update_clothes)
        dialog.exec()

    def open_connection_dialog(self):
        dialog = connection.AddConnectionDialog(self)
        dialog.connection_added.connect(self.update_connection)
        dialog.exec()

    def open_food_dialog(self):
        dialog = food.AddFoodDialog(self)
        dialog.food_added.connect(self.update_food)
        dialog.exec()

    def open_fun_dialog(self):
        dialog = fun.AddFunDialog(self)
        dialog.fun_added.connect(self.update_fun)
        dialog.exec()

    def open_health_dialog(self):
        dialog = health.AddHealthDialog(self)
        dialog.health_added.connect(self.update_health)
        dialog.exec()

    def open_hygiene_dialog(self):
        dialog = hygiene.AddHygieneDialog(self)
        dialog.hygiene_added.connect(self.update_hygiene)
        dialog.exec()

    def open_pet_dialog(self):
        dialog = pet.AddPetDialog(self)
        dialog.pet_added.connect(self.update_pet)
        dialog.exec()

    def open_present_dialog(self):
        dialog = present.AddPresentDialog(self)
        dialog.present_added.connect(self.update_present)
        dialog.exec()

    def open_taxi_dialog(self):
        dialog = taxi.AddTaxiDialog(self)
        dialog.taxi_added.connect(self.update_taxi)
        dialog.exec()

    def open_transport_dialog(self):
        dialog = transport.AddTransportDialog(self)
        dialog.transport_added.connect(self.update_transport)
        dialog.exec()

    def update_cafe(self, cafe_name):
        print(f"Cafe added: {cafe_name}")
        self.outer_color = QColor("#006400")
        self.update()

    def update_balance(self, amount):
        try:
            self.cursor.execute('SELECT User_id FROM balance WHERE User_id = ?', (self.user_id,))
            existing_user = self.cursor.fetchone()

            if existing_user:
                self.cursor.execute('UPDATE balance SET Amount = Amount + ? WHERE User_id = ?', (amount, self.user_id))
            else:
                self.cursor.execute('INSERT INTO balance (User_id, Amount) VALUES (?, ?)', (self.user_id, amount))

            self.conn.commit()
        except Exception as e:
            print(f"Error updating balance in the database: {e}")

            
    def less_balance(self, user_id, amount):
        try:
            conn = sqlite3.connect('cash.db')
            cursor = conn.cursor()

            cursor.execute('SELECT User_id FROM balance WHERE User_id = ?', (user_id,))
            existing_user = cursor.fetchone()

            if existing_user:
                cursor.execute('UPDATE balance SET Amount = Amount - ? WHERE User_id = ?', (amount, user_id))
            else:
                print("Пользователь не найден в базе данных!")

            conn.commit()
            conn.close()
        except Exception as e:
            print(f"Error updating balance in the database: {e}")

    def update_food(self, value):
        self.outer_color = QColor("#f58cb5")
        self.update()
        print(f"Food added with value: {value}")

    def update_property(self, value):
        self.outer_color = QColor("#b7e0d3")
        self.update()
        print(f"Property added with value: {value}")

    def update_cafe(self, value):
        self.outer_color = QColor("#a2d5b2")
        self.update()
        print(f"Cafe added with value: {value}")

    def update_hygiene(self, value):
        self.outer_color = QColor("#50606b")
        self.update()
        print(f"Hygiene added with value: {value}")
    
    def update_sport(self, value):
        self.outer_color = QColor("#ffbfd9")
        self.update()
        print(f"Sport added with value: {value}")

    def update_health(self, value):
        self.outer_color = QColor("#ec504f")
        self.update()
        print(f"Health added with value: {value}")

    def update_connection(self, value):
        self.outer_color = QColor("#b3a6b9")
        self.update()
        print(f"Connection added with value: {value}")

    def update_pet(self, value):
        self.outer_color = QColor("#77d2a0")
        self.update()
        print(f"Pet added with value: {value}")

    def update_present(self, value):
        self.outer_color = QColor("#d6c0c7")
        self.update()
        print(f"Present added with value: {value}")

    def update_clothes(self, value):
        self.outer_color = QColor("#bfa0cc")
        self.update()
        print(f"Clothes added with value: {value}")

    def update_taxi(self, value):
        self.outer_color = QColor("#df9e18")
        self.update()
        print(f"Taxi added with value: {value}")
    
    def update_fun(self, value):
        self.outer_color = QColor("#edcf9c")
        self.update()
        print(f"Fun added with value: {value}")

    def update_transport(self, value):
        self.outer_color = QColor("#f68583")
        self.update()
        print(f"Transport added with value: {value}")

    def update_car(self, value):
        self.outer_color = QColor("#7c869d")
        self.update()
        print(f"Car added with value: {value}")

if __name__ == "__main__":
    app = QApplication([])
    circle_widget = CircleWidget()
    circle_widget.show()
    app.exec()