import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QGridLayout, QPushButton, QLineEdit
from PyQt6.QtCore import Qt


class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ماشین حساب")

        # Layout setup
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        # Display setup
        self.display = QLineEdit()
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.display.setFixedHeight(50)
        self.layout.addWidget(self.display)

        # Button layout
        self.buttonsLayout = QGridLayout()
        self.layout.addLayout(self.buttonsLayout)

        # Buttons
        buttons = [
            ('7', 0, 0), ('8', 0, 1), ('9', 0, 2), ('/', 0, 3),
            ('4', 1, 0), ('5', 1, 1), ('6', 1, 2), ('*', 1, 3),
            ('1', 2, 0), ('2', 2, 1), ('3', 2, 2), ('-', 2, 3),
            ('0', 3, 0), ('.', 3, 1), ('+', 3, 2), ('=', 3, 3),
        ]

        for text, row, col in buttons:
            button = QPushButton(text)
            button.setFixedSize(50, 50)
            self.buttonsLayout.addWidget(button, row, col)
            button.clicked.connect(self.on_button_click)

        self.clear_button = QPushButton('C')
        self.clear_button.setFixedSize(50, 50)
        self.clear_button.setObjectName('clear_button')  # برای متمایز کردن دکمه پاک کردن
        self.buttonsLayout.addWidget(self.clear_button, 4, 0, 1, 4)
        self.clear_button.clicked.connect(self.clear_display)

        # Load QSS styles
        self.load_styles()

    def load_styles(self):
        with open("style.qss", "r") as file:
            self.setStyleSheet(file.read())



    def on_button_click(self):
        button = self.sender()
        text = button.text()

        if text == "=":
            try:
                expression = self.display.text()
                result = str(eval(expression))
                self.display.setText(result)
            except Exception as e:
                self.display.setText("Error")
        else:
            current_text = self.display.text()
            new_text = current_text + text
            self.display.setText(new_text)

    def clear_display(self):
        self.display.clear()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Calculator()
    window.show()
    sys.exit(app.exec())
