#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import kivy
kivy.require('1.8.0')

from kivy.app import App
from kivy.uix.carousel import Carousel
from kivy.factory import Factory

class Example1(App):

    def build(self):
        carousel = Carousel(direction='right')
        for i in range(4):
            src = "http://placehold.it/480x270.png&text=slide-%d&.png" % i
            image = Factory.AsyncImage(source=src, allow_stretch=True)
            carousel.add_widget(image)
        return carousel

Example1().run()
