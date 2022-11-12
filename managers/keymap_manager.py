from PySide6 import QtCore


def load_keymap(window, event):
    key_quit = event.key() == QtCore.Qt.Key_Q or event.key() == QtCore.Qt.Key_Escape

    load_movement_keymap(window, event)
    load_sizing_keymap(window, event)
    load_mode_keymap(window, event)
    load_guide_keymap(window, event)
    load_config_keymap(window, event)

    if key_quit:
        window.guide_window.close()
        window.close()

    window.save_config()
    return


def load_config_keymap(window, event):
    key_save_spot_1 = event.key() == event.key() == QtCore.Qt.Key_Exclam
    key_load_spot_1 = event.key() == QtCore.Qt.Key_1
    key_save_spot_2 = event.key() == QtCore.Qt.Key_At
    key_load_spot_2 = event.key() == QtCore.Qt.Key_2
    key_save_spot_3 = event.key() == QtCore.Qt.Key_NumberSign
    key_load_spot_3 = event.key() == QtCore.Qt.Key_3
    key_save_spot_4 = event.key() == QtCore.Qt.Key_Dollar
    key_load_spot_4 = event.key() == QtCore.Qt.Key_4
    key_save_spot_5 = event.key() == QtCore.Qt.Key_Percent
    key_load_spot_5 = event.key() == QtCore.Qt.Key_5

    if key_save_spot_1:
        window.save_config_as(1)
        return
    if key_load_spot_1:
        window.load_config_as(1)
        return
    if key_save_spot_2:
        window.save_config_as(2)
    if key_load_spot_2:
        window.load_config_as(2)
    if key_save_spot_3:
        window.save_config_as(3)
    if key_load_spot_3:
        window.load_config_as(3)
    if key_save_spot_4:
        window.save_config_as(4)
    if key_load_spot_4:
        window.load_config_as(4)
    if key_save_spot_5:
        window.save_config_as(5)
    if key_load_spot_5:
        window.load_config_as(5)


def load_mode_keymap(window, event):
    key_portrait = (
        event.key() == QtCore.Qt.Key_P and event.modifiers() == QtCore.Qt.NoModifier
    )
    key_landscape = (
        event.key() == QtCore.Qt.Key_L and event.modifiers() == QtCore.Qt.NoModifier
    )

    key_reverse = event.key() == QtCore.Qt.Key_R

    if key_portrait:
        if window.portrait_mode:
            window.portrait_mode = False
        elif not window.portrait_mode:
            window.portrait_mode = True
            window.cam_frame.resize(540, 960)
            window.setFixedSize(window.cam_frame.width(), window.cam_frame.height())
            window.save_config()
            window.portrait_mode = True

    if key_landscape:
        if window.landscape_mode:
            window.portrait_mode = False
            window.cam_frame.resize(960, 540)
            window.setFixedSize(window.cam_frame.width(), window.cam_frame.height())
            window.save_config()
        elif not window.landscape_mode:
            window.portrait_mode = False

    if key_reverse:
        if window.reverse_mode:
            window.reverse_mode = False
        elif not window.reverse_mode:
            window.reverse_mode = True


def load_guide_keymap(window, event):
    key_guide = event.key() == QtCore.Qt.Key_G

    if key_guide:
        if window.guide_window.isVisible():
            window.guide_window.hide()
        else:
            window.guide_window.show()


def load_movement_keymap(window, event):
    shift_pressed = event.modifiers() == QtCore.Qt.ShiftModifier
    key_left = event.key() == QtCore.Qt.Key_H or event.key() == QtCore.Qt.Key_A
    key_down = event.key() == QtCore.Qt.Key_J or event.key() == QtCore.Qt.Key_S
    key_up = event.key() == QtCore.Qt.Key_K or event.key() == QtCore.Qt.Key_W
    key_right = event.key() == QtCore.Qt.Key_L or event.key() == QtCore.Qt.Key_D

    if shift_pressed:

        # Move L/D/U/R
        # Prevent moving out of frame

        if key_left:
            if window.zoom_x > 5:
                window.zoom_x -= 5
        if key_up:
            if window.zoom_y > 5:
                window.zoom_y -= 5
        if key_right:
            window.setFixedSize(window.cam_frame.width(), window.cam_frame.height())
            zoom_width = window.width() * window.zoom_percent / 100000
            if window.cam_frame.width() - window.zoom_x > zoom_width:
                window.zoom_x += 5
        if key_down:
            window.setFixedSize(window.cam_frame.width(), window.cam_frame.height())
            zoom_height = window.height() * window.zoom_percent / 100000
            if window.cam_frame.height() - window.zoom_y > zoom_height - 5:
                window.zoom_y += 5
        return

    if key_left:
        if window.guide_window.isVisible():
            window.guide_window.move(
                window.guide_window.x() - 10, window.guide_window.y()
            )
        else:
            window.move(window.x() - 25, window.y())
    if key_down:
        if window.guide_window.isVisible():
            window.guide_window.move(
                window.guide_window.x(), window.guide_window.y() + 10
            )
        else:
            window.move(window.x(), window.y() + 25)
    if key_up:
        if window.guide_window.isVisible():
            window.guide_window.move(
                window.guide_window.x(), window.guide_window.y() - 10
            )
        else:
            window.move(window.x(), window.y() - 25)
    if key_right:
        if window.guide_window.isVisible():
            window.guide_window.move(
                window.guide_window.x() + 10, window.guide_window.y()
            )
        else:
            window.move(window.x() + 25, window.y())


def load_sizing_keymap(window, event):
    shift_pressed = event.modifiers() == QtCore.Qt.ShiftModifier
    key_in = event.key() == QtCore.Qt.Key_I or event.key() == QtCore.Qt.Key_Q
    key_out = event.key() == QtCore.Qt.Key_O or event.key() == QtCore.Qt.Key_E

    if key_in and shift_pressed:
        window.zoom_percent = window.zoom_percent * 1.05
        return
    if key_out and shift_pressed:
        window.zoom_percent = window.zoom_percent * 0.95
        return

    if key_in:
        if window.guide_window.isVisible():
            window.guide_window.resize(
                window.guide_window.width() * 1.05, window.guide_window.height() * 1.05
            )
        else:
            window.cam_frame.resize(
                window.cam_frame.width() * 1.05, window.cam_frame.height() * 1.05
            )
            window.zoom_percent = window.zoom_percent * 1.05
            window.zoom_x = window.zoom_x * 1.05
            window.zoom_y = window.zoom_y * 1.05
            window.setFixedSize(window.cam_frame.width(), window.cam_frame.height())
    if key_out:
        if window.guide_window.isVisible():
            window.guide_window.resize(
                window.guide_window.width() * 0.95, window.guide_window.height() * 0.95
            )
        else:
            window.cam_frame.resize(
                window.cam_frame.width() * 0.95, window.cam_frame.height() * 0.95
            )
            window.zoom_percent = window.zoom_percent * 0.95
            window.zoom_x = window.zoom_x * 0.95
            window.zoom_y = window.zoom_y * 0.95
            window.setFixedSize(window.cam_frame.width(), window.cam_frame.height())
