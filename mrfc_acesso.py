from mfrc522 import SimpleMFRC522
from time import sleep
import RPi.GPIO as GPIO

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)

leitor = SimpleMFRC522()

GPIO.setup(20, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)

acesso = False


print("Chega mais perto, vai")

while True:
    id,texto = leitor.read()
    
    if id == 426883519919:
        print("Acesso liberado")
        acesso = True
        GPIO.output(20, True)
        sleep(2)
        GPIO.output(20, False)
        
    else:
        print("Acesso negado")
        acesso = False
        GPIO.output(21, True)
        sleep(2)
        GPIO.output(21, False)