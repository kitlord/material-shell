from initgtk import Gtk
from components.Progress import Progress
from components.IconButton import IconButton

def taskamanager():
    layout = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=12, css_classes=["pad"])
    processes = {123: {"icon": "sports_esports", "name": "game", "memory": 1200, "cpu": 0.5, "disk": 0.2, "download": 5, "upload": 5, "uptime": "0:4:00"}, 321: {"icon": "fire_extinguisher", "name": "firefox", "memory": 800, "cpu": 0.2, "disk": 0.1, "download": 1, "upload": 1, "uptime": "0:14:00"}}
    selected = None

    for process in processes:
        process_button = IconButton(processes[process]["icon"], [processes[process]["name"]])
        process_button.set_css_classes([])
        layout.append(process_button)

    extras = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
    if selected:
        actions = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
        cancel = IconButton("undo", ["Cancel"])
        kill = IconButton("stop", ["Kill"])
        kill.set_css_classes(["--mt-border-full", "--mt-error-container"])
        actions.append(cancel)
        actions.append(kill)
        layout.append(actions)
        layout.append(Progress(processes[process]["cpu"], "memory"))
        layout.append(Progress(processes[process]["memory"] / 16000, "memory_alt"))
        layout.append(Progress(processes[process]["disk"], "hard_disk"))
        extras.append(IconButton("timer", [processes[process]["uptime"]]))
        extras.append(IconButton("arrow_downward", [f"{processes[process]['download']} Mbps"]))
        extras.append(IconButton("arrow_upward", [f"{processes[process]['upload']} Mbps"]))
    else:
        layout.append(Progress(0.6, "memory"))
        layout.append(Progress(0.16, "memory_alt"))
        layout.append(Progress(0.6, "hard_disk"))
        extras.append(IconButton("timer", ["0:4:00"]))
        extras.append(IconButton("arrow_downward", ["5 Mbps"]))
        extras.append(IconButton("arrow_upward", ["5 Mbps"]))
    
    layout.append(extras)

    # layout.append(Progress(0.75, "brightness_medium"))
    # layout.append(Progress(0.75, "volume_up"))
    # layout.append(Progress(0.5, "device_thermostat"))

    return layout