_quickActions_window = None
# from calendar import Calendar

from components.IconButton import IconButton
from components.FAB import FAB
from components.clock import Clock
from components.calendar import Calendar

MODE = 0

def _build_quickActions(application=None):
	from initgtk import Gtk, Gtk4LayerShell as LayerShell

	window = Gtk.Window(application=application)

	LayerShell.init_for_window(window)
	LayerShell.set_layer(window, LayerShell.Layer.TOP)
	LayerShell.set_anchor(window, LayerShell.Edge.TOP, True)
	LayerShell.set_anchor(window, LayerShell.Edge.LEFT, True)
	LayerShell.set_anchor(window, LayerShell.Edge.RIGHT, True)

	panel = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6, css_classes=["--mt-surface", "--mt-padding-small", "--mt-border-b-large"])

	view = None

	nav = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)

	preview = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
	scroll = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)

	if MODE:
		for i in range(2):
			wall = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
			wall.set_css_classes(["--mt-secondary", "--mt-border-large"])
			wall.set_size_request(80, 40)
			scroll.append(wall)
		preview.append(scroll)
		prev = FAB("arrow_left", expand=False)
		apply = IconButton("reset_image", ["Reset"])
		next = FAB("arrow_right", expand=False)
		view = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
		controls = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
		controls.append(prev)
		controls.append(apply)
		controls.append(next)
		thumb = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
		thumb.set_css_classes(["--mt-secondary", "--mt-border-large"])
		thumb.set_size_request(80, 40)
		view.append(thumb)
		view.append(controls)
	else:
		view = Clock()
		calendar = Calendar()
		preview.append(calendar)
		# panel.set_hexpand(True)
		# view.set_hexpand(True)
		view.set_halign(Gtk.Align.FILL)

	panel.append(view)
	calendar = IconButton("calendar_today", ["Calendar"])
	wallpaper = IconButton("wallpaper", ["Wallpaper"])
	for btn in (calendar, wallpaper):
		btn.add_css_class("--mt-padding-extra-small")
	nav.append(calendar)
	nav.append(wallpaper)
	preview.append(nav)
	panel.append(preview)

	panel.set_halign(Gtk.Align.CENTER)

	window.set_child(panel)

	def on_close_request(_window):
		_window.hide()
		return True

	window.connect("close-request", on_close_request)
	return window


def toggle_quickActions(application=None):
	global _quickActions_window

	if _quickActions_window is None:
		_quickActions_window = _build_quickActions(application=application)

	if _quickActions_window.get_visible():
		_quickActions_window.hide()
	else:
		_quickActions_window.present()

	return _quickActions_window