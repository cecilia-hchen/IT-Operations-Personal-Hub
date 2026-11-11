import sys

from PySide6.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QVBoxLayout,
    QWidget,
)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("IT Operations Personal Hub")
        self.resize(1100, 700)

        central_widget = QWidget()
        layout = QVBoxLayout(central_widget)

        title = QLabel("Welcome to the IT Operations Hub!")
        title.setStyleSheet("font-size: 28px; font-weight: bold;")

        subtitle = QLabel("Your personal IT Operations workspace.")

        layout.addWidget(title)
        layout.addWidget(subtitle)
        layout.addStretch()

        self.setCentralWidget(central_widget)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()