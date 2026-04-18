from initgtk import Gtk

def material_icon(name: str):
    icon = Gtk.Label(label=name)
    icon.set_css_classes(["material-symbol"])
    return icon