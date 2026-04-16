_dashboard_window = None


def _build_dashboard(application=None):
	from initgtk import Gtk, Gtk4LayerShell as LayerShell

	window = Gtk.Window(application=application)

	LayerShell.init_for_window(window)
	LayerShell.set_layer(window, LayerShell.Layer.TOP)
	LayerShell.set_anchor(window, LayerShell.Edge.TOP, True)
	LayerShell.set_anchor(window, LayerShell.Edge.BOTTOM, True)
	LayerShell.set_anchor(window, LayerShell.Edge.LEFT, True)
	# LayerShell.set_margin(window, LayerShell.Edge.TOP, 34)
	# LayerShell.set_keyboard_mode(window, LayerShell.KeyboardMode.ON_DEMAND)

	panel = Gtk.Box(
		orientation=Gtk.Orientation.VERTICAL,
		spacing=12,
		css_classes=["--mt-surface", "dashboard-panel"],
	)
	panel.set_size_request(360, -1)
	panel.set_margin_top(12)
	panel.set_margin_bottom(12)
	panel.set_margin_end(12)
	panel.set_margin_start(12)

	title = Gtk.Label(label="Dashboard", xalign=0)
	title.set_css_classes(["--mt-on-surface"])
	title.add_css_class("dashboard-title")

	content = Gtk.Label(label="Quick controls and glance widgets go here.", xalign=0)
	content.set_css_classes(["--mt-on-surface-variant"])

	panel.append(title)
	panel.append(content)

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
