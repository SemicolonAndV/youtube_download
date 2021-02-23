import sys
from PySide2.QtWidgets import (QLineEdit, QPushButton, QApplication,
    QVBoxLayout, QDialog, QMessageBox)
from dl_script import download_mp3

class MainWindow(QDialog):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        
        self.link_field = QLineEdit()
        self.link_field.setPlaceholderText("Enter YouTube link here...")
        self.download_button = QPushButton("Download MP3")
        
        layout = QVBoxLayout()
        layout.addWidget(self.link_field)
        layout.addWidget(self.download_button)
        self.setLayout(layout)
        self.download_button.clicked.connect(self.dl_check)

    def dl_check(self):
        status = download_mp3(self.link_field.text())
        info_msg = QMessageBox()
        info_msg.setWindowTitle("Download status")
        info_msg.setStandardButtons(QMessageBox.Ok)
        if status:
            info_msg.setIcon(QMessageBox.Information)
            info_msg.setText("Download successful")
        else:
            info_msg.setIcon(QMessageBox.Warning)
            info_msg.setText("Invalid URL")
        info_msg.exec_()


