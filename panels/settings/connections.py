from initgtk import Gtk
from components.IconButton import IconButton
from components.FAB import FAB

def connections():
    layout = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6, css_classes=["pad"])
    layout.set_homogeneous(True) # instead set fixed height of wifi/blutooth label
    # layout.set_size_request(-1, 160)
    
    wifi = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
    wifi_toggle = IconButton("wifi", desc=["Wi-Fi", "jiofiber_1234"])
    wifi_toggle.add_css_class("--mt-padding-large")
    wifi.append(wifi_toggle)
    wifi.append(FAB("chevron_forward", expand=False))
    layout.append(wifi)

    blutooth = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
    blutooth_toggle = IconButton("bluetooth", desc=["Bluetooth"])
    blutooth_toggle.add_css_class("--mt-padding-large")
    blutooth.append(blutooth_toggle)
    blutooth.append(FAB("chevron_forward", expand=False))

    layout.append(blutooth)

    return layout