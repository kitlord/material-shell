from initgtk import Gtk
from components.icon import material_icon
from panels.settings.settings import toggle_settings

class SettingsWidget(Gtk.Box):
    def __init__(self):
        super().__init__(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)

        self.set_css_classes(["bar-widget"])
        self.set_hexpand(False)

        wifi = Gtk.Button()
        wifi.set_child(material_icon("wifi"))

        bluetooth = Gtk.Button()
        bluetooth.set_child(material_icon("bluetooth"))

        power = Gtk.Button()
        power.set_child(material_icon("power_settings_new"))

        for b in (wifi, bluetooth, power):
            b.connect("clicked", self._on_settings_clicked)

        self.append(wifi)
        self.append(bluetooth)
        self.append(power)

    def _on_settings_clicked(self, _button):
        root = self.get_root()
        application = root.get_application() if root else None
        toggle_settings(application=application)