from initgtk import Gtk
from materialwidgets import material_icon

class MusicWidget(Gtk.Box):
    def __init__(self):
        super().__init__(orientation=Gtk.Orientation.HORIZONTAL, spacing=12)

        self.set_css_classes(["bar-widget", "--mt-shape-full"])

        # Album art
        details = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
        cover = material_icon("album")
        details.append(cover)

        title = Gtk.Label(label="Song Title")
        title.set_xalign(0)
        title.set_css_classes(["title"])
        details.append(title)

        # Controls (static)
        controls = Gtk.Box(spacing=0)

        prev_btn = Gtk.Button()
        prev_btn.set_child(material_icon("skip_previous"))

        play_btn = Gtk.Button()
        play_btn.set_child(material_icon("play_arrow"))

        next_btn = Gtk.Button()
        next_btn.set_child(material_icon("skip_next"))

        for b in (prev_btn, play_btn, next_btn):
            b.set_sensitive(False)

        controls.append(prev_btn)
        controls.append(play_btn)
        controls.append(next_btn)

        # Layout
        self.append(details)
        self.append(controls)