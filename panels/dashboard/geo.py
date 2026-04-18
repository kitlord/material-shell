from components.spacer import spacer
from initgtk import Gtk
from components.Chip import Chip

def geo():
    layout = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6, css_classes=["pad"])
    ambient = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
    # ambient.set_hexpand(True)
    weather = Chip("Partly Cloudy", "partly_cloudy_day")
    weather.set_halign(Gtk.Align.FILL)
    weather.set_hexpand(True)
    ambient.append(weather)
    
    temperature = Chip("22°", "device_thermostat")
    temperature.set_halign(Gtk.Align.FILL)
    temperature.set_hexpand(True)
    ambient.append(temperature)

    layout.append(ambient)
    
    location = Chip("Malappuram", "location_on")
    location.set_halign(Gtk.Align.FILL)
    layout.append(location)
    
    return layout