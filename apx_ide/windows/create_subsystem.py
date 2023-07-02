# create_subsystem.py
#
# Copyright 2023 Mirko Brombin
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# SPDX-License-Identifier: GPL-3.0-only

from gi.repository import Gtk, GObject, Gio, Gdk, GLib, Adw, Vte, Pango


@Gtk.Template(resource_path='/org/vanillaos/drivers_utility/gtk/create-subsystem.ui')
class CreateSubsystemWindow(Adw.Window):
    __gtype_name__ = 'CreateSubsystemWindow'

    def __init__(self, window: Adw.ApplicationWIndow, **kwargs):
        super().__init__(**kwargs)
        self.set_transient_for(window)