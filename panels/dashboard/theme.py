from initgtk import Gtk
from components.FAB import FAB
from components.IconButton import IconButton

def theme():
    layout = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6, css_classes=["pad"])
    themes = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
    appearance = IconButton("palette", desc=["Appearance"])
    dark_mode = IconButton("dark_mode", desc=["Dark Mode"])
    for item in (appearance, dark_mode):
        item.add_css_class("--mt-padding-small")
        themes.append(item)
    layout.append(themes)
    layout.append(FAB("settings", expand=False))
    return layout