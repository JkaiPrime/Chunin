from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.popup import Popup
class pg(GridLayout):
       
    def calculo(self, instance):
        try:
            num1 = float(self.number1.text)
            num2 = float(self.number2.text)
            resultado = (num1 * num2) * 0.2
            self.show_result(resultado)
        except ValueError:
            self.show_error_message("Digite apenas números nos campos!")
    
    def show_result(self, resultado):
        popup = Popup(title='Resultado',
                      content=Label(text=str(resultado)),
                      size_hint=(None, None), size=(200, 100))
        popup.open()
    def show_error_message(self, mensagem):#função do pop up de erro
        popup = Popup(title='Erro',#criação do pop up e definindo o mesmo
                      content=Label(text=mensagem),
                      size_hint=(None, None), size=(500, 100))
        popup.open()    



    def __init__(self, **kwargs):
        super(pg, self).__init__(**kwargs)
        Window.size = (700, 150)# definindo o tamanho da janela
        self.cols = 2 #colunas
        self.rows = 3# numero de linas
        #1 Input e label
        _N1 = Label(text="Digite a quantidade de mês que falta ->", color = (220, 20, 60, 1))
        self.add_widget(_N1)
        self.number1 = TextInput(multiline=False)
        self.add_widget(self.number1)
        #2 Input e label
        _N2 = Label(text="Digite o valor da mensalida(digite . ao inves de ,) ->",color=(220, 20, 60, 1))
        self.add_widget(_N2)
        self.number2 = TextInput(multiline=False)
        self.add_widget(self.number2)
        #butão da operação.
        btn = Button(text="Calcular", on_press=self.calculo)
        self.add_widget(btn)
        
class MyApp(App):
    #classe do app quando instanciar vai chamar outra classe
    def build(self):
        return pg()


if __name__ == '__main__':
    MyApp().run()# instanciando o app