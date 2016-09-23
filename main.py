from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

from kivy.uix.widget import Widget
from kivy.graphics import Line

class Drawer(Widget):
    def on_touch_down(self, touch):
        with self.canvas:
            touch.ud["line"] = Line(Points=(touch.x,touch.y))

    def on_touch_move(self, touch):
        touch.ud["line"].points += (touch.x,touch.y)

class MainScreen(Screen):
    pass

class AnotherScreen(Screen):
    pass

class ScreenManagement(ScreenManager):
    pass


presentation = Builder.load_file("FirstKivy.kv")

class FirstKivy(App):
    def build(self):
        return presentation


if __name__ == "__main__":
    FirstKivy().run();
