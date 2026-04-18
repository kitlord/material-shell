from pathlib import Path

from gi.repository import Gio, GLib, Gtk, Gdk

from material import generate


_ROOT_DIR = Path(__file__).resolve().parent
MAIN_CSS_PATH = _ROOT_DIR / "css" / "main.css"
COLORS_JSON_PATH = _ROOT_DIR / "material" / "colors.json"
COMBINED_CSS_PATH = _ROOT_DIR / "material" / "material.css"

_provider = Gtk.CssProvider()
_monitors = []
_reload_source_id = 0


def _read_main_css(path: Path = MAIN_CSS_PATH) -> str:
	with open(path, "r", encoding="utf-8") as f:
		return f.read()


def build_combined_css() -> str:
	material = generate.generate_material_css(
		theme_mode=generate.THEME_MODE,
		colors_path=COLORS_JSON_PATH,
	)
	return f"{material}\n\n{_read_main_css()}"


def apply_css() -> None:
	css = build_combined_css()

	with open(COMBINED_CSS_PATH, "w", encoding="utf-8") as f:
		f.write(css)

	_provider.load_from_path(str(COMBINED_CSS_PATH))

	settings = Gtk.Settings.get_default()
	if settings:
		settings.set_property("gtk-font-name", generate.APP_FONT)
		settings.set_property(
			"gtk-application-prefer-dark-theme",
			generate.THEME_MODE == "dark",
		)

	Gtk.StyleContext.add_provider_for_display(
		Gdk.Display.get_default(),
		_provider,
		Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION,
	)


def _on_css_changed(_monitor, _file, _other_file, event_type):
	global _reload_source_id
	if event_type not in (
		Gio.FileMonitorEvent.CHANGED,
		Gio.FileMonitorEvent.CHANGES_DONE_HINT,
		Gio.FileMonitorEvent.CREATED,
		Gio.FileMonitorEvent.DELETED,
		Gio.FileMonitorEvent.MOVED,
		Gio.FileMonitorEvent.MOVED_IN,
		Gio.FileMonitorEvent.MOVED_OUT,
	):
		return

	if _reload_source_id:
		GLib.source_remove(_reload_source_id)

	_reload_source_id = GLib.timeout_add(120, _reload_css)


def _reload_css():
	global _reload_source_id
	_reload_source_id = 0
	apply_css()
	return False


def watch_css_files(paths=(MAIN_CSS_PATH, COLORS_JSON_PATH)) -> None:
	if _monitors:
		return

	for path in paths:
		monitor = Gio.File.new_for_path(str(path)).monitor_file(Gio.FileMonitorFlags.NONE, None)
		monitor.connect("changed", _on_css_changed)
		_monitors.append(monitor)


def setup() -> None:
	apply_css()
	watch_css_files()
