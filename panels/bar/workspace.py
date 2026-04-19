from initgtk import Gtk, Adw, GLib
from panels.QuickActions.QuickActions import toggle_quickActions


class Workspace(Gtk.Overlay):
    def __init__(self, item_size):
        super().__init__()
        self.item_size = item_size
        self.items = []
        # self.current = {"left": None, "right": None}
        self.cur_left = None
        self.cur_right = None
        self.active_index = None

        # self.set_halign(Gtk.Align.CENTER)
        # self.set_valign(Gtk.Align.CENTER)

        self.workspace = Gtk.Box(
            orientation=Gtk.Orientation.HORIZONTAL,
            css_classes=["bar-widget", "workspace"],
            spacing=0,
        )
        self.set_child(self.workspace)

        self.knob = Gtk.Box(css_classes=["knob", "--mt-border-full"])
        self.knob.set_halign(Gtk.Align.START)
        self.knob.set_valign(Gtk.Align.CENTER)
        self.add_overlay(self.knob)

        for i in range(1, 11):
            item = Gtk.Button(css_classes=["--mt-on-surface", "transparent"])
            item.set_size_request(item_size, item_size)
            item.connect("clicked", lambda _btn, idx=i: self._set_active(idx))
            item.set_label(str(i))
            self.items.append(item)
            self.workspace.append(item)

        motion = Gtk.EventControllerMotion()
        motion.connect("enter", self._on_workspace_hovered)
        self.add_controller(motion)

        self.connect("map", self._on_map)
        self.connect("notify::width", lambda *_: self._cache_bounds())
        self.connect("notify::height", lambda *_: self._cache_bounds())

    def _cache_bounds(self):
        self.bounds_cache = []
        for item in self.items:
            ok, b = item.compute_bounds(self.workspace)
            self.bounds_cache.append(b if ok else None)

    def _set_knob_geometry(self, left, right):
        self.knob.set_margin_start(int(left))
        self.knob.set_size_request(int(right - left), self.item_size)

    # def _get_item_bounds(self, index):
    #     widget = self.items[index - 1]
    #     ok, bounds = widget.compute_bounds(self.workspace)
    #     return bounds if ok else None

    def _get_item_bounds(self, index):
        return self.bounds_cache[index - 1]

    # def _update_labels(self, new_index):
    #     if self.active_index is not None:
    #         self.items[self.active_index - 1].set_label(str(self.active_index))

    #     self.items[new_index - 1].set_label("")
    #     self.active_index = new_index

    def _update_labels(self, new_index):
        if self.active_index:
            self.items[self.active_index - 1].set_label(str(self.active_index))
        self.items[new_index - 1].set_label("")
        self.active_index = new_index

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

        # bounds = self._get_item_bounds(index)
        # if bounds is None or bounds.size.width == 0:
        #     return

        # left = bounds.origin.x
        # right = left + bounds.size.width

        left = (index - 1) * self.item_size
        right = left + self.item_size

        if self.cur_left is None:
            self._set_knob_geometry(left, right)
        else:
            self._animate(self.cur_left, self.cur_right, left, right)

        self.cur_left = left
        self.cur_right = right

    def _on_map(self, _widget):
        # GLib.idle_add(lambda: (self._set_active(1), False)[1])
        def init():
            self._cache_bounds()
            self._set_active(1)
            return False
        GLib.idle_add(init)

    def _on_workspace_hovered(self, _controller, _x, _y):
        root = self.get_root()
        application = root.get_application() if root else None
        toggle_quickActions(application=application)