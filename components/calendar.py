from components.spacer import spacer
from initgtk import Gtk
import datetime

class Calendar(Gtk.Box):
    def __init__(self):
        super().__init__(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
        self.set_hexpand(True)
        self.set_halign(Gtk.Align.FILL)
        today = datetime.date.today()
        days_to_subtract = (today.weekday() + 1) % 7
        sunday = today - datetime.timedelta(days=days_to_subtract)
        
        day_letters = ["S", "M", "T", "W", "T", "F", "S"]
        
        for i in range(7):
            current_date = sunday + datetime.timedelta(days=i)
            is_today = (current_date == today)
            
            day_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=8)
            
            day_label = Gtk.Label(label=day_letters[i])
                
            date_label = Gtk.Label(label=str(current_date.day))

            if is_today:
                day_box.set_css_classes(["material-widget", "--mt-padding-extra-small"])
            else:
                day_label.set_css_classes(["material-widget", "--mt-padding-extra-small"])
            
            day_box.append(day_label)
            day_box.append(date_label)
            self.append(day_box)
            self.append(spacer())

        