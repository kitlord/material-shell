from initgtk import Gtk
from components.icon import material_icon

class FAB(Gtk.AspectFrame):
    def __init__(self, icon_name, expand=True):
        super().__init__(xalign=0.5, yalign=0.5, ratio=1.0, obey_child=False, css_classes=["material-widget"])
        icon = material_icon(icon_name)
        self.set_hexpand(expand)
        self.set_child(icon)