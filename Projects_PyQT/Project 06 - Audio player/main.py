import sys
import os
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QLabel,
    QHBoxLayout,
    QVBoxLayout,
    QPushButton,
    QSlider,
    QFileDialog,
    QStyle,
    QSizePolicy,
)
from PyQt6.QtMultimedia import QMediaPlayer, QAudioOutput
from PyQt6.QtGui import QIcon, QAction
from PyQt6.QtCore import Qt, QUrl


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Video Player")
        self.setWindowIcon(QIcon('kteam.jpg'))

        self.create_menu_bar()

        self.media_player = QMediaPlayer()
        audio_output = QAudioOutput(self.media_player)
        audio_output.setVolume(50)
        self.media_player.setAudioOutput(audio_output)

        self.media_player.playbackStateChanged.connect(self.status_changed)
        self.media_player.positionChanged.connect(self.position_changed)
        self.media_player.durationChanged.connect(self.duration_changed)

        self.label = QLabel("No music")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.progress_slider = QSlider(Qt.Orientation.Horizontal)
        self.progress_slider.setRange(0, 0)
        self.progress_slider.sliderMoved.connect(self.set_position)

        self.seek_backward_button = QPushButton()
        self.seek_backward_button.setIcon(QApplication.style().standardIcon(QStyle.StandardPixmap.SP_MediaSeekBackward))
        self.seek_backward_button.clicked.connect(self.seek_backward)

        self.play_button = QPushButton()
        self.play_button.setIcon(QApplication.style().standardIcon(QStyle.StandardPixmap.SP_MediaPlay))
        self.play_button.clicked.connect(self.play)

        self.seek_forward_button = QPushButton()
        self.seek_forward_button.setIcon(QApplication.style().standardIcon(QStyle.StandardPixmap.SP_MediaSeekForward))
        self.seek_forward_button.clicked.connect(self.seek_forward)

        hbox = QHBoxLayout()
        hbox.addStretch()
        hbox.addWidget(self.seek_backward_button)
        hbox.addWidget(self.play_button)
        hbox.addWidget(self.seek_forward_button)
        hbox.addStretch()

        kteam_label = QLabel('@kteam', self)
        kteam_label.setAlignment(Qt.AlignmentFlag.AlignRight)
        last_item_policy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        kteam_label.setSizePolicy(last_item_policy)

        vbox = QVBoxLayout()
        vbox.addWidget(self.label)
        vbox.addWidget(self.progress_slider)
        vbox.addLayout(hbox)
        vbox.addWidget(kteam_label)

        widget = QWidget()
        widget.setLayout(vbox)
        self.setCentralWidget(widget)

    def status_changed(self, status):
        if status == QMediaPlayer.PlaybackState.PlayingState:
            self.play_button.setIcon(QApplication.style().standardIcon(QStyle.StandardPixmap.SP_MediaPause))
        else:
            self.play_button.setIcon(QApplication.style().standardIcon(QStyle.StandardPixmap.SP_MediaPlay))

    def create_menu_bar(self):
        self.menu_bar = self.menuBar()
        self.menu_bar.setNativeMenuBar(False)

        file_menu = self.menu_bar.addMenu('File')

        open_action = QAction('Open', self)
        open_action.setShortcut('Ctrl+O')
        open_action.triggered.connect(self.open_file)
        file_menu.addAction(open_action)

        exit_action = QAction('Exit', self)        
        exit_action.setShortcut('Ctrl+Q')
        exit_action.triggered.connect(self.exit)
        file_menu.addAction(exit_action)

    def open_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Open Audio File", "", "Audio Files (*.mp3 *.wav)")

        if file_path:
            media_content = QUrl.fromLocalFile(file_path)
            self.media_player.setSource(media_content)
            self.media_player.play()
            self.play_button.setIcon(QApplication.style().standardIcon(QStyle.StandardPixmap.SP_MediaPause))
            
            self.label.setText(os.path.basename(file_path))

    def exit(self):
        sys.exit(app.exec_())

    def play(self):
        if self.media_player.playbackState() == QMediaPlayer.PlaybackState.PlayingState:
            self.media_player.pause()
        else:
            self.media_player.play()

    def seek_backward(self):
        self.media_player.setPosition(self.media_player.position() - 1000)

    def seek_forward(self):
        self.media_player.setPosition(self.media_player.position() + 1000)

    def position_changed(self, position):
        self.progress_slider.setValue(position)

    def duration_changed(self, duration):
        self.progress_slider.setRange(0, duration)

    def set_position(self, position):
        self.media_player.setPosition(position)

if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec())