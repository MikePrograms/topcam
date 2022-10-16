import cv2
from PySide6 import QtGui, QtCore
from PySide6.QtWidgets import QLabel
from PySide6.QtCore import Qt


def load_cam(window):
    window.capture = cv2.VideoCapture(2)
    window.capture.set(cv2.CAP_PROP_FRAME_WIDTH, 5000)
    window.capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 5000)
    window.timer = QtCore.QTimer()
    window.timer.timeout.connect(lambda: update_frames(window))
    window.timer.start(16)
    window.cam_frame = QLabel(window)
    window.zoom_percent = 100000
    window.zoom_x = 0
    window.zoom_y = 0
    window.drag_pos = None
    window.portrait_mode = False
    window.landscape_mode = False


def update_frames(window):
    captured, image = window.capture.read()

    if captured:
        color_swapped_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        qimage_image = QtGui.QImage(
            color_swapped_image.data,
            color_swapped_image.shape[1],
            color_swapped_image.shape[0],
            color_swapped_image.strides[0],
            QtGui.QImage.Format_RGB888,
        )

        qpixmap_image = QtGui.QPixmap.fromImage(qimage_image)
        qpixmap_image = qpixmap_image.scaled(
            qpixmap_image.width() * window.zoom_percent / 100000,
            qpixmap_image.height() * window.zoom_percent / 100000,
        )
        final_qpixmap_image = qpixmap_image.copy(
            window.zoom_x,
            window.zoom_y,
            window.cam_frame.width(),
            window.cam_frame.height(),
        )

        if not window.portrait_mode and not window.landscape_mode:
            mask = QtGui.QPixmap(window.cam_frame.width(), window.cam_frame.height())

            mask.fill(Qt.transparent)
            painter = QtGui.QPainter(mask)
            painter.setRenderHint(QtGui.QPainter.Antialiasing)
            painter.setBrush(Qt.white)
            painter.setPen(Qt.NoPen)
            painter.drawEllipse(
                0, 0, window.cam_frame.width(), window.cam_frame.height()
            )
            painter.end()

            final_qpixmap_image.setMask(mask.mask())

        window.cam_frame.setPixmap(final_qpixmap_image)
