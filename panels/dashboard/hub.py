from components.spacer import spacer
from initgtk import Gtk
from components.NavigationButton import NavButton

def hub():
    layout = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0, css_classes=["pad"])
    layout.append(spacer(direction=Gtk.Orientation.VERTICAL))
    integrations = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
    integrations.set_homogeneous(True)
    integrations.set_hexpand(True)
    integrations.append(NavButton("notifications", desc="Alerts"))
    integrations.append(NavButton("neurology", desc="AI"))
    integrations.append(NavButton("content_paste", desc="Clipboard"))
    integrations.append(NavButton("book_2", desc="Notes"))
    # integrations.append(IconButton("deployed_code", desc="Processes"))
    layout.append(integrations)

    return layout