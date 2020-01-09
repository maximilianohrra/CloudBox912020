#LIBRERIAS KIVY
import kivy
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.widget import Widget 
from kivy.uix.button import Button 
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label 
from kivy.uix.modalview import ModalView
from kivy.uix.screenmanager import FadeTransition

#CONFIGURACION PARA QUE NO SALTE EL ERROR DE OPENGL
#from kivy import Config 
#Config.set("graphics","multisamples","0")

class Wind_Pregunta(ScreenManager):
    transition = FadeTransition()
    pass

class Wind_Menu(Screen):
    transition = FadeTransition()
    pass

class Wind_Buscarjuego(Screen):
    pass

class MainApp(App):
    title= 'Cloud Box - Inicio'
    #LA FUNCION BUILD ES OBLIGATORIA PARA KIVY Y ANDROID
    def build(self):
        return Wind_Pregunta()
if __name__=='__main__':
    MainApp().run()

