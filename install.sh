#!/bin/bash

# This file installs Noah Tye's disper-applet.  It doesn't actually
# move the disper-applet.py

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
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

# from http://hintsforums.macworld.com/archive/index.php/t-73839.html
abspath=`dirname $(cd "${0%/*}" 2>/dev/null; echo "$PWD"/"${0##*/}")`

cat > ~/.config/autostart/ <<EOF
[Desktop Entry]
Type=Application
Exec=$abspath/disper-applet.py
Hidden=false
NoDisplay=false
X-GNOME-Autostart-enabled=true
Name=
EOF


