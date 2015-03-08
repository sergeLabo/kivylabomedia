#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import kivy
kivy.require('1.8.0')

from kivy.app import App
from kivy.core.window import Window

# Set window size or not with your screen resolution
Window.size = (1120, 630)


class GridlayoutApp(App):
    '''L'application principale.'''
    def build(GridLayout):
        '''Gridlayout.kv commence par "GridLayout".
        GridLayout ne prend pas size_hint_y, tous les boutons ont la même
        hauteur.
        '''
        pass

if __name__ == '__main__':
    GridlayoutApp().run()
