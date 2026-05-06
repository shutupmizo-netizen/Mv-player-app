# Build trigger
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.window import Window
Window.clearcolor=(0.05,0.07,0.1,1)
class MusicApp(App):
    def build(self):
        box=BoxLayout(orientation='vertical',padding=20,spacing=20)
        title=Label(text='MV Player',font_size='30sp',size_hint_y=0.3)
        btn=Button(text='Play',size_hint_y=0.2,background_color=(0.1,0.5,1,1))
        box.add_widget(title)
        box.add_widget(btn)
        return box
if __name__=='__main__':MusicApp().run()
