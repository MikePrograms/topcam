from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Qt


def load_guide(window):
    window.guide_window = QWidget()
    flags = Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint
    window.guide_window.setWindowFlags(flags)
    window.guide_window.setAttribute(Qt.WA_ShowWithoutActivating)
    window.guide_window.setAttribute(Qt.WA_TransparentForMouseEvents)
    style = "background-color: rgba(0, 0, 0, 0); border: 5px solid green;"
    window.guide_window.setStyleSheet(style)
    window.guide_window.setFixedSize(540, 960)
