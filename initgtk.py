import gi
from ctypes import CDLL

gi.require_version("Gtk", "4.0")
gi.require_version("Adw", "1")
gi.require_version("Gtk4LayerShell", "1.0")

CDLL('libgtk4-layer-shell.so')

from gi.repository import Gtk, Adw, GLib, Gdk, GObject, Gtk4LayerShell

__all__ = ["Gtk", "Adw", "GLib", "Gdk", "GObject", "Gtk4LayerShell"]