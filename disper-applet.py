#!/usr/bin/env python
# 
# disper-applet.py - an App Indicator (for GNOME and KDE) that acts as
# a GUI front-end to Willem van Engen's Disper, which can be found at
# <http://willem.engen.nl/projects/disper/>.
#
# To use disper-applet.py, first install Disper from the above URL.
# Then run install.sh, which should have come in the same directory as
# this file.  Note that this installer will not copy disper-applet.py
# anywhere, it simply adds disper-applet.py (wherever it currently
# lives) to GNOME's startup programs.
#
# Feel free to email me at <noah@tyes.us>.

# Copyright (c) 2011 Noah Tye
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# The Software shall be used for Good, not Evil.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

import sys, os
import pygtk, gtk, gobject, appindicator
pygtk.require('2.0')

CONF_FILE_LOCATION = os.path.expanduser('~/.disper_applet')

# Make the App Indicator widget

ind = appindicator.Indicator("example-simple-client", 'computer',
                             appindicator.CATEGORY_APPLICATION_STATUS)
ind.set_status(appindicator.STATUS_ACTIVE)

# Define the menu (this object is passed into build_menu, which
# returns a gtk.Menu object.

MENU = [('Laptop screen only', 'disper -s'),
        ('External screen only', 'disper -S'),
        ('Clone displays', 'disper -c'),
        ('Extend displays', [('Up', 'disper -e -t top'),
                             ('Left', 'disper -e -t left'),
                             ('Right', 'disper -e -t right'),
                             ('Down', 'disper -e -t bottom')
                             ])
        ]

def menu_click(command, menu_index_stack):
    # hack: accept arbitrary arguments and don't use them, because
    #       we use this to define GTK callbacks, which get called
    #       with GTK widgets as arguments.
    def f(*hack):
        ind.set_menu(build_menu(MENU, menu_index_stack))
        os.system(command)
        with open(CONF_FILE_LOCATION, 'w') as conf_file:
            conf_file.write(str(menu_index_stack))
    return f


def build_menu(menu_template, active_menuitems, index_stack=[]):
    menu = gtk.Menu()

    try:
        active_item = active_menuitems[0]
    except IndexError:
        active_item = -1 # no index will ever be -1, so no menu items are active

    for index, menuitem in enumerate(menu_template):
        # mnenomics
        menu_label, menu_command = menuitem

        # If this menu item was the last applied setting, draw a checkbox
        if index == active_item:
            mi = gtk.CheckMenuItem(menu_label)
            mi.set_active(True)
            menu.append(mi)
            mi.show()
        else:
            mi = gtk.MenuItem(menu_label)
            menu.append(mi)
            mi.show()

        # If it has a command, set it. Otherwise set the submenu.
        if isinstance(menu_command, str):
            mi.connect('activate', menu_click(menu_command,
                                              index_stack+[index]))
        else:
            mi.set_submenu(build_menu(menu_command, active_menuitems[1:],
                                      index_stack+[index]))

    return menu

# this catches nonexistent files as well as parse errors
try:
    with open(CONF_FILE_LOCATION) as conf_file:
        menu_index_stack = eval(conf_file.read())
except:
    menu_index_stack = []

ind.set_menu(build_menu(MENU, menu_index_stack))

gtk.main()
