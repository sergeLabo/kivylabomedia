#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import kivy
kivy.require('1.8.0')

from kivy.app import App
from kivy.core.window import Window

Window.size = (1120, 630)


class MelangeApp(App):
    def build(FloatLayout):
        pass

if __name__ == '__main__':
    MelangeApp().run()
