import sys

from PyQt6.QtWidgets import (
    QApplication,
    QLabel,
    QLineEdit,
    QWidget,
    QHBoxLayout,
    QVBoxLayout,
    QPushButton,
)
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import Qt


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 280, 80)
        self.setWindowTitle("Calculator App")
        self.setWindowIcon(QIcon('kteam.jpg'))

        vbox = QVBoxLayout()
 
        label1 = QLabel("<h1>Calculator!</h1>")

        vbox.addWidget(label1)

        hbox1 = QHBoxLayout()

        self.number1_line_edit = QLineEdit()

        label2 = QLabel("+")

        self.number2_line_edit = QLineEdit()

        label3 = QLabel("=")

        self.total_line_edit = QLineEdit()
        self.total_line_edit.setReadOnly(True)


        hbox1.addWidget(self.number1_line_edit)
        hbox1.addWidget(label2)
        hbox1.addWidget(self.number2_line_edit)
        hbox1.addWidget(label3)
        hbox1.addWidget(self.total_line_edit)

        vbox.addLayout(hbox1)
        
        button = QPushButton("Submit")
        button.clicked.connect(self.handle_click)
        vbox.addWidget(button)

        label4 = QLabel("@kteam")
        label4.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignBottom)

        vbox.addWidget(label4)

        self.setLayout(vbox)
        
    def handle_click(self):
        try:
            number1 = int(self.number1_line_edit.text())
            number2 = int(self.number2_line_edit.text())

            self.total_line_edit.setText(str(number1 + number2))
        except:
            pass

if __name__ == '__main__':
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())
