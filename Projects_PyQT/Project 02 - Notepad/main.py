import sys

from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QLabel,
    QVBoxLayout,
    QFileDialog,
    QTextEdit,
)
from PyQt6.QtGui import QAction, QIcon, QTextCursor
from PyQt6.QtCore import Qt


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 480, 350)
        self.setWindowTitle("Kteam App")
        self.setWindowIcon(QIcon('kteam.jpg'))

        menu_bar = self.menuBar()

        file_menu = menu_bar.addMenu('File')

        new_action = QAction('New', self)
        open_action = QAction("Open", self)
        save_action = QAction('Save', self)
        exit_action = QAction('Exit', self)

        file_menu.addAction(new_action)
        file_menu.addAction(open_action)
        file_menu.addAction(save_action)
        file_menu.addSeparator()
        file_menu.addAction(exit_action)

        new_action.triggered.connect(self.new_document)
        open_action.triggered.connect(self.open_file)
        save_action.triggered.connect(self.save_file)
        exit_action.triggered.connect(self.exit_app)

        central_widget = QWidget(self)
        vbox = QVBoxLayout(central_widget)

        self.text_edit = QTextEdit(self)
        self.text_edit.setPlainText("Dòng chữ mặc định")
        cursor = self.text_edit.textCursor()
        cursor.movePosition(QTextCursor.MoveOperation.End)
        self.text_edit.setTextCursor(cursor)

        label = QLabel('@kteam', self)
        label.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignBottom)

        vbox.addWidget(self.text_edit)
        vbox.addWidget(label)

        self.setCentralWidget(central_widget)

        self.file_path = None

    def new_document(self):
        self.text_edit.setPlainText("")
        self.file_path = None

    def open_file(self):
        file_dialog = QFileDialog(self)
        file_path, _ = file_dialog.getOpenFileName()

        if file_path:
            with open(file_path, 'r') as file:
                content = file.read()
                self.text_edit.setPlainText(content)

                self.file_path = file_path

    def save_file(self):
        if self.file_path:
            with open(self.file_path, 'w') as file:
                content = self.text_edit.toPlainText()
                file.write(content)
        else:
            file_dialog = QFileDialog(self)
            file_path, _ = file_dialog.getSaveFileName()

            if file_path:
                with open(file_path, 'w') as file:
                    content = self.text_edit.toPlainText()
                    file.write(content)

    def exit_app(self):
        QApplication.quit()

app = QApplication([])
window = Window()
window.show()
sys.exit(app.exec())
