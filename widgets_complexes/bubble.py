#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.bubble import Bubble
from kivy.properties import ObjectProperty

class Cut_copy_paste(Bubble):
    pass

class BubbleDemo(FloatLayout):

    def __init__(self, **kwargs):
        super(BubbleDemo, self).__init__(**kwargs)
        self.but_bubble = Button(text='Press to show bubble')
        self.but_bubble.bind(on_release=self.show_bubble)
        self.add_widget(self.but_bubble)
        self.bubb = Cut_copy_paste()

    def show_bubble(self, *l):
        if not hasattr(self, 'self.bubb'):
            self.add_widget(self.bubb)
        else:
            values = ('left_top', 'left_mid', 'left_bottom', 'top_left',
                'top_mid', 'top_right', 'right_top', 'right_mid',
                'right_bottom', 'bottom_left', 'bottom_mid', 'bottom_right')
            index = values.index(self.bubb.arrow_pos)
            self.bubb.arrow_pos = values[(index + 1) % len(values)]

class BubbleApp(App):
    def build(self):
        return BubbleDemo()

if __name__ == '__main__':
    BubbleApp().run()
