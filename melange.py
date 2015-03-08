#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import kivy
kivy.require('1.8.0')

from kivy.app import App
from kivy.core.window import Window

# Set window size or not with your screen resolution
Window.size = (1120, 630)


class MelangeApp(App):
    '''L'application principale.'''
    def build(FloatLayout):
        '''Melange.kv commence par "GridLayout".
        FloatLayout n'a pas d'arguments.
        '''
        pass

if __name__ == '__main__':
    MelangeApp().run()
