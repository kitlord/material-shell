def Workspace(item_size):
    from initgtk import Gtk, Adw, GLib

    overlay = Gtk.Overlay()
    overlay.set_halign(Gtk.Align.CENTER)
    overlay.set_valign(Gtk.Align.CENTER)
    overlay.set_vexpand(False)
    overlay.set_hexpand(False)

    workspace = Gtk.Box(
        orientation=Gtk.Orientation.HORIZONTAL,
        css_classes=["bar-widget", "workspace"],
        spacing=0,
    )
    workspace.set_hexpand(False)
    workspace.set_vexpand(False)
    overlay.set_child(workspace)

    knob = Gtk.Box(css_classes=["knob", "--mt-shape-full"])
    knob.set_halign(Gtk.Align.START)
    knob.set_valign(Gtk.Align.CENTER)
    overlay.add_overlay(knob)

    items = []
    current = {"left": None, "right": None}

    def set_knob_geometry(left, right):
        knob.set_margin_start(int(left))
        knob.set_size_request(int(right - left), item_size)

    def get_item_bounds(index):
        widget = items[index - 1]
        ok, bounds = widget.compute_bounds(workspace)
        return bounds if ok else None

    def update_labels(active_index):
        for i, item in enumerate(items, start=1):
            item.set_label("" if i == active_index else str(i))

    def animate(from_l, from_r, to_l, to_r):
        moving_right = to_l > from_l
        state = {"left": from_l, "right": from_r}

        def make_anim(key, from_val, to_val, easing):
            def on_tick(value):
                state[key] = from_val + (to_val - from_val) * value
                set_knob_geometry(state["left"], state["right"])

            anim = Adw.TimedAnimation.new(
                knob, 0.0, 1.0, 180,
                Adw.CallbackAnimationTarget.new(on_tick)
            )
            anim.set_easing(easing)
            return anim

        if moving_right:
            first  = make_anim("right", from_r, to_r, Adw.Easing.EASE_OUT_CUBIC)
            second = make_anim("left",  from_l, to_l, Adw.Easing.EASE_OUT_QUAD)
        else:
            first  = make_anim("left",  from_l, to_l, Adw.Easing.EASE_OUT_CUBIC)
            second = make_anim("right", from_r, to_r, Adw.Easing.EASE_OUT_QUAD)

        first.play()
        GLib.timeout_add(60, lambda: (second.play(), False)[1])

    def set_active(index):
        update_labels(index)

        bounds = get_item_bounds(index)
        if bounds is None or bounds.size.width == 0:
            return

        left  = bounds.origin.x
        right = left + bounds.size.width

        if current["left"] is None:
            set_knob_geometry(left, right)
        else:
            animate(current["left"], current["right"], left, right)

        current["left"], current["right"] = left, right

    for i in range(1, 11):
        item = Gtk.Button(css_classes=["--mt-on-surface", "transparent"])
        item.set_size_request(item_size, item_size)
        items.append(item)

        item.connect("clicked", lambda _btn, idx=i: set_active(idx))
        workspace.append(item)

    def on_map(_):
        GLib.idle_add(lambda: (set_active(1), False)[1])

    overlay.connect("map", on_map)
    return overlay