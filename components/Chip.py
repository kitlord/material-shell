from initgtk import Gtk
from components.icon import material_icon

class Chip(Gtk.Box):
    def __init__(self, label, icon_name):
        super().__init__(orientation=Gtk.Orientation.HORIZONTAL, spacing=0, css_classes=["bar-widget"])
        
        icon = material_icon(icon_name)
        icon.set_halign(Gtk.Align.CENTER)
        icon.set_valign(Gtk.Align.CENTER)
        icon.set_css_classes(["material-symbol"])
    
        self.set_halign(Gtk.Align.START)
        self.append(icon)

        if type(label) == str:
            self.append(Gtk.Label(label=label))
        else:
            self.append(Gtk.Label(label=f"{int(label * 100)}"))