import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class Main(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Proxecto recuperación")
        self.set_border_width(10)

if __name__ == '__main__':
    Main()
    Gtk.main
