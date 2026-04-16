from bar import bar

def layer(application=None):
    from initgtk import Gtk, Gtk4LayerShell as LayerShell

    window = Gtk.Window(application=application)

    LayerShell.init_for_window(window)
    LayerShell.set_layer(window, LayerShell.Layer.TOP)
    LayerShell.set_anchor(window, LayerShell.Edge.TOP, True)
    LayerShell.set_anchor(window, LayerShell.Edge.LEFT, True)
    LayerShell.set_anchor(window, LayerShell.Edge.RIGHT, True)
    LayerShell.auto_exclusive_zone_enable(window)

    window.add_css_class("--mt-surface")
    window.set_child(bar(28))
    window.present()