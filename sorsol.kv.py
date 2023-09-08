# Spinner
from kivy.config import Config
Config.set('graphics','width',500)
Config.set('graphics','height',800)
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder
import random
from numpy import random as nprand


Builder.load_string("""
<Szamolo>:
	lab2: lab2
	sp1: sp1
    Label:
		size_hint: .3, .2        
		pos_hint: {'x': 0.2,'y':0.7}
		text: 'max.'
        font_size: 60 
    Spinner: 
        id: sp1
        size_hint: .3, .2        
		pos_hint: {'x': 0.55,'y':0.7}
        text: "6"	        
        values:'4','6','12','20','35','45','50','80','90'
		font_size: 50  
		on_text: root.szamol()  	                           
    Button:
        text: "Sorsol"
        font_size: 60
        background_color: 'blue'
        size_hint: .6, .2        
        pos_hint: {'x': 0.2,'y':0.4}    
        on_press: root.szamol()                   
    Label:
		id: lab2
        text: "Press Sorsol !"  
        font_size: 80  
        color: 'red'     
        size_hint: .6, .3
        pos_hint: {'x': 0.2,'y':0}
""")

class Szamolo(FloatLayout):
	def szamol(self):
		maxszam=int(self.sp1.text)
		number=random.randint(1,maxszam)  #  1-maxszam közötti véletlen szám
		number2=nprand.randint(maxszam)+1
		self.lab2.text =str(number) + '  ' + str(number2) 
	
class MainApp(App):
    def build(self):
        return Szamolo()

if __name__ == '__main__':
    app = MainApp()
    app.run()
