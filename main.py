from PySide6.QtWidgets import QApplication
from ui import CircleWidget
import logger
import sys

def main():
    app = QApplication(sys.argv)
    window = CircleWidget()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()