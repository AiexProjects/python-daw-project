from PySide6.QtWidgets import QApplication, QWidget, QMainWindow, QLabel, QSplitter, QVBoxLayout ,QHBoxLayout , QGridLayout
from PySide6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("LAAV DAW")
        self.resize(1280, 720)

        transport = QLabel("Transport — play, stop, BPM")
        track_list = QLabel("Track list")
        timeline = QLabel("Timeline")
        mixer = QLabel("Mixer")

        for widget in [transport, track_list, timeline, mixer]:
            widget.setAlignment(Qt.AlignCenter)
            widget.setStyleSheet("border: 1px dashed gray; color: gray;")

        splitter = QSplitter(Qt.Horizontal)
        splitter.addWidget(track_list)
        splitter.addWidget(timeline)
        splitter.setSizes([200, 1000])
        track_list.setMaximumWidth(800)
        

        transport.setFixedHeight(30)

        root = QVBoxLayout()
        root.addWidget(transport)
        root.addWidget(splitter, 7)
        root.addWidget(mixer, 2)

        container = QWidget()
        container.setLayout(root)
        self.setCentralWidget(container)
