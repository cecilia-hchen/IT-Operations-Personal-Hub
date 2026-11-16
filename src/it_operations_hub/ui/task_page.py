
from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QTableWidget,
    QTableWidgetItem,
    QMessageBox,
    QHeaderView,
)

from it_operations_hub.services.task_service import (
    create_task,
    get_all_tasks,
    update_task_status,
    delete_task,
)


class TaskPage(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)

        title = QLabel("Task Manager")
        title.setStyleSheet(
            "font-size: 24px; font-weight: bold;"
        )
        layout.addWidget(title)

        # Task creation form
        form = QHBoxLayout()

        self.title_input = QLineEdit()
        self.title_input.setPlaceholderText("Enter task title")

        add_button = QPushButton("Add Task")
        add_button.clicked.connect(self.add_task)

        form.addWidget(self.title_input)
        form.addWidget(add_button)
        layout.addLayout(form)

        # Task table
        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(
            ["ID", "Title", "Priority", "Status"]
        )
        self.table.horizontalHeader().setSectionResizeMode(
            QHeaderView.ResizeMode.Stretch
        )
        self.table.setSelectionBehavior(
            QTableWidget.SelectionBehavior.SelectRows
        )
        self.table.setEditTriggers(
            QTableWidget.EditTrigger.NoEditTriggers
        )

        layout.addWidget(self.table)

        # Action buttons
        actions = QHBoxLayout()

        complete_button = QPushButton("Mark Completed")
        complete_button.clicked.connect(self.complete_task)

        delete_button = QPushButton("Delete Task")
        delete_button.clicked.connect(self.remove_task)

        actions.addWidget(complete_button)
        actions.addWidget(delete_button)
        layout.addLayout(actions)

        self.load_tasks()

    def load_tasks(self):
        tasks = get_all_tasks()
        self.table.setRowCount(len(tasks))

        for row, task in enumerate(tasks):
            values = [
                task["id"],
                task["title"],
                task["priority"],
                task["status"],
            ]

            for column, value in enumerate(values):
                self.table.setItem(
                    row,
                    column,
                    QTableWidgetItem(str(value)),
                )

    def add_task(self):
        title = self.title_input.text().strip()

        if not title:
            QMessageBox.warning(
                self, "Validation", "Please enter a task title."
            )
            return

        create_task(title)
        self.title_input.clear()
        self.load_tasks()

    def get_selected_task_id(self):
        row = self.table.currentRow()

        if row < 0:
            QMessageBox.warning(
                self, "Selection", "Please select a task."
            )
            return None

        item = self.table.item(row, 0)
        return int(item.text())

    def complete_task(self):
        task_id = self.get_selected_task_id()

        if task_id is None:
            return

        update_task_status(task_id, "Completed")
        self.load_tasks()

    def remove_task(self):
        task_id = self.get_selected_task_id()

        if task_id is None:
            return

        answer = QMessageBox.question(
            self,
            "Confirm Delete",
            "Are you sure you want to delete this task?",
            QMessageBox.StandardButton.Yes
            | QMessageBox.StandardButton.No,
        )

        if answer == QMessageBox.StandardButton.Yes:
            delete_task(task_id)
            self.load_tasks()
