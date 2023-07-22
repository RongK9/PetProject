import sys

from PyQt6.QtWidgets import (
    QApplication,
    QLabel,
    QLineEdit,
    QWidget,
    QFormLayout,
    QVBoxLayout,
    QPushButton,
    QMessageBox,
)
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import Qt


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Main Window")
        self.setGeometry(100, 100, 280, 300)
        self.setWindowIcon(QIcon('kteam.jpg'))

        # Create widgets for the main window (add your content here)
        layout = QVBoxLayout()
        
        label1 = QLabel("Welcome to the Main Window!")
        label1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        button = QPushButton("Logout")
        button.clicked.connect(self.logout)

        label2 = QLabel("@kteam")
        label2.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignBottom)
        
        layout.addWidget(label1)
        layout.addWidget(button)
        layout.addWidget(label2)

        self.setLayout(layout)

    def logout(self):
        self.login_form = LoginForm()
        self.login_form.show()

        self.close()


class LoginForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 280, 80)
        self.setWindowTitle("Login")
        self.setWindowIcon(QIcon('kteam.jpg'))

        username_label = QLabel("Username:")
        self.username_input = QLineEdit()
        self.username_input.returnPressed.connect(self.login)
        
        password_label = QLabel("Password:")
        self.password_input = QLineEdit()
        self.password_input.returnPressed.connect(self.login)
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)

        login_button = QPushButton("Login")
        login_button.clicked.connect(self.login)
        
        kteam_label = QLabel("@Kteam")
        kteam_label.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignBottom)

        form_layout = QFormLayout()
        form_layout.addRow(username_label, self.username_input)
        form_layout.addRow(password_label, self.password_input)
        form_layout.addWidget(login_button)
        form_layout.addWidget(kteam_label)

        self.setLayout(form_layout)

    def login(self):
        username = self.username_input.text()
        password = self.password_input.text()
        
        if username == "admin" and password == "1234":
            self.main_window = MainWindow()
            self.main_window.show()
            self.close()
        else:
            QMessageBox.critical(self, "Login Failed", "Invalid username or password. Please try again.")

if __name__ == '__main__':
    app = QApplication([])
    window = LoginForm()
    window.show()
    sys.exit(app.exec())