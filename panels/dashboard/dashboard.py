_dashboard_window = None
import panels.dashboard.mixer
import panels.dashboard.theme
import panels.dashboard.hub
import panels.dashboard.geo

def _build_dashboard(application=None):
	from initgtk import Gtk, Gtk4LayerShell as LayerShell

	window = Gtk.Window(application=application)

	LayerShell.init_for_window(window)
	LayerShell.set_layer(window, LayerShell.Layer.TOP)
	LayerShell.set_anchor(window, LayerShell.Edge.TOP, True)
	LayerShell.set_anchor(window, LayerShell.Edge.BOTTOM, True)
	LayerShell.set_anchor(window, LayerShell.Edge.LEFT, True)

	panel = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6, css_classes=["transparent", "--mt-margin-small"])
	mixer = panels.dashboard.mixer.mixer()
	theme = panels.dashboard.theme.theme()
	geo = panels.dashboard.geo.geo()
	hub = panels.dashboard.hub.hub()
	panel.append(mixer)
	panel.append(geo)
	panel.append(theme)
	panel.append(hub)

	# panel.set_size_request(260, -1)

	window.set_child(panel)

	def on_close_request(_window):
		_window.hide()
		return True

	window.connect("close-request", on_close_request)
	return window


def toggle_dashboard(application=None):
	global _dashboard_window

	if _dashboard_window is None:
		_dashboard_window = _build_dashboard(application=application)

	if _dashboard_window.get_visible():
		_dashboard_window.hide()
	else:
		_dashboard_window.present()

	return _dashboard_window
