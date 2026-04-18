from initgtk import Gtk, GLib, Gdk
from components.icon import material_icon
import cairo
import math
import time

class Clock(Gtk.AspectFrame):
    def __init__(self):
        super().__init__(xalign=0.5, yalign=0.5, ratio=1.0, obey_child=False, css_classes=["material-widget", "--mt-padding-extra-small"])
        self.set_hexpand(True)
        
        self.drawing_area = Gtk.DrawingArea()
        self.drawing_area.set_hexpand(True)
        self.drawing_area.set_draw_func(self.on_draw)
        
        self.set_child(self.drawing_area)
        GLib.timeout_add_seconds(60, self.update_clock)
        
    def update_clock(self):
        self.drawing_area.queue_draw()
        return True

    def on_draw(self, area, cr, width, height):
        del area  # unused
        cr.translate(width / 2, height / 2)
        style_context = self.get_style_context()
        
        N = 12
        R = min(width, height) / 2 * 0.85
        A = min(width, height) / 2 * 0.1
        
        cr.move_to(R + A, 0)
        for i in range(1, 360):
            theta = math.radians(i)
            r = R + A * math.cos(N * theta)
            cr.line_to(r * math.cos(theta), r * math.sin(theta))
        cr.close_path()

        # Fill the clock face from CSS background (dynamic theme color)
        cr.save()
        cr.clip()
        Gtk.render_background(style_context, cr, -width / 2, -height / 2, width, height)
        cr.restore()

        # Rebuild the shape path (clip() consumes current path in cairo)
        cr.move_to(R + A, 0)
        for i in range(1, 360):
            theta = math.radians(i)
            r = R + A * math.cos(N * theta)
            cr.line_to(r * math.cos(theta), r * math.sin(theta))
        cr.close_path()

        # Add tint + outline so the shape stays distinct across themes
        fg = style_context.get_color()
        cr.set_source_rgba(fg.red, fg.green, fg.blue, 0.10)
        cr.fill_preserve()
        cr.set_source_rgba(fg.red, fg.green, fg.blue, 0.58)
        cr.set_line_width(max(1.0, min(width, height) * 0.03))
        cr.stroke_preserve()
        cr.new_path()
        
        t = time.localtime()
        h = t.tm_hour % 12
        m = t.tm_min
        
        cr.set_line_cap(cairo.LINE_CAP_ROUND)
        Gdk.cairo_set_source_rgba(cr, fg)
        cr.set_line_width(min(width, height) * 0.08)
        
        # Hour hand
        cr.move_to(0, 0)
        h_angle = math.radians((h + m / 60) * 30 - 90)
        cr.line_to(math.cos(h_angle) * R * 0.5, math.sin(h_angle) * R * 0.5)
        cr.stroke()
        
        # Minute hand
        cr.move_to(0, 0)
        m_angle = math.radians(m * 6 - 90)
        cr.line_to(math.cos(m_angle) * R * 0.7, math.sin(m_angle) * R * 0.7)
        cr.stroke()
