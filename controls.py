from initgtk import Gtk
from materialwidgets import material_icon

def ControlsWidget():
    controls = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0, css_classes=["bar-widget"])
    controls.set_hexpand(False)

    wifi = Gtk.Button(css_classes=["icon-button"])
    wifi.set_child(material_icon("wifi"))

    bluetooth = Gtk.Button(css_classes=["icon-button"])
    bluetooth.set_child(material_icon("bluetooth"))

    power = Gtk.Button(css_classes=["icon-button"])
    power.set_child(material_icon("power_settings_new"))

    for b in (wifi, bluetooth, power):
        b.set_sensitive(False)

    controls.append(wifi)
    controls.append(bluetooth)
    controls.append(power)

    return controls