from initgtk import Gtk

def spacer(direction=Gtk.Orientation.HORIZONTAL):
    box = Gtk.Box(orientation=direction, spacing=0)
    box.set_hexpand(True)
    return box