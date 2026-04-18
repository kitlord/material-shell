from initgtk import Gtk
from components.Chip import Chip

class Progress(Gtk.Box):
    def __init__(self, percent, icon_name, direction=Gtk.Orientation.HORIZONTAL):
        super().__init__(
            orientation=direction,
            spacing=6
        )

        progress_bg = Gtk.LevelBar()
        progress_bg.set_min_value(0.0)
        progress_bg.set_max_value(1.0)
        progress_bg.set_value(percent)

        progress_bg.add_css_class("bar-widget")
        progress_bg.add_css_class("progress-bg")
        progress_bg.add_css_class("--mt-primary")
        progress_bg.add_css_class("--mt-border-full")

        progress_bg.set_hexpand(True)
        progress_bg.set_size_request(-1, 20)

        chip = Chip(percent, icon_name)
        self.append(chip)
        self.append(progress_bg)