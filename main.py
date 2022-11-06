import sys
from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtCore import Qt
import cam_manager
import config_manager
import keymap_manager
import guide_manager


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setStyleSheet("background-color: rgba(0, 0, 0, 0);")
        self.setFixedSize(1000, 1000)

        cam_manager.load_cam(self)
        guide_manager.load_guide(self)

        self.load_config()
        self.show()

    def save_config(self):
        config_manager.save_config(self)

    def load_config(self):
        try:
            config_manager.load_config(self)
        except FileNotFoundError:
            config_manager.create_config(self)

    def save_config_as(self, spot):
        config_manager.save_config_as(self, spot)

    def load_config_as(self, spot):
        config_manager.load_config_as(self, spot)

    def mousePressEvent(self, event):
        self.drag_pos = event.globalPos()

    def mouseMoveEvent(self, event):
        self.move(self.pos() + event.globalPos() - self.drag_pos)
        self.drag_pos = event.globalPos()
        event.accept()

    def mouseReleaseEvent(self, event):
        self.save_config()
        event.accept()

    def keyPressEvent(self, event):
        keymap_manager.load_keymap(self, event)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
