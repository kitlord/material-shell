from layer import layer
import signal
import materialcss
from initgtk import Gtk

def on_activate(app):
    materialcss.generate_css()
    materialcss.watch_css_files()
    app.hold()
    layer(application=app)

app = Gtk.Application(application_id="org.astora.shell")
app.connect("activate", on_activate)

signal.signal(signal.SIGINT, lambda *_: app.quit())

app.run(None)