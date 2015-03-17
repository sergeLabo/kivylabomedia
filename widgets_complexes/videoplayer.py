#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from kivy.app import App
from kivy.uix.videoplayer import VideoPlayer
from kivy.uix.floatlayout import FloatLayout

class Test(VideoPlayer, FloatLayout):
    player = VideoPlayer(source="softboy.avi", state='play')

class VideoplayerApp(App):
    def build(self):
        return Test()

if __name__ == '__main__':
    VideoplayerApp().run()
