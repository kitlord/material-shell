def power():
    from initgtk import Gtk
    layout = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
    
    power_btn = Gtk.Button(css_classes=["icon-button"])
    power_btn.set_child(Gtk.Label(label="power_settings_new", css_classes=["material-symbol"]))
    power_btn.set_sensitive(False)

    layout.append(power_btn)
    

    return layout