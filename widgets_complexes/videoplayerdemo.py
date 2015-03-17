#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import kivy
kivy.require('1.8.0')

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.videoplayer import VideoPlayer

parent = Widget()
parent.size = 400, 300

class MyApp(App):
    def build(self):
        button = Button(text='Video Player', font_size=14)
        button.size = 400, 300
        button.bind(on_press=on_button_press)
        parent.add_widget(button) #add button
        return parent

def on_button_press(self):
        video= VideoPlayer(source='softboy.avi', state='play',
                           options={'allow_fullscreen': True})
        parent.add_widget(video) #add videoplayer
        return parent

if __name__ == '__main__':
    MyApp().run()
