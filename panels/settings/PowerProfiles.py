from initgtk import Gtk
from components.FAB import FAB

def powerprofiles():
    layout = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6, css_classes=["pad"])
    core = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
    secondary = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)

    core.append(FAB("power_settings_new"))
    core.append(FAB("restart_alt"))
    core.append(FAB("coffee"))

    child = core.get_first_child()
    while child is not None:
        child.set_hexpand(True)
        child = child.get_next_sibling()

    layout.append(core)

    secondary.append(FAB("lock"))
    secondary.append(FAB("sync"))
    secondary.append(FAB("bolt"))
    
    layout.append(secondary)

    return layout