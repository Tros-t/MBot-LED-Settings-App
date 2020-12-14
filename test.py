from lib.mBot import *
import sys
import kivy 
from kivy.app import App 
from kivy.uix.label import Label 
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout

def reset(lol):
    if lol == True:
        man = True
def best():

    def light(r, b, g):
        bot = mBot()
        bot.startWithSerial('COM3')
        while True:
            bot.doRGBLedOnBoard(0, r, b, g)

    
    # Replace this with your  
    # current version 
    kivy.require('1.11.1')   

    class Layout(GridLayout):
        def __init__(self, **kwargs):
            super(Layout, self).__init__(**kwargs)

            self.rows = 2

            self.red = TextInput(multiline=False)
            self.add_widget(self.red)
            self.red.text = '250'

            self.green = TextInput(multiline=False)
            self.add_widget(self.green)
            self.green.text = '0'

            self.blue = TextInput(multiline=False)
            self.add_widget(self.blue)
            self.blue.text = '0'

            self.stat = Label(text="R=0 G=0 B=0")
            self.add_widget(self.stat)

            self.up = Button(text="Update LED Lights !", font_size=35)
            self.up.bind(on_press=self.upd)
            self.add_widget(self.up)

            self.err = Label(text="Error Display")
            self.add_widget(self.err)

        def upd(self, instance):

            redi = int(self.red.text)
            greeni = int(self.green.text)
            bluei = int(self.blue.text)
            light(redi, greeni, bluei)

            reset(True)

    # Defining a class 
    class MBotLedSettings(App): 
        def build(self): 
            l = Layout()
            return l        
    
    if __name__ == "__main__":
        MBotLedSettings().run() 


best()
