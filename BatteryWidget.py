from initgtk import Gtk
from progress import CircularProgressBar
from material.materialwidgets import material_icon

class BatteryWidget(Gtk.Box):
    def __init__(self, item_size, percentage=0.7, icon_name="battery_android_0"):
        super().__init__(
            orientation=Gtk.Orientation.HORIZONTAL,
            spacing=6,
            css_classes=["bar-widget"]
        )

        overlay = Gtk.Overlay()

        aspect = Gtk.AspectFrame(
            ratio=1.0,
            obey_child=False
        )

        self.progress = CircularProgressBar(item_size=item_size)
        self.progress.percentage = percentage

        aspect.set_child(self.progress)
        overlay.set_child(aspect)

        self.icon = material_icon(icon_name)
        self.icon.set_halign(Gtk.Align.CENTER)
        self.icon.set_valign(Gtk.Align.CENTER)
        self.icon.set_css_classes(["material-symbol", "battery-widget-icon"])
        overlay.add_overlay(self.icon)

        self.append(overlay)

        label = Gtk.Label(label=f"{int(percentage * 100)}")
        self.append(label)