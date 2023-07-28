import sys
from PyQt6.QtWidgets import (
    QApplication,
    QLabel,
    QWidget,
    QMainWindow,
    QHBoxLayout,
    QVBoxLayout,
    QPushButton,
    QFileDialog,
)
from PyQt6.QtGui import QAction, QPainter, QPen, QImage, QColor, QIcon, QPixmap
from PyQt6.QtCore import Qt, QSize


COLORS = [
    '#000000', '#141923', '#414168', '#3a7fa7', '#35e3e3', '#8fd970', '#5ebb49',
    '#458352', '#dcd37b', '#fffee5', '#ffd035', '#cc9245', '#a15c3e', '#a42f3b',
    '#f45b7a', '#c24998', '#81588d', '#bcb0c2', '#ffffff',
]


class QPaletteButton(QPushButton):

    def __init__(self, color):
        super().__init__()
        self.setFixedSize(QSize(24,24))
        self.color = color
        self.setStyleSheet("background-color: %s;" % color)
    

class Window(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Painter App")
        self.setWindowIcon(QIcon('kteam.jpg'))
        self.create_menu_bar()

        self.label = QLabel(self)
        self.canvas = QPixmap(400, 300)
        self.canvas.fill(Qt.GlobalColor.white)
        self.label.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)
        self.label.setPixmap(self.canvas)

        widget = QWidget()
        vbox = QVBoxLayout()

        palette = QHBoxLayout()
        for c in COLORS:
            b = QPaletteButton(c)
            b.pressed.connect(lambda c=c: self.set_pen_color(c))
            palette.addWidget(b)

        kteam_label = QLabel('@kteam', self)
        kteam_label.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignBottom)
        
        vbox.addWidget(self.label)
        vbox.addStretch()
        vbox.addLayout(palette)
        vbox.addWidget(kteam_label)

        widget.setLayout(vbox)
        self.setCentralWidget(widget)

        self.last_x, self.last_y = None, None
        self.file_path = None
        self.pen_color = QColor('#000000')

    def set_pen_color(self, color):
        self.pen_color = QColor(color)

    def open_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, 'Open Image File', '', 'Images (*.png *.jpg *.bmp);;All Files (*)')

        if file_path:
            image = QImage(file_path)
            if image.isNull():
                return

            self.file_path = file_path
            self.label.setPixmap(QPixmap.fromImage(image).scaled(400, 200))

    def save_file(self):
        if self.file_path:
            pixmap = self.label.pixmap()
            pixmap.save(self.file_path)
        else:
            file_name, _ = QFileDialog.getSaveFileName(self, 'Save Image File', '', 'Images (*.png);;All Files (*)')

            if file_name:
                pixmap = self.label.pixmap()
                pixmap.save(file_name)

    def create_menu_bar(self):
        self.menu_bar = self.menuBar()
        self.menu_bar.setNativeMenuBar(False)

        file_menu = self.menu_bar.addMenu('File')

        open_action = QAction('Open', self)
        open_action.triggered.connect(self.open_file)
        file_menu.addAction(open_action)

        save_action = QAction('Save', self)
        save_action.triggered.connect(self.save_file)
        file_menu.addAction(save_action)

    def mouseMoveEvent(self, e):
        if self.last_x is None: # First event.
            self.last_x = e.position().x()
            self.last_y = e.position().y()
            return # Ignore the first time.

        canvas = self.label.pixmap()
        painter = QPainter(canvas)
        painter.setPen(QPen(self.pen_color, 2, Qt.PenStyle.SolidLine, Qt.PenCapStyle.RoundCap, Qt.PenJoinStyle.RoundJoin))


        painter.drawLine(
            int(self.last_x),
            int(self.last_y) - self.menu_bar.height(),
            int(e.position().x()),
            int(e.position().y()) - self.menu_bar.height()
        )
        painter.end()
        self.label.setPixmap(canvas)

        # Update the origin for next time.
        self.last_x = e.position().x()
        self.last_y = e.position().y()

    def mouseReleaseEvent(self, e):
        self.last_x = None
        self.last_y = None


if __name__ == '__main__':
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())