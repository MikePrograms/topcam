import os
import toml


def save_config(window, spot=None):

    if spot is not None:
        filename = "config_" + str(spot) + ".toml"
    else:
        filename = "default_config.toml"

    # Check if config folder exists. If not, create it.
    if not os.path.exists("configs"):
        os.makedirs("configs")

    with open("configs/" + filename, "w", encoding="utf-8") as file:
        toml.dump(
            {"frame_size": [window.cam_frame.width(), window.cam_frame.height()]},
            file,
        )
        toml.dump({"window_position": [window.x(), window.y()]}, file)
        toml.dump({"zoom_percent": window.zoom_percent}, file)
        toml.dump({"zoom_x": window.zoom_x}, file)
        toml.dump({"zoom_y": window.zoom_y}, file)
        toml.dump(
            {
                "guide_window_position": [
                    window.guide_window.x(),
                    window.guide_window.y(),
                ]
            },
            file,
        )
        toml.dump(
            {
                "guide_window_size": [
                    window.guide_window.width(),
                    window.guide_window.height(),
                ]
            },
            file,
        )


def load_config(window, spot=None):

    if spot is not None:
        filename = "config_" + str(spot) + ".toml"
        # Check if the file exists. If not, show a message and return.
        if not os.path.exists("configs/" + filename):
            print("Config file not found. You need to save a config first.")
            return
    else:
        filename = "default_config.toml"

    with open("configs/" + filename, "r", encoding="utf-8") as file:
        data = toml.load(file)

        frame_size = data["frame_size"]
        window_position = data["window_position"]
        window.zoom_percent = data["zoom_percent"]
        window.zoom_x = data["zoom_x"]
        window.zoom_y = data["zoom_y"]
        guide_window_position = data["guide_window_position"]
        guide_window_size = data["guide_window_size"]
        window.cam_frame.resize(frame_size[0], frame_size[1])
        window.setFixedSize(window.cam_frame.width(), window.cam_frame.height())
        window.move(window_position[0], window_position[1])
        window.guide_window.move(guide_window_position[0], guide_window_position[1])
        window.guide_window.resize(guide_window_size[0], guide_window_size[1])


def create_config(window):
    print("Config file not found. Generating...")
    window.cam_frame.resize(1000, 1000)
    window.setFixedSize(window.cam_frame.width(), window.cam_frame.height())
    window.zoom_percent = 100000
    window.zoom_x = 0
    window.zoom_y = 0
    window.guide_window.resize(540, 960)
    save_config(window)


def save_config_as(window, spot):
    save_config(window, spot)
    print("Saved config as " + str(spot))


def load_config_as(window, spot):
    load_config(window, spot)
    print("Loaded config " + str(spot))
