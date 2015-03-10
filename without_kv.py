#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.lang import Builder

Builder.load_string('''
<Withoutkv>:
    Button:
        text: "bla bla !"
''')

class Withoutkv(FloatLayout):
    pass

class TestApp(App):
    def build(self):
        return Withoutkv()

if __name__ == '__main__':
    TestApp().run()
