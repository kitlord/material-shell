from initgtk import Gtk
from materialwidgets import material_icon

class GlanceWidget(Gtk.Box):
    def __init__(self):
        super().__init__(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)

        self.set_css_classes(["bar-widget"])

        volume = Gtk.Button(css_classes=["icon-button"])
        volume.set_child(material_icon("volume_up"))

        brightness = Gtk.Button(css_classes=["icon-button"])
        brightness.set_child(material_icon("brightness_medium"))

        for b in (volume, brightness):
            b.set_sensitive(False)

        self.append(volume)
        self.append(brightness)