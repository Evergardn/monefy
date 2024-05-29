import sys
import math
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QDialog, QLineEdit, QHBoxLayout, QInputDialog, QColorDialog
from PySide6.QtGui import QPainter, QColor, QBrush, QPixmap, QFont
from PySide6.QtCore import Qt, Signal, Slot
from dialogs import *
from services.get_balance_from_db import get_balance
from buttons.food import AddFoodDialog
from buttons.property import AddPropertyDialog
from buttons.cafe import AddCafeDialog
from buttons.hygiene import AddHygieneDialog
from buttons.sport import AddSportDialog
from buttons.health import AddHealthDialog
from buttons.connection import AddConnectionDialog
from buttons.pet import AddPetDialog
from buttons.present import AddPresentDialog
from buttons.clothes import AddClothesDialog
from buttons.taxi import AddTaxiDialog
from buttons.fun import AddFunDialog
from buttons.transport import AddTransportDialog
from buttons.car import AddCarDialog

def open_food_dialog(self):
    dialog = AddFoodDialog(self)
    return dialog

def open_property_dialog(self):
    dialog = AddPropertyDialog(self)
    return dialog

def open_cafe_dialog(self):
    dialog = AddCafeDialog(self)
    return dialog

def open_hygiene_dialog(self):
    dialog = AddHygieneDialog(self)
    return dialog

def open_sport_dialog(self):
    dialog = AddSportDialog(self)
    return dialog

def open_health_dialog(self):
    dialog = AddHealthDialog(self)
    return dialog

def open_connection_dialog(self):
    dialog = AddConnectionDialog(self)
    return dialog

def open_pet_dialog(self):
    dialog = AddPetDialog(self)
    return dialog

def open_present_dialog(self):
    dialog = AddPresentDialog(self)
    return dialog

def open_clothes_dialog(self):
    dialog = AddClothesDialog(self)
    return dialog

def open_taxi_dialog(self):
    dialog = AddTaxiDialog(self)
    return dialog

def open_fun_dialog(self):
    dialog = AddFunDialog(self)
    return dialog

def open_transport_dialog(self):
    dialog = AddTransportDialog(self)
    return dialog

def open_car_dialog(self):
    dialog = AddCarDialog(self)
    return dialog