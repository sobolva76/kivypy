from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
import screen1, screen2, screen3

# hierarhy:
#   ScreensSample (App)
#   |- MyScreens (ScreenManager)
#      |- MyScreen1 (Screen)
#      |- MyScreen2 (Screen)
#      |- MyScreen3 (Screen)

class MyScreens(ScreenManager):
    def screen_manager_method(self):
        print('Hello from screen manager')

class Screen_testApp(App):
    def app_method(self):
        print('Hello from app')


if __name__ == "__main__":
    Screen_testApp().run()