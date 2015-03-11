#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from kivy.app import App
from kivy.uix.widget import Widget

class PongGame(Widget):
    pass

class Ping_pongApp(App):
    def build(self):
        return PongGame()

if __name__ == "__main__":
    Ping_pongApp().run()
