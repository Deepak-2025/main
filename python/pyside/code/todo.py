import sys
import json
from PySide6.QtCore import Qt, QPropertyAnimation, QPoint, QEasingCurve, QDateTime
from PySide6.QtWidgets import QApplication, QWidget, QMainWindow, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QListWidget, QInputDialog, QLabel, QFrame, QScrollArea,QMessageBox
from PySide6.QtGui import QColor, QFont

class ToDoApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("To Do List ")
        self.setGeometry(100, 100, 350, 550)
        self.setStyleSheet(self.get_stylesheet())

        # Central widget container
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)

        # Header - Current Date
        self.header_widget = QWidget(self)
        self.date_label = QLabel(self)
        self.update_date()
        self.header_layout = QVBoxLayout(self.header_widget)
        self.header_layout.addWidget(self.date_label)
        self.header_widget.setStyleSheet("border-radius:12px;background-color: #0093E9;background-image: linear-gradient(160deg, #0093E9 0%, #80D0C7 100%);")
        self.header_widget.setFixedHeight(60)
        main_layout.addWidget(self.header_widget)

        # Task List
        self.task_list_widget = QWidget(self)
        self.todo_list = QListWidget(self)
        self.todo_list.setStyleSheet("font-size:25px;color:black;background-color:#d3e9f3; border-radius: 15px; padding: 10px;margin:5px;")
        self.scroll_area = QScrollArea(self)
        self.scroll_area.setWidget(self.todo_list)
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setStyleSheet("background-color: transparent; border: none;")
        self.task_list_layout = QVBoxLayout(self.task_list_widget)
        self.task_list_layout.addWidget(self.scroll_area)
        main_layout.addWidget(self.task_list_widget)

        self.btn_widget = QWidget(self)
        self.input_field = QLineEdit(self)
        self.input_field.setPlaceholderText("Enter your task here")
        self.input_field.setStyleSheet("font-style:italic;background-color:#d3e9f3; border-radius: 15px; padding: 10px; font-size: 18px;")
        self.btn_layout = QVBoxLayout(self.btn_widget)
        self.btn_layout.addWidget(self.input_field)
        main_layout.addWidget(self.btn_widget)

        # Input and Control Buttons
        self.control_widget = QWidget(self)
        self.add_button = QPushButton("Add Task", self)
        self.add_button.setStyleSheet(self.button_stylesheet())
        self.add_button.clicked.connect(self.add_task)
        self.update_button = QPushButton("Update Task", self)
        self.update_button.setStyleSheet(self.button_stylesheet())
        self.update_button.clicked.connect(self.update_task)
        self.delete_button = QPushButton("Delete Task", self)
        self.delete_button.setStyleSheet(self.button_stylesheet())
        self.delete_button.clicked.connect(self.delete_task)
        self.save_button = QPushButton("Save Tasks", self)
        self.save_button.setStyleSheet(self.button_stylesheet())
        self.save_button.clicked.connect(self.save_tasks)

        self.control_layout = QHBoxLayout(self.control_widget)
        self.control_layout.addWidget(self.add_button)
        self.control_layout.addWidget(self.update_button)
        self.control_layout.addWidget(self.delete_button)
        self.control_layout.addWidget(self.save_button)
        main_layout.addWidget(self.control_widget)

        # Load tasks from file
        self.load_tasks()

    def add_task(self):
        task = self.input_field.text().strip()
        if task:
            self.todo_list.addItem("•  " + task)
            self.input_field.clear()

    def update_task(self):
        selected_item = self.todo_list.currentItem()
        if selected_item:
            new_task, ok = QInputDialog.getText(self, "Update Task", "Edit task:", text=selected_item.text())
            if ok and new_task.strip():
                selected_item.setText(new_task.strip())
                

    def delete_task(self):
        selected_item = self.todo_list.currentItem()
        if selected_item:
            self.todo_list.takeItem(self.todo_list.row(selected_item))
            

    def save_tasks(self):
        tasks = [self.todo_list.item(i).text() for i in range(self.todo_list.count())]
        with open("tasks.json", "w") as file:
            json.dump(tasks, file)
        self.show_message("Success", "Tasks saved successfully!")

    def load_tasks(self):
        try:
            with open("tasks.json", "r") as file:
                tasks = json.load(file)
                for task in tasks:
                    self.todo_list.addItem(task)
        except FileNotFoundError:
            pass  # No saved tasks to load.

    def update_date(self):
        self.current_date = QDateTime.currentDateTime().toString("dddd, MMMM dd, yyyy")
        self.date_label.setText(self.current_date)
        #print(self.current_date)
        self.date_label.setAlignment(Qt.AlignCenter)
        self.date_label.setStyleSheet("color: black; font-size: 20px; font-weight: bold;")


    def show_message(self, title, message):
        msg = QMessageBox(self)
        msg.setIcon(QMessageBox.Information)
        msg.setText(message)
        msg.setWindowTitle(title)
        msg.exec()

    def button_stylesheet(self):
        return """
        QPushButton {
            background-color: #004e92;
            color: white;
            padding: 10px;
            border-radius: 5px;
            font-size: 16px;
            border: none;
            margin: 0 5px;
        }
        QPushButton:hover {
            background-color: #2d4a53;
            color:#c1e8ff;
        }
        QPushButton:focus {
            outline: none;
        }
        """

    def get_stylesheet(self):
        return """
        QWidget {
            color:black;
            
            font-family: Arial, sans-serif;
            background-color: #8BC6EC;
            background-image: linear-gradient(135deg, #8BC6EC 0%, #9599E2 100%);

        }
        QLineEdit {
            background-color: white;
            border-radius: 5px;
            padding: 10px;
            font-size: 16px;
        }
        QListWidget {
            border-radius: 10px;
            font-size: 18px;
            margin-bottom: 10px;
            padding: 10px;
            selection-background-color: #3498db;
            selection-color: black;
        }
        QScrollArea {
            border: none;
        }
        """
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ToDoApp()
    window.show()
    sys.exit(app.exec())
