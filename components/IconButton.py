from initgtk import Gtk
from components.icon import material_icon

class IconButton(Gtk.Box):
    def __init__(self, icon_name, desc=None, direction=Gtk.Orientation.HORIZONTAL):
        super().__init__(orientation=direction, spacing=3, css_classes=[])
        self.set_hexpand(True)
        self.set_halign(Gtk.Align.FILL)
        icon = material_icon(icon_name)
        icon.set_valign(Gtk.Align.CENTER)
        self.set_css_classes(["material-widget"])
        
        if desc:
            item = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=3)
            item.set_valign(Gtk.Align.CENTER)
            item.set_hexpand(False)
            for label in desc:
                label = Gtk.Label(label=label)
                label.set_halign(Gtk.Align.START)
                label.set_valign(Gtk.Align.CENTER)
                item.append(label)
            self.append(icon)
            self.append(item)