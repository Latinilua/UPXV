from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import StringProperty, ListProperty
from kivy.uix.spinner import Spinner
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.clock import Clock

class InicioScreen(Screen):
    def on_enter(self, *args):
        Clock.schedule_once(self.go_to_main_screen, 3)

    def go_to_main_screen(self, dt):
        self.manager.current = 'selecionar_shopping'

class SelecionarShopping(Screen):
    shopping_selecionado = StringProperty('Selecione o shopping')
    shoppings = ListProperty(['Shopping Multiverso'])

    def avancar_para_lojas(self):
        if self.shopping_selecionado != 'Selecione o shopping':
            selecionar_loja_screen = self.manager.get_screen('selecionar_loja')
            selecionar_loja_screen.shopping = self.shopping_selecionado
            self.manager.current = 'selecionar_loja'

class SelecionarLoja(Screen):
    shopping = StringProperty('')
    loja = StringProperty('Selecione a loja')
    opcoes_loja = ListProperty([])

    def on_enter(self):
        self.loja = 'Selecione a loja'
        self.ids.spinner_loja.text = 'Selecione a loja'
        self.atualizar_opcoes_loja(self.shopping)

    def atualizar_opcoes_loja(self, shopping):
        self.shopping = shopping
        todas_as_lojas = ['Stark Tech & Gadgets', 'Asgardian Fashion', 'Wakanda Forever Fabrics',
                          'Pym Particles Miniatures', 'Captains Vintage', 'Guardians Galactic Goods',
                           'Pym Particles', 'Widows Warb Security', 'Sanitários']
        self.opcoes_loja = todas_as_lojas
        self.ids.spinner_loja.values = self.opcoes_loja

    def verificar_selecao(self):
        if self.loja != 'Selecione a loja':
            mapa_screen = self.manager.get_screen('mapa')
            mapa_screen.shopping = self.shopping
            mapa_screen.loja = self.loja
            self.manager.current = 'mapa'

class MapaTela(Screen):
    loja_info = StringProperty()
    mapa_source = StringProperty('mapa_shopping.jpg')
    shopping = StringProperty('')
    loja = StringProperty('')

    def on_pre_enter(self):
        self.atualizar_mapa(self.shopping, self.loja)

    def atualizar_mapa(self, shopping, loja):
        mapa_lojas = {
            'Stark Tech & Gadgets': 'L1.jpg',
            'Asgardian Fashion': 'L2.jpg',
            'Wakanda Forever Fabrics': 'L3.jpg',
            'Pym Particles Miniatures': 'L4.jpg',
            'Captains Vintage': 'L5.jpg',
            'Guardians Galactic Goods': 'L6.jpg',
            'Pym Particles': 'L7.jpg',
            'Widows Warb Security': 'L9.jpg',
            'Sanitários': 'L10.jpg'
        }
        if loja in mapa_lojas:
            self.mapa_source = mapa_lojas[loja]
        else:
            self.mapa_source = 'mapa_shopping.jpg'

class MainApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(InicioScreen(name='inicio_screen'))
        sm.add_widget(SelecionarShopping(name='selecionar_shopping'))
        sm.add_widget(SelecionarLoja(name='selecionar_loja'))
        sm.add_widget(MapaTela(name='mapa'))
        sm.current = 'inicio_screen'
        return sm

if __name__ == '__main__':
    MainApp().run()
