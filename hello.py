#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import kivy
kivy.require('1.8.0')

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty, StringProperty
from kivy.core.window import Window

Window.size = (1120, 630)


class Hello(FloatLayout):
    '''hello.kv commence par <Hello>'''
    # Text du bouton
    info = StringProperty()

    # Text du label
    label_wid = ObjectProperty()

    def do_action(self):
        '''Si j'appuie, je fais ça.'''

        # Modifie le texte du bouton défini dans le build de HelloApp
        self.info = " : Non, c'est fini"

        # Modification du texte avec label_wid défini au début de <Hello>:
        # et utilisé pour définir le texte du Label
        self.label_wid.text = "J'ai appuyé"


class HelloApp(App):
    '''Lit Hello.kv parce que la classe s'appelle HelloApp'''
    def build(self):
        return Hello(info=" ici !")


if __name__ == "__main__":
    HelloApp().run()
