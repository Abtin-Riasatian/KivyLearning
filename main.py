from kivy.app import App
# from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout

class FirstKivy(App):
    def build(self):
        return FloatLayout()


if __name__ == "__main__":
    FirstKivy().run();
