import sys

from PySide6.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QVBoxLayout,
    QWidget,
)

from it_operations_hub.ui.task_page import TaskPage

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set application window title
        self.setWindowTitle("IT Operations Personal Hub")

        # Set initial window size
        self.resize(1100, 700)

        # Display the Task Manager page
        self.setCentralWidget(TaskPage())


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()