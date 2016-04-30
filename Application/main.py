#!/usr/bin/python
# -*- coding: latin-1 -*-
import os
import json
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
from kivy.uix.scrollview import ScrollView
from kivy.uix.widget import Widget
from kivy.metrics import dp
from kivy.graphics import *

from kivy.garden.navigationdrawer import NavigationDrawer

curdir = unicode(os.path.dirname(os.path.realpath(__file__)))
chardir = unicode(os.path.join(curdir, u"chars"))

class CustomNavigationDrawer(NavigationDrawer):
    pass

class CharacterDatabase(ScrollView):
    def __init__(self, callback):
        super(CharacterDatabase,self).__init__()
        self.callback = callback
        layout = GridLayout(cols=1, height=70, font_size=15, spacing=10, padding=10, size_hint_y=None)
        # Make sure the height is such that there is something to scroll.
        layout.bind(minimum_height=layout.setter('height'))
        self.chars = self.load_chars()
        for c in self.chars:
            btn = Button(text=c.Name, size_hint_y=None, height=40)
            btn.bind(on_press=self.btn_pressed)
            layout.add_widget(btn)
        self.add_widget(layout)

    def btn_pressed(self, btn):
        for c in self.chars:
            if c.Name == btn.text:
                self.callback(c)

    def load_chars(self):
        chars = []
        for infile in os.listdir(chardir):
            with open(os.path.join(chardir,infile), "r") as char:
                j = json.load(char)
                c = RandChar.FromJSON(j)
                chars.append(c)
        return chars


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
        self.menu_btn_pressed(toggle=False)
        return self.nav

    def menu_btn_pressed(self, toggle=True, char=None):
        b_gen = self.nav.ids.btn_generate
        b_db = self.nav.ids.btn_database
        for b in [b_gen, b_db]:
            b.color = [1,1,1,1]
            b.font_size = 15
        if type(self.main) is RandChar:
            self.open(CharacterDatabase(callback=self.show_char),b_db)
            self.set_optbtn("Database")
        else:
            self.open(char or RandChar(),b_gen)
            self.set_optbtn("RandChar")
        if toggle:
            self.nav.toggle_state()

    def set_optbtn(self, tag):
        b_opt = self.nav.ids.btn_option
        if tag == "RandChar":
            b_opt.text = "Save"
            b_opt.on_press = self.save
        else:
            b_opt.text = "Export"
            b_opt.on_press = self.export

    def show_char(self, char):
        self.menu_btn_pressed(toggle=False, char=char)

    def export(self):
        pass

    def save(self):
        if not os.path.exists(chardir):
            os.mkdir(chardir)
        char = self.main
        charfile = os.path.join(chardir, unicode(char.Name))
        with open(charfile, "w") as outfile:
            outfile.write(char.ToJSON())

    def delete(self):
        char = self.main
        charfile = os.path.join(chardir, char.Name)
        os.remove(charfile)

    def open(self, main, btn):
        if not self.main is type(main):
            self.highlight_btn(btn)
            if self.main:
                self.nav.ids.main.remove_widget(self.main)
            self.main = main
            self.nav.ids.main.add_widget(self.main)

    def highlight_btn(self, btn):
        if btn:
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
            try:
                val = accelerometer.acceleration[:3]
                if not val == (None,None,None):
                    print(val)
            except Exception:
                pass

if __name__ == '__main__':
    SRNPCGen().run()
