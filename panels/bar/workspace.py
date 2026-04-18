from initgtk import Gtk, Adw, GLib
from panels.QuickActions.QuickActions import toggle_quickActions


class Workspace(Gtk.Overlay):
    def __init__(self, item_size):
        super().__init__()
        self.item_size = item_size
        self.items = []
        self.current = {"left": None, "right": None}

        self.set_halign(Gtk.Align.CENTER)
        self.set_valign(Gtk.Align.CENTER)
        self.set_vexpand(False)
        self.set_hexpand(False)

        self.workspace = Gtk.Box(
            orientation=Gtk.Orientation.HORIZONTAL,
            css_classes=["bar-widget", "workspace"],
            spacing=0,
        )
        self.workspace.set_hexpand(False)
        self.workspace.set_vexpand(False)
        self.set_child(self.workspace)

        self.knob = Gtk.Box(css_classes=["knob", "--mt-border-full"])
        self.knob.set_halign(Gtk.Align.START)
        self.knob.set_valign(Gtk.Align.CENTER)
        self.add_overlay(self.knob)

        for i in range(1, 11):
            item = Gtk.Button(css_classes=["--mt-on-surface", "transparent"])
            item.set_size_request(item_size, item_size)
            item.connect("clicked", lambda _btn, idx=i: self._set_active(idx))
            self.items.append(item)
            self.workspace.append(item)

        motion = Gtk.EventControllerMotion()
        motion.connect("enter", self._on_workspace_hovered)
        self.add_controller(motion)

        self.connect("map", self._on_map)

    def _set_knob_geometry(self, left, right):
        self.knob.set_margin_start(int(left))
        self.knob.set_size_request(int(right - left), self.item_size)

    def _get_item_bounds(self, index):
        widget = self.items[index - 1]
        ok, bounds = widget.compute_bounds(self.workspace)
        return bounds if ok else None

    def _update_labels(self, active_index):
        for i, item in enumerate(self.items, start=1):
            item.set_label("" if i == active_index else str(i))

    def _animate(self, from_l, from_r, to_l, to_r):
        moving_right = to_l > from_l
        state = {"left": from_l, "right": from_r}

        def make_anim(key, from_val, to_val, easing):
            def on_tick(value):
                state[key] = from_val + (to_val - from_val) * value
                self._set_knob_geometry(state["left"], state["right"])

            anim = Adw.TimedAnimation.new(
                self.knob,
                0.0,
                1.0,
                180,
                Adw.CallbackAnimationTarget.new(on_tick),
            )
            anim.set_easing(easing)
            return anim

        if moving_right:
            first = make_anim("right", from_r, to_r, Adw.Easing.EASE_OUT_CUBIC)
            second = make_anim("left", from_l, to_l, Adw.Easing.EASE_OUT_QUAD)
        else:
            first = make_anim("left", from_l, to_l, Adw.Easing.EASE_OUT_CUBIC)
            second = make_anim("right", from_r, to_r, Adw.Easing.EASE_OUT_QUAD)

        first.play()
        GLib.timeout_add(60, lambda: (second.play(), False)[1])

    def _set_active(self, index):
        self._update_labels(index)

        bounds = self._get_item_bounds(index)
        if bounds is None or bounds.size.width == 0:
            return

        left = bounds.origin.x
        right = left + bounds.size.width

        if self.current["left"] is None:
            self._set_knob_geometry(left, right)
        else:
            self._animate(self.current["left"], self.current["right"], left, right)

        self.current["left"], self.current["right"] = left, right

    def _on_map(self, _widget):
        GLib.idle_add(lambda: (self._set_active(1), False)[1])

    def _on_workspace_hovered(self, _controller, _x, _y):
        root = self.get_root()
        application = root.get_application() if root else None
        toggle_quickActions(application=application)