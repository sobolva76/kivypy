# File name: settings.py

import kivy
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty


class PlayerCount(BoxLayout):
    count_text = StringProperty("")


class PlayerSettings(BoxLayout):
    label_text = StringProperty("")


class SettingsScreen(Screen):
    pass