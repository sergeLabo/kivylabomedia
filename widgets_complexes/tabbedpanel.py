#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from kivy.app import App
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder

Builder.load_string("""

<Test>:
    size_hint: .5, .5
    pos_hint: {'center_x': .5, 'center_y': .5}
    do_default_tab: False

    TabbedPanelItem:
        text: 'Onglet 1'
        Label:
            text: "Label dans l'onglet"
    TabbedPanelItem:
        text: 'Onglet 2'
        BoxLayout:
            Label:
                text: 'Un label est ici'
            Button:
                text: 'Bouton qui ne fait rien'
    TabbedPanelItem:
        text: 'Onglet 3'
        RstDocument:
            text: '\\n'.join(("Ceci est un RSTDocument"))

""")


class Test(TabbedPanel):
    pass


class TabbedPanelApp(App):
    def build(self):
        return Test()

if __name__ == '__main__':
    TabbedPanelApp().run()
