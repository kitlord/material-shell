import controls
from workspace import Workspace
from music import MusicWidget
from spacer import spacer
from glance import GlanceWidget
from BatteryWidget import BatteryWidget

def bar(item_size = 28):
    from initgtk import Gtk
    bar = Gtk.Box(
        orientation=Gtk.Orientation.HORIZONTAL,
        css_classes=["--mt-surface", "bar"],
        spacing=12,
    )

    bar.ALIGNMENT = Gtk.Align.CENTER

    bar.set_hexpand(True)
    bar.set_vexpand(False)
    bar.append(GlanceWidget())
    bar.append(MusicWidget())
    bar.append(spacer())
    bar.append(Workspace(item_size))
    bar.append(spacer())
    bar.append(BatteryWidget(item_size=item_size)) #increases height for some reason, investigate later
    bar.append(BatteryWidget(icon_name="bluetooth", item_size=item_size))
    bar.append(controls.ControlsWidget())

    return bar