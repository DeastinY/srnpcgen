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
    def __init__(self, callback = None):
        super(CharacterDatabase,self).__init__()
        self.callback = callback
        layout = GridLayout(cols=1, height="70dp", font_size="15sp", spacing=10, padding=10, size_hint_y=None)
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
        try:
            for infile in os.listdir(chardir):
                with open(os.path.join(chardir,infile), "r") as char:
                    j = json.load(char)
                    c = RandChar.FromJSON(j)
                    chars.append(c)
            return chars
        except:
            return []


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
        self.b_gen = self.nav.ids.btn_generate
        self.b_db = self.nav.ids.btn_database
        self.open_generate(toggle=False)
        return self.nav

    def set_optbtn(self, tag):
        b_opt = self.nav.ids.btn_option
        if tag == "Generator":
            b_opt.text = "Save"
            b_opt.on_press = self.save
        elif tag ==  "Database":
            b_opt.text = "Export"
            b_opt.on_press = self.export

    def open_database(self, toggle=True):
        self.highlight_btn(self.b_db)
        if not type(self.main) is CharacterDatabase:
            self.open(CharacterDatabase(callback=self.show_char))
            self.set_optbtn("Database")
            if toggle:
                self.nav.toggle_state()

    def open_generate(self, toggle=True, char = None):
        self.highlight_btn(self.b_gen)
        if not type(self.main) is RandChar:
            self.open(char or RandChar())
            self.set_optbtn("Generator")
            if toggle:
                self.nav.toggle_state()

    def show_char(self, char):
        self.open_generate(toggle=False, char=char)

    def export(self):
        pass

    def save(self):
        try:
            if not os.path.exists(chardir):
                os.mkdir(chardir)
            char = self.main
            charfile = os.path.join(chardir, unicode(char.Name))
            with open(charfile, "w") as outfile:
                outfile.write(char.ToJSON())
        except:
            pass #Shitty hack for now

    def delete(self):
        try:
            char = self.main
            charfile = os.path.join(chardir, char.Name)
            os.remove(charfile)
        except:
            pass #Shitty hack for now

    def open(self, main):
        if self.main:
            self.nav.ids.main.remove_widget(self.main)
        self.main = main
        self.nav.ids.main.add_widget(self.main)

    def highlight_btn(self, btn):
        for b in [self.b_gen, self.b_db]:
            b.color = [1,1,1,1]
            b.font_size = "15sp"
        if btn:
            btn.color = [0,1,0,1]
            btn.font_size = "20sp"

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
