from initgtk import Gtk
from material.materialwidgets import material_icon
from dashboard import toggle_dashboard

class GlanceWidget(Gtk.Box):
    def __init__(self):
        super().__init__(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)

        self.set_css_classes(["bar-widget"])

        volume = Gtk.Button(css_classes=["icon-button"])
        volume.set_child(material_icon("volume_up"))

        brightness = Gtk.Button(css_classes=["icon-button"])
        brightness.set_child(material_icon("brightness_medium"))

        for b in (volume, brightness):
            b.connect("clicked", self._on_glance_clicked)

        self.append(volume)
        self.append(brightness)

    def _on_glance_clicked(self, _button):
        root = self.get_root()
        application = root.get_application() if root else None
        toggle_dashboard(application=application)