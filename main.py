import sys
from PySide2.QtWidgets import QApplication
from gui import MainWindow

if __name__ == '__main__':
    app = QApplication()
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())