#! /usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Ce script décrit:
* les interactions avec les fichiers py et kv,
* les héritages des class
* les méthodes qu'il faut utiliser.
'''


from kivy.app import App
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout

class CustomDropDown(DropDown):
    '''Lit <CustomDropDown>: dans exemple_simple.kv'''
    pass


class DropdownDemo(FloatLayout):
    '''Le code de l'application proprement dite.'''
    def __init__(self, **kwargs):
        '''Le bouton présent à l'ouverture de la fenêtre est créé ici,
        pas dans kv
        '''
        super(DropdownDemo, self).__init__(**kwargs)
        self.dropdown = CustomDropDown()
        # Création d'un widget bouton
        self.mainbutton = Button(text='Etes-vous poli ou mal poli?',
                                 size_hint_x=0.6, size_hint_y=0.15)
        # Ajout du bouton au FloatLayout donc hérite cette class
        self.add_widget(self.mainbutton)
        # Ajout des actions
        # Si clic
        self.mainbutton.bind(on_release=self.dropdown.open)
        # root.select appelle on_select
        self.dropdown.bind(on_select=lambda\
                           instance, x: setattr(self.mainbutton, 'text', x))
        self.dropdown.bind(on_select=self.callback)

    def callback(self, instance, x):
        '''x est self.mainbutton.text actualisé'''
        print("Le mode choisi est: {0}".format(x))


class Exemple_simpleApp(App):
    '''La fonction build retourne root,
    ici root = DropdownDemo().
    root ne peut être appelé que dans le fichier kv.
    '''
    def build(self):
        return DropdownDemo()


if __name__ == '__main__':
    '''La class s'appelle Exemple_simpleApp() parce que le fichier *.kv
    s'appelle exemple_simple.kv, soit:
        * Majuscule au début
        * App à la fin
    '''
    Exemple_simpleApp().run()
