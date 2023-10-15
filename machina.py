#!/usr/bin/python
# -*- coding: utf-8 -*-0
import urwid

if __name__=="__main__":
    def exit_on_q(key):
        if key in ('q', 'Q'):
            raise urwid.ExitMainLoop()

    palette = [
        ('banner', 'black', 'light gray'),
        ('streak', 'black', 'red'),
        ('bg', 'black', 'blue'), ]

    txt = urwid.Text(('banner', u" Hello World "), align='center')
    map1 = urwid.AttrMap(txt, 'streak')
    fill = urwid.Filler(map1)
    map2 = urwid.AttrMap(fill, 'bg')
    loop = urwid.MainLoop(map2, palette, unhandled_input=exit_on_q)
    loop.run()
    print("Hi, I'm Machina Ratiocinatrix.")

"""or
chmod +x machina.py
./machina.py
"""