from panels.bar.settings import SettingsWidget
from panels.bar.workspace import Workspace
from panels.bar.music import MusicWidget
from components.spacer import spacer
from panels.bar.glance import GlanceWidget
from components.battery import Battery

def bar(item_size=28):
    from initgtk import Gtk

    bar = Gtk.CenterBox(css_classes=["--mt-surface", "--mt-padding-extra-small"])
    bar.set_hexpand(True)

    left = Gtk.Box(spacing=6)
    left.append(GlanceWidget())
    left.append(MusicWidget())

    center = Workspace(item_size)

    right = Gtk.Box(spacing=6)
    right.append(Battery(item_size=item_size))
    right.append(Battery(icon_name="bluetooth", item_size=item_size))
    right.append(SettingsWidget())

    bar.set_start_widget(left)
    bar.set_center_widget(center)
    bar.set_end_widget(right)

    return bar