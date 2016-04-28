#!/usr/bin/python
# -*- coding: latin-1 -*-
from plyer import accelerometer
from chargen.randchar import RandChar

import kivy
kivy.require('1.9.0')

from kivy.app import App
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.metrics import dp
from kivy.graphics import *

from kivy.garden.navigationdrawer import NavigationDrawer

class CustomNavigationDrawer(NavigationDrawer):
    pass

class SRNPCGen(App):
    def __init__(self):
        super(SRNPCGen, self).__init__()
        self.initialize_accelerometer()
        self.main = None

    def initialize_accelerometer(self):
            if accelerometer.enable():
                print("Accelerometer activated")
                self.has_accelerometer = True
                Clock.schedule_interval(self.get_acceleration, 1/20.)
            else:
                print("Accelerometer not available")
                self.has_accelerometer = False

    def build(self):
        self.nav = CustomNavigationDrawer()
        self.open_generator()
        return self.nav

    def menu_btn_pressed(self):
        btns = [self.nav.ids.btn_generate,self.nav.ids.btn_database]
        for b in btns:
            b.color=[1,1,1,1]
            b.font_size=15

    def open_generator(self):
        if not self.main is RandChar:
            self.highlight_btn(self.nav.ids.btn_generate)
            if self.main:
                self.nav.ids.main.remove_widget(self.main)
            self.main = RandChar()
            self.nav.ids.main.add_widget(self.main)

    def highlight_btn(self, btn):
        btn.color=[0,1,0,1]
        btn.font_size=20

    def on_pause(self):
        Clock.unschedule(self.get_acceleration)
        if self.has_accelerometer:
            accelerometer.disable()

    def on_resume(self):
        if self.has_accelerometer:
            Clock.schedule_interval(self.get_acceleration, 1/20.)
            accelerometer.enable()

    def get_acceleration(self, dt):
        if self.has_accelerometer:
            print("adornes")
            try:
                val = accelerometer.acceleration[:3]
                if not val == (None,None,None):
                    print(val)
            except Exception:
                pass

if __name__ == '__main__':
    SRNPCGen().run()
