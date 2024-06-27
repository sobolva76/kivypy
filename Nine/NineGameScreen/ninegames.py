from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
import gamebase, gamestart, gameend


class BaseScreens(ScreenManager):
    def screen_manager_method(self):
        print('Принт из менеджера экранов')

class NineGameSApp(App):
    def app_method(self):
        print('Принт из app')


if __name__ == "__main__":
    NineGameSApp().run()