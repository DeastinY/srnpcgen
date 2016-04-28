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
        self.navigationdrawer = NavigationDrawer()
        self.side_panel = GridLayout(cols=1,rows=3)
        self.main_panel = GridLayout(cols=1,rows=2, padding=[0,10,0,0])
        m = self.main_panel
        nav = self.navigationdrawer
        s = self.side_panel

        nav.anim_type = 'slide_above_anim'

        s.add_widget(Button(text='Generate', height=70, size_hint_y=None))
        s.add_widget(Button(text='Database', height=70, size_hint_y=None))
        text = Label(text='Hier würde jetzt cooler text stehen, wenn mir denn was einfallen würde. \
                     Oder ein Bild, oder so. kA. Wenn ihr ideen habt, nur raus damit :D ')
        text.text_size=(text.width,None)
        text.valign='middle'
        text.halign='center'
        s.add_widget(text)

        top_bar = GridLayout(cols=2, rows=1, height=50, size_hint_y=None, padding=[10,0,10,0])
        top_bar.add_widget(Button(text="Menu", on_press=self.toggle_drawer, width=50, size_hint_x=None))
        top_bar.add_widget(Label(text = "Roll Your NPC", font_size=30, italic=True))

        m.add_widget(top_bar)
        m.add_widget(RandChar())
        # First : Side, Second : Main
        nav.add_widget(s)
        nav.add_widget(m)

        return nav

    def toggle_drawer(self, sender):
        self.navigationdrawer.toggle_state()


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
