_settings_window = None
from components import spacer
from panels.settings import connections, taskmanager, PowerProfiles


def _build_settings(application=None):
    from initgtk import Gtk, Gtk4LayerShell as LayerShell

    window = Gtk.Window(application=application)

    LayerShell.init_for_window(window)
    LayerShell.set_layer(window, LayerShell.Layer.TOP)
    LayerShell.set_anchor(window, LayerShell.Edge.TOP, True)
    LayerShell.set_anchor(window, LayerShell.Edge.BOTTOM, True)
    LayerShell.set_anchor(window, LayerShell.Edge.RIGHT, True)

    panel = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=12, css_classes=["transparent", "--mt-margin-small"])

    powerprofiles = PowerProfiles.powerprofiles()
    # panel.set_size_request(260, -1)
    # panel.set_margin_top(12)
    # panel.set_margin_bottom(12)
    # panel.set_margin_end(12)
    # panel.set_margin_start(12)

    # title = Gtk.Label(label="Settings", xalign=0)
    # title.set_css_classes(["--mt-on-surface"])

    panel.append(powerprofiles)
    panel.append(connections.connections())
    panel.append(spacer.spacer(direction=Gtk.Orientation.VERTICAL))
    panel.append(taskmanager.taskamanager())
    window.set_child(panel)

    def on_close_request(_window):
        _window.hide()
        return True

    window.connect("close-request", on_close_request)
    return window

def toggle_settings(application=None):
    global _settings_window

    if _settings_window is None:
        _settings_window = _build_settings(application=application)

    if _settings_window.get_visible():
        _settings_window.hide()
    else:
        _settings_window.present()

    return _settings_window
