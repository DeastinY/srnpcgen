#!/usr/bin/python
# -*- coding: latin-1 -*-
from chargen import chargen
from plyer import accelerometer

import kivy
kivy.require('1.9.0')

from kivy.app import App
from kivy.core.window import Window
from kivy.clock import Clock
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
        Clock.schedule_interval(self.get_acceleration, 1/20.)

    def get_acceleration(self, dt):
        try:
            val = accelerometer.acceleration[:3]
            if not val == (None,None,None):
                print(val)
        except Exception:
            print("Accelerometer not available")

    class AttrButton(Button):
        pass

if __name__ == '__main__':
    SRNPCGen().run()
