from initgtk import Gtk
from components.Progress import Progress
from components.FAB import FAB

def mixer():
    layout = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=12, css_classes=["pad"])
    layout.append(Progress(0.75, "brightness_medium"))
    layout.append(Progress(0.75, "volume_up"))
    layout.append(Progress(0.5, "device_thermostat"))

    tools = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
    tools.append(FAB("screenshot_frame_2"))
    tools.append(FAB("videocam"))
    tools.append(FAB("colorize"))
    tools.append(FAB("mic"))
    layout.append(tools)

    return layout