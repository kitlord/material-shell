THEME_MODE = "dark"
# THEME_MODE = "light"

APP_FONT = "Roboto 11"

import json

from gi.repository import Gio, GLib

_css_monitors = []
_reload_source_id = 0

def generate_css():
    from gi.repository import Gtk, Gdk
    with open("colors.json", "r") as f:
        data = json.load(f)
        
    colors = data.get("colors", {})
    css = ""
    
    shapes = {
        "none": "0px",
        "extra-small": "4px",
        "small": "8px",
        "medium": "12px",
        "large": "16px",
        "large-increased": "20px",
        "extra-large": "28px",
        "extra-large-increased": "32px",
        "extra-extra-large": "48px",
        "full": "9999px"
    }

    # Generate CSS for the selected THEME_MODE
    css += f"/* {THEME_MODE.capitalize()} Theme */\n"
    css += "* { all: unset; background: transparent; border: none; padding: 0; margin: 0;}"
    css += ":root {\n"
        
    for name, value in colors.items():
        css_name = name.replace('_', '-')
        hex_color = value.get(THEME_MODE, {}).get("color", "")
        if hex_color:
            css += f"  --mt-{css_name}: {hex_color};\n"

    for name, value in shapes.items():
        css += f"  --mt-shape-{name}: {value};\n"

    css += "}\n\n"

    # Generate utility classes for backgrounds and text colors
    for name in colors.keys():
        css_name = name.replace('_', '-')
        css += f".--mt-{css_name} {{\n"

        if "on_" in name:
            css += f"  color: var(--mt-{css_name});\n"
            replaced_name = css_name.replace('on-', '')
            if replaced_name in colors:
                css += f"  background: var(--mt-{replaced_name});\n"
            # print(name, css_name, css_name.replace('on-', ''))
        else:
            if f"on_{name}" in colors:
                css += f"  color: var(--mt-on-{css_name});\n"
            css += f"  background: var(--mt-{css_name});\n"

        css += "  border: none;\n"
        css += "  padding: 0;\n"

        css += "}\n"

    # Generate utility classes for border radius
    for name in shapes.keys():
        css += f".--mt-shape-{name} {{\n"
        css += f"  border-radius: var(--mt-shape-{name});\n"
        css += "}\n\n"
    
    with open("material.css", "w") as f:
        f.write(css)
        with open("main.css", "r") as src:
            f.write(src.read())

    provider = Gtk.CssProvider()
    provider.load_from_path("material.css")
    # Set the GTK dark theme preference based on THEME_MODE
    settings = Gtk.Settings.get_default()
    if settings:
        settings.set_property("gtk-font-name", APP_FONT)
        settings.set_property("gtk-application-prefer-dark-theme", THEME_MODE == "light")

    Gtk.StyleContext.add_provider_for_display(
        Gdk.Display.get_default(),
        provider,
        Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
    )


def _on_css_source_changed(_monitor, _file, _other_file, event_type):
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
    generate_css()
    return False


def watch_css_files(paths=("main.css", "colors.json")):
    if _css_monitors:
        return

    for path in paths:
        monitor = Gio.File.new_for_path(path).monitor_file(Gio.FileMonitorFlags.NONE, None)
        monitor.connect("changed", _on_css_source_changed)
        _css_monitors.append(monitor)