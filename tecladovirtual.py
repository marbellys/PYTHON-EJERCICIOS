from kivy import Config
Config.set('graphics', 'multisamples', '0')
import os
os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.vkeyboard import VKeyboard
class Test(VKeyboard):
    player = VKeyboard()
class VKeyboardApp(App):
    def build(self):
        return Test()
if __name__ == '__main__':
    VKeyboardApp().run()