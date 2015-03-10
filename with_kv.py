#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout

class Withkvtest(FloatLayout):
    pass

class With_kvApp(App):
    def build(self):
        # Retourne le widget root
        return Withkvtest()

if __name__ == '__main__':
    With_kvApp().run()
