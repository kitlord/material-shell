from panels.bar.settings import settings
from panels.bar.workspace import Workspace
from panels.bar.music import MusicWidget
from components.spacer import spacer
from panels.bar.glance import GlanceWidget
from components.battery import Battery

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
    bar.append(Battery(item_size=item_size))
    bar.append(Battery(icon_name="bluetooth", item_size=item_size))
    bar.append(settings())

    return bar