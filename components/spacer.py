from initgtk import Gtk

def spacer(direction=Gtk.Orientation.HORIZONTAL):
    box = Gtk.Box(orientation=direction, spacing=0)
    if direction == Gtk.Orientation.VERTICAL:
        box.set_vexpand(True)
    else:
        box.set_hexpand(True)
    return box