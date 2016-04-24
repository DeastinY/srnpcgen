#!/usr/bin/python
# -*- coding: latin-1 -*-
from chargen import chargen

import kivy
kivy.require('1.9.0')

from kivy.app import App
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout

class AttrWidget(GridLayout):
    def UpdateAll(self):
        app = App.get_running_app()
        app.Char.RandAll()
        self.ids['b_name'].text=app.Char.Name
        self.ids['b_age'].text=app.Char.Age
        self.ids['b_metatype'].text=app.Char.Metatype
        self.ids['b_gender'].text=app.Char.Gender
        self.ids['b_trait'].text=app.Char.Traits
        self.ids['b_special'].text=app.Char.Special

class SRNPCGen(App):
    def __init__(self):
        super(SRNPCGen, self).__init__()
        self.Char = chargen.RandomCharacter()

    def on_motion(self, etype, motionevent):
        pass
        # Maybe there is a way to react to shaking here.
        #print(motionevent)

    Window.bind(on_motion=on_motion)

    class AttrButton(Button):
        pass

if __name__ == '__main__':
    SRNPCGen().run()
