#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import kivy
kivy.require('1.8.0')

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.carousel import Carousel

class MainScreen(Screen):
    pass

class Screen1(Screen):
    pass

class Screen2(Screen):
    pass

class Screen3(Screen):
    pass

class Screen4(Screen):
    pass

class SettingsScreen(Screen):
    pass

class JsonScreen(Screen):
    pass

class OpenScreen(Screen):
    pass

SCREENS = { 0: (MainScreen,       "Menu"),
            1: (Screen1,          "Ecran 1"),
            2: (Screen2,          "Ecran 2"),
            3: (Screen3,          "Ecran 3"),
            4: (Screen4,          "Ecran 4"),
            5: (SettingsScreen,   "Options"),
            6: (JsonScreen,       "Texte libre"),
            7: (OpenScreen,       "Page libre")
           }

class Carousel_1App(App):
    def build(self):
        carousel = Carousel(direction='right')
        for i in range(8):
            carousel.add_widget(SCREENS[i][0](name=SCREENS[i][1]))
        return carousel


if __name__ == '__main__':
    Carousel_1App().run()
