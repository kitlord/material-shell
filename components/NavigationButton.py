from initgtk import Gtk
from components.icon import material_icon

class NavButton(Gtk.Box):
    def __init__(self, icon_name, desc=None, direction=Gtk.Orientation.HORIZONTAL):
        super().__init__(orientation=direction, spacing=3)
        self.set_hexpand(True)
        self.set_halign(Gtk.Align.FILL)
        icon = material_icon(icon_name)
        icon.set_valign(Gtk.Align.CENTER)
        icon.set_halign(Gtk.Align.FILL)
        icon.add_css_class("--mt-border-small")
        if desc:
            item = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=3)
            self.set_css_classes(["transparent"])
            icon.add_css_class("bar-widget")
            label = Gtk.Label(label=desc)
            label.set_hexpand(True)
            item.append(icon)
            item.append(label)
            self.append(item)