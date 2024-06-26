from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from kivy.clock import Clock
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

    def build(self):
        game = screen1.NineGameBase()
        # спавн аппонентов, сколько аппонентов в секунду (сейчас один раз в 3 секунды)
        Clock.schedule_interval(game.spawn_apponent, 3 / 1) # в н сикунд / н раз
        # инициализация объектов
        game.serve_objects()
        # запуск основного цикла - обновляется каждую секунду
        Clock.schedule_interval(game.update, 1 / 60.0)
        Clock.schedule_interval(game.mov_player, 1 / 60.0)
        Clock.schedule_interval(game.collide_player, 1 / 60.0)
        return game


if __name__ == "__main__":
    Screen_testApp().run()