from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.config import Config
from kivy.clock import Clock

import RPi.GPIO as GPIO
import time

started = time.time()

# GPIO setup
solenoid1Pin = 11
GPIO.setmode(GPIO.BOARD)
GPIO.setup(solenoid1Pin, GPIO.OUT)

#Positions
left=2
center=7
right=12

#Initialization
pwm=GPIO.PWM(11,50)
pwm.start(0)

class lockerGUI(App):
    def build(self):
        self.window = GridLayout()
        
        # add widgets to window
        
        # image widget
        self.testImage = Image(source="ws3hvk2cimeqj8z79gy1xf2fkp5g4g.png",pos=(100,368),size=(400,400))
        self.window.add_widget(self.testImage)
        
        # label widget
        #self.testText = Label(text="this is a test",pos=(300,300))
        #self.window.add_widget(self.testText)
        
        # button widget
        self.testButton = Button(text="UNLOCK",bold=True,size=(350,80),pos=(125,250))
        self.testButton.bind(on_press=self.testButtonAction)
        self.window.add_widget(self.testButton)
        
        return self.window
    
    def testButtonAction(self,instance):
        time.sleep(0.5)
        self.testButton.text = "UNLOCKED"
        pwm.ChangeDutyCycle(left) # Left - 90 deg position
        time.sleep(2)
        pwm.ChangeDutyCycle(right) # Right +90 position
    
Config.set("graphics",'width','600')
Config.set("graphics",'height','1024')
Config.set('graphics', 'fullscreen', 'auto')

if __name__ == "__main__":
    lockerGUI().run()
