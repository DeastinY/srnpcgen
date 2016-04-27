#!/usr/bin/python
# -*- coding: latin-1 -*-
from plyer import accelerometer
from chargen.randchar import RandChar

import kivy
kivy.require('1.9.0')

from kivy.app import App
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget

class SRNPCGen(App):
    def __init__(self):
        super(SRNPCGen, self).__init__()
        self.initialize_accelerometer()

    def initialize_accelerometer(self):
        try:
            accelerometer.enable()
        except NotImplementedError:
            self.has_accelerometer = False
        else:
            self.has_accelerometer = True
            Clock.schedule_interval(self.get_acceleration, 1/20.)

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
            try:
                val = accelerometer.acceleration[:3]
                if not val == (None,None,None):
                    print(val)
            except Exception:
                print("Accelerometer not available")

if __name__ == '__main__':
    SRNPCGen().run()
