#!/usr/bin/python
# -*- coding: latin-1 -*-
from chargen import chargen

import kivy
kivy.require('1.9.1')

from kivy.app import App
from kivy.core.window import Window
from kivy.uix.button import Button

class SRNPCGen(App):
    def __init__(self):
        super(SRNPCGen, self).__init__()
        self.Char = chargen.RandomCharacter()

    def on_motion(self, etype, motionevent):
        print(motionevent)

    Window.bind(on_motion=on_motion)

    class AttrButton(Button):
        pass

if __name__ == '__main__':
    SRNPCGen().run()
