from kivy.app import App
# from kivy.uix.label import Label
from kivy.uix.widget  import Widget

class TouchInput(Widget):
    def on_touch_down(self, touch):
        print("touch down" , touch)

    def on_touch_up(self, touch):
        print("touch up" , touch)

    def on_touch_move(self, touch):
        print ("touch move" , touch)

class FirstKivy(App):
    def build(self):
        return TouchInput()


if __name__ == "__main__":
    FirstKivy().run();
