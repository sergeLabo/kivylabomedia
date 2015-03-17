#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import kivy
kivy.require('1.8.0')

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager, Screen

class MenuScreen(Screen):
    '''Lit <MenuScreen>: dans kv soit:
    <MenuScreen>:
        BoxLayout:
            Button:
                text: 'Définir les options'
                on_press: root.manager.current = 'Options'
            Button:
                text: 'Quitter'
    '''
    pass

class SettingsScreen(Screen):
    # Lit <SettingsScreen>: dans kv
    pass

class ScreenmanagerApp(App):
    def build(self):
        sm = ScreenManager()
        # Appel de la classe qui lit kv
        sm.add_widget(MenuScreen(name='Menu'))
        # Appel de la classe qui lit kv
        sm.add_widget(SettingsScreen(name='Options'))
        # Retourne root = sm
        return sm

if __name__ == '__main__':
    ScreenmanagerApp().run()
