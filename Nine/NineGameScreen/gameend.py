from kivy.uix.screenmanager import Screen

class GameEndScreen(Screen):
    """ Класс окончания игры """
    print("gameend")

    # функция запускается призагрузке скрина
    def on_enter(self, *args):
        print("on_enter - gameend")

    # функция запускается после выхода из скрина
    def on_leave(self, *args):
        print("on_leavel - gameend")