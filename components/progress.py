# CircularProgressBar.py
import math
import cairo

from initgtk import Gtk, Gdk, GObject

class CircularProgressBar(Gtk.DrawingArea):
    __gtype_name__ = "CircularProgressBar"

    def __init__(self, item_size):
        super().__init__()

        self._line_width = 2
        self._percentage = 0.7
        self._center_fill_color = "#adadad"
        self._radius_fill_color = "#d3d3d3"
        self._progress_fill_color = "#4a90d9"

        self.center_filled = False
        self.radius_filled = False
        self.line_cap = cairo.LineCap.ROUND

        self.add_css_class("--mt-on-surface")
        self.add_css_class("transparent")

        self.set_draw_func(self._draw)
        self.connect("notify", lambda *_: self.queue_draw())

    # ---- GObject properties ----
    @GObject.Property(type=bool, default=False, nick="Center Fill", blurb="Center Fill toggle")
    def center_filled(self):
        return self._center_filled

    @center_filled.setter
    def center_filled(self, value):
        self._center_filled = bool(value)

    @GObject.Property(type=bool, default=False, nick="Radius Fill", blurb="Radius Fill toggle")
    def radius_filled(self):
        return self._radius_filled

    @radius_filled.setter
    def radius_filled(self, value):
        self._radius_filled = bool(value)

    @GObject.Property(type=str, default="URW Gothic", nick="Font", blurb="Font description without size")
    def font(self):
        return self._font

    @font.setter
    def font(self, value):
        self._font = value or "URW Gothic"

    @GObject.Property(type=object, nick="Line Cap", blurb="Line cap for stroke (cairo.LineCap)")
    def line_cap(self):
        return self._line_cap

    @line_cap.setter
    def line_cap(self, value):
        self._line_cap = value if value is not None else cairo.LineCap.BUTT

    @GObject.Property(type=str, default="#adadad", nick="Inside circle fill color")
    def center_fill_color(self):
        return self._center_fill_color

    @center_fill_color.setter
    def center_fill_color(self, value):
        rgba = Gdk.RGBA()
        if rgba.parse(value):
            self._center_fill_color = value

    @GObject.Property(type=str, default="#d3d3d3", nick="Circular radius fill color")
    def radius_fill_color(self):
        return self._radius_fill_color

    @radius_fill_color.setter
    def radius_fill_color(self, value):
        rgba = Gdk.RGBA()
        if rgba.parse(value):
            self._radius_fill_color = value

    @GObject.Property(type=str, default="#4a90d9", nick="Progress fill color")
    def progress_fill_color(self):
        return self._progress_fill_color

    @progress_fill_color.setter
    def progress_fill_color(self, value):
        rgba = Gdk.RGBA()
        if rgba.parse(value):
            self._progress_fill_color = value

    @GObject.Property(type=int, default=1, nick="Circle width")
    def line_width(self):
        return self._line_width

    @line_width.setter
    def line_width(self, value):
        v = max(0, int(value))
        # Clamp against current radius when possible
        r = self._calculate_radius()
        self._line_width = min(v, r if r >= 0 else v)

    @GObject.Property(type=float, default=0.0, minimum=0.0, maximum=1.0, nick="Percentage/Value")
    def percentage(self):
        return self._percentage

    @percentage.setter
    def percentage(self, value):
        self._percentage = min(1.0, max(0.0, float(value)))

    # ---- internal helpers ----
    def _calculate_radius(self):
        w = self.get_width()
        h = self.get_height()
        return max(0, min(w // 2, h // 2) - 1)

    def _parse_rgba(self, color_str):
        rgba = Gdk.RGBA()
        rgba.parse(color_str)
        return rgba

    def _draw(self, area, cr, width, height):
        del area  # unused

        center_x = width / 2.0
        center_y = height / 2.0
        radius = max(0, min(width // 2, height // 2) - 1)

        line_width = self.line_width
        if radius - line_width < 0:
            delta = 0
            line_width = radius
        else:
            delta = radius - (line_width / 2.0)

        cr.save()
        cr.set_line_cap(self.line_cap)
        cr.set_line_width(line_width)

        # Center fill
        if self.center_filled:
            cr.arc(center_x, center_y, delta, 0, 2 * math.pi)
            Gdk.cairo_set_source_rgba(cr, self._parse_rgba(self.center_fill_color))
            cr.fill()

        # Radius fill
        if self.radius_filled:
            cr.arc(center_x, center_y, delta, 0, 2 * math.pi)
            Gdk.cairo_set_source_rgba(cr, self._parse_rgba(self.radius_fill_color))
            cr.stroke()

        # Progress fill
        if self.percentage > 0:
            context = self.get_style_context()
            Gdk.cairo_set_source_rgba(cr, context.get_color())

            start = 1.5 * math.pi
            end = (1.5 + self.percentage * 2.0) * math.pi

            if line_width == 0:
                cr.move_to(center_x, center_y)
                cr.arc(center_x, center_y, delta + 1, start, end)
                cr.fill()
            else:
                cr.arc(center_x, center_y, delta, start, end)
                cr.stroke()
    
        cr.restore()