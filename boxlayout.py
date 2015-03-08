#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import kivy
kivy.require('1.8.0')

from kivy.app import App
from kivy.core.window import Window

# Set window size or not with your screen resolution
Window.size = (1120, 630)

class BoxlayoutApp(App):
    '''L'application principale.'''
    def build(FloatLayout):
        '''Boxlayout.kv commence par "BoxLayout"
        BoxLayout ne prend pas cols et rows, seulement horizontal ou vertical.
        Cette fonction build construit sur un FloatLayout.
        '''
        pass

if __name__ == '__main__':
    BoxlayoutApp().run()
