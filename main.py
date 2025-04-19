from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import StringProperty

class SelecionarTela(Screen):
    shopping = StringProperty('Selecione o shopping')
    loja = StringProperty('Selecione a loja')

    def on_pre_enter(self):
        self.shopping = 'Selecione o shopping'
        self.loja = 'Selecione a loja'
        self.ids.spinner_shopping.text = 'Selecione o shopping'
        self.ids.spinner_loja.text = 'Selecione a loja'

    def verificar_selecao(self):
        if self.shopping != 'Selecione o shopping' and self.loja != 'Selecione a loja':
            self.manager.current = 'mapa' 

class MapaTela(Screen):
    loja_info = StringProperty()

    def on_pre_enter(self):
        self.ids.info_loja.text = f"Você selecionou: {self.manager.get_screen('selecionar').shopping} - Loja {self.manager.get_screen('selecionar').loja}\nPiso 1 - Alameda Central"

class MainApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(SelecionarTela(name='selecionar'))
        sm.add_widget(MapaTela(name='mapa'))
        return sm
    
if __name__ == '__main__':
    MainApp().run()
