import sys
from PySide6.QtCore import QDate, Qt
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QGridLayout, QLabel, QCheckBox, QGroupBox, QPushButton

class DateCheckboxWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Dates and Checkboxes")
        self.resize(550, 500)
        

        # Current date
        current_date = QDate.currentDate()

        # Create a QVBoxLayout for the main window
        main_layout = QVBoxLayout()

        # Create a QGroupBox to hold the grid layout
        group_box = QGroupBox("Select Dates")
        group_box.setStyleSheet("QGroupBox{background-color:#1d3c45;color:black;}")
        group_layout = QGridLayout()

        # Store checkboxes in a list for later access
        self.checkboxes = []

        # Loop through the next 30 days and create labels and checkboxes
        for i in range(30):
            next_day = current_date.addDays(i)

            # Create the label for the date
            date_label = QLabel(f"{next_day.toString('dd/MM/yyyy')}")
            date_label.setStyleSheet("QLabel{color:#a9c0a6;font-size:20px;font-weight:bold;}")

            # Create two checkboxes for each date
            checkbox1 = QCheckBox("✓")
          #  checkbox1.setStyleSheet("QCheckBox{background-color:gray;color:black;border:1px solid black;}")
            checkbox2 = QCheckBox("x")
            checkbox1.setStyleSheet("""
                QCheckBox {
                    font-size: 16px;
                    color: #a9c0a6;
                }
                QCheckBox::indicator {
                    width: 20px;
                    height: 20px;
                }
                QCheckBox::indicator:checked {
                    background-color: #4CAF50;
                    border: 2px solid white;
                    border-radius: 5px;
                }
                QCheckBox::indicator:unchecked {
                    background-color:#097770;
                    border: 2px solid #ccc;
                    border-radius: 5px;
                }
                QCheckBox::indicator:checked:hover {
                    background-color: #45a049;
                }
                QCheckBox::indicator:unchecked:hover {
                    background-color:#45a049;
                }
            """)
            checkbox2.setStyleSheet("""
                QCheckBox {
                    font-size: 16px;
                    color: #a9c0a6;
                }
                QCheckBox::indicator {
                    width: 20px;
                    height: 20px;
                }
                QCheckBox::indicator:checked {
                    background-color: #4CAF50;
                    border: 2px solid white;
                    border-radius: 5px;
                }
                QCheckBox::indicator:unchecked {
                    background-color:#097770;
                    border: 2px solid #ccc;
                    border-radius: 5px;
                }
                QCheckBox::indicator:checked:hover {
                    background-color: #45a049;
                }
                QCheckBox::indicator:unchecked:hover {
                    background-color: #45a049;
                }
            """)

            # Store checkboxes in the list to access them later
            self.checkboxes.append((date_label, checkbox1, checkbox2))

            # Determine the column (0, 1, 2) for the date and checkboxes
            col = i // 10  # This will determine the column (0, 1, or 2)
            row = i % 10  # This will determine the row (0 to 9)

            # Add the date label and checkboxes to the grid layout
            group_layout.addWidget(date_label, row, col * 3)  # Date label in first column of each group
            group_layout.addWidget(checkbox1, row, col * 3 + 1)  # Checkbox 1 in second column
            group_layout.addWidget(checkbox2, row, col * 3 + 2)  # Checkbox 2 in third column

        # Set the group layout in the group box
        group_box.setLayout(group_layout)

        # Add the group box to the main layout
        main_layout.addWidget(group_box)

        # Create the save button
        self.save_button = QPushButton("Save Checkbox States")
        self.save_button.clicked.connect(self.save_checkbox_state)

        # Add the save button to the main layout
        main_layout.addWidget(self.save_button)

        # Set the main layout of the window
        self.setLayout(main_layout)

        # Load checkbox states from the file
        self.load_checkbox_state()

    def save_checkbox_state(self):
        # Open a file to save the checkbox states
        with open("checkbox_states.txt", "w") as file:
            # Iterate over the stored checkboxes
            for date_label, checkbox1, checkbox2 in self.checkboxes:
                # Write the date and the states of the checkboxes
                file.write(f"{date_label.text()}: Checkbox 1: {'Checked' if checkbox1.isChecked() else 'Unchecked'}, "
                           f"Checkbox 2: {'Checked' if checkbox2.isChecked() else 'Unchecked'}\n")

        print("Checkbox states saved to file.")

    def load_checkbox_state(self):
        try:
            # Open the file to load checkbox states
            with open("checkbox_states.txt", "r") as file:
                # Iterate over each line in the file
                for line in file:
                    date, state = line.strip().split(": ", 1)
                    checkbox1_state, checkbox2_state = state.split(", ")

                    # Extract whether the checkboxes were checked or unchecked
                    checkbox1_state = checkbox1_state.split(": ")[1] == 'Checked'
                    checkbox2_state = checkbox2_state.split(": ")[1] == 'Checked'

                    # Find the matching date and set checkbox states
                    for date_label, checkbox1, checkbox2 in self.checkboxes:
                        if date_label.text() == date:
                            checkbox1.setChecked(checkbox1_state)
                            checkbox2.setChecked(checkbox2_state)

        except FileNotFoundError:
            print("No saved data found, starting fresh.")

# Run the application
app = QApplication(sys.argv)
window = DateCheckboxWindow()
window.show()
sys.exit(app.exec())
