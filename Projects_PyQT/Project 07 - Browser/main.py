import sys
from PyQt6.QtCore import QUrl
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QHBoxLayout,
    QVBoxLayout,
    QWidget,
    QLineEdit,
    QPushButton,
    QStyle,
    QLabel,
    QSizePolicy,
)
from PyQt6.QtGui import QIcon
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtCore import Qt


class BrowserApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle("Browser App")
        self.setWindowIcon(QIcon('kteam.jpg'))
        self.setGeometry(100, 100, 800, 600)

        self.back_button = QPushButton()
        self.back_button.setIcon(QApplication.style().standardIcon(QStyle.StandardPixmap.SP_ArrowLeft))
        self.back_button.clicked.connect(self.go_back)

        self.forward_button = QPushButton()
        self.forward_button.setIcon(QApplication.style().standardIcon(QStyle.StandardPixmap.SP_ArrowRight))
        self.forward_button.clicked.connect(self.go_forward)

        self.search_line_edit = QLineEdit()
        self.search_line_edit.returnPressed.connect(self.navigate)

        hbox = QHBoxLayout()
        hbox.addWidget(self.back_button)
        hbox.addWidget(self.forward_button)
        hbox.addWidget(self.search_line_edit)

        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("https://www.google.com"))
        self.browser.urlChanged.connect(self.update_search_line_edit)

        kteam_label = QLabel('@kteam', self)
        kteam_label.setAlignment(Qt.AlignmentFlag.AlignRight)
        last_item_policy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        kteam_label.setSizePolicy(last_item_policy)

        vbox = QVBoxLayout()
        vbox.addLayout(hbox)
        vbox.addWidget(self.browser)
        vbox.addWidget(kteam_label)

        central_widget = QWidget()
        central_widget.setLayout(vbox)
        self.setCentralWidget(central_widget)

    def go_back(self):
        self.browser.back()

    def go_forward(self):
        self.browser.forward()

    def update_search_line_edit(self, url):
        self.search_line_edit.setText(url.toString()) 

    def navigate(self):
        url = self.search_line_edit.text().strip()
        if not url.startswith("http://") and not url.startswith("https://"):
            if "." in url:
                url = "https://" + url
            else:
                url = f"https://www.google.com/search?q={url}"
            
        self.browser.setUrl(QUrl(url))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    browser = BrowserApp()
    browser.show()
    sys.exit(app.exec())