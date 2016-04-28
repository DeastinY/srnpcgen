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

from kivy.garden.navigationdrawer import NavigationDrawer

class SRNPCGen(App):
    def __init__(self):
        super(SRNPCGen, self).__init__()
        self.initialize_accelerometer()

    def build(self):
        navigationdrawer = NavigationDrawer()
        navigationdrawer.anim_type = 'slide_above_anim'

        side_panel = BoxLayout(orientation='vertical')
        side_panel.add_widget(Label(text='Some cool text'))
        side_panel.add_widget(Button(text='A button'))
        side_panel.add_widget(Button(text='Another button'))
        navigationdrawer.add_widget(side_panel)
        navigationdrawer.add_widget(RandChar())

        navigationdrawer.toggle_state()

        return navigationdrawer


    def initialize_accelerometer(self):
            if accelerometer.enable():
                print("Accelerometer activated")
                self.has_accelerometer = True
                Clock.schedule_interval(self.get_acceleration, 1/20.)
            else:
                print("Accelerometer not available")
                self.has_accelerometer = False


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
