from PySide6.QtWidgets import QApplication
from ui import CircleWidget
 


if __name__ == "__main__":
    app = QApplication([])
    circle_widget = CircleWidget()
    circle_widget.show()
    app.exec()