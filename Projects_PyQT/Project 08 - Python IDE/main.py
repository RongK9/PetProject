import sys
import subprocess

from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QLabel,
    QVBoxLayout,
    QFileDialog,
    QTextEdit,
    QStyle,
)
from PyQt6.QtGui import (
    QAction,
    QIcon,
)
from PyQt6.Qsci import QsciScintilla, QsciLexerPython
from PyQt6.QtCore import Qt, QSize


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 480, 350)
        self.setWindowTitle("Python IDE App")
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

        code_tool_bar = self.addToolBar("Code")
        code_tool_bar.setIconSize(QSize(20, 20))

        run_action = QAction("Run", self)
        run_action.setIcon(app.style().standardIcon(QStyle.StandardPixmap.SP_MediaPlay))

        code_tool_bar.addAction(run_action)

        run_action.triggered.connect(self.run_code)

        central_widget = QWidget(self)
        vbox = QVBoxLayout(central_widget)

        self.text_edit = QsciScintilla()
        self.text_edit.setMarginType(0, QsciScintilla.MarginType.NumberMargin)
        self.text_edit.setMarginLineNumbers(0, True)
        self.text_edit.setFolding(QsciScintilla.FoldStyle.PlainFoldStyle)
        self.text_edit.setAutoIndent(True)
        self.text_edit.setBraceMatching(QsciScintilla.BraceMatch.SloppyBraceMatch)
        self.text_edit.setCaretLineVisible(True)
        self.text_edit.setCaretLineBackgroundColor(Qt.GlobalColor.lightGray)
        self.text_edit.setLexer(QsciLexerPython(self.text_edit))

        self.output = QTextEdit()
        self.output.setReadOnly(True)
        self.output.setFixedHeight(120)

        label = QLabel('@kteam', self)
        label.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignBottom)

        vbox.addWidget(self.text_edit)
        vbox.addWidget(self.output)
        vbox.addWidget(label)

        self.setCentralWidget(central_widget)

        self.file_path = None

    def new_document(self):
        self.text_edit.setText("")
        self.file_path = None

    def open_file(self):
        file_dialog = QFileDialog(self)
        file_path, _ = file_dialog.getOpenFileName()

        if file_path:
            with open(file_path, 'r') as file:
                content = file.read()
                self.text_edit.setText(content)

                self.file_path = file_path

    def save_file(self):
        if self.file_path:
            with open(self.file_path, 'w') as file:
                content = self.text_edit.text()
                file.write(content)
        else:
            file_dialog = QFileDialog(self)
            file_path, _ = file_dialog.getSaveFileName()

            if file_path:
                with open(file_path, 'w') as file:
                    content = self.text_edit.text()
                    file.write(content)
    def run_code(self):
        code = self.text_edit.text()
        result = subprocess.run(["python", "-c", code], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        output = result.stdout + result.stderr
        self.output.setPlainText(output)

    def exit_app(self):
        QApplication.quit()

if __name__ == '__main__':
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())