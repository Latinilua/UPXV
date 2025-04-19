from kivy.app import App
from kivy.uix.label import Label

class TesteApp(App):
    def build(self):
        return Label(text='Se você está vendo isso, o Kivy está funcionando!')

if __name__ == '__main__':
    TesteApp().run()
