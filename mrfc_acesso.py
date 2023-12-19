from mfrc522 import SimpleMFRC522       #Biblioteca do RFID  
from time import sleep                  #função de delay 
import RPi.GPIO as GPIO                 #Biblioteca para gerenciamento de GPIO

GPIO.setwarnings(False)                 #Desabilita os avisos         

GPIO.setmode(GPIO.BCM)                  #Estabelece a referência dos pinos baseadas no Chip (BCM) e não na placa (Board)

leitor = SimpleMFRC522()                #Cria o objeto leitor 

GPIO.setup(20, GPIO.OUT)                #Configura o pino 20 como saída
GPIO.setup(21, GPIO.OUT)                #Configura o pino 21 como saída

acesso = False                          #inicializa a variável acesso como false


print("Chega mais perto, vai")

while True:
    #cria as variáveis "id" e "texto", e as atribui as leituras da id e do texto coletado da tag pelo leitor, respectivamente
    id,texto = leitor.read()
    
    #Checa se o ID corresponde ao ID , e printa Acesso liberado, acende um led verde e concede acesso se corresponder
    if id == 426883519919:
        print("Acesso liberado")
        acesso = True
        GPIO.output(20, True)
        sleep(2)
        GPIO.output(20, False)
    #se não, printa Acesso negado e acende um led vermelho e revoga o acesso   
    else:
        print("Acesso negado")
        acesso = False
        GPIO.output(21, True)
        sleep(2)
        GPIO.output(21, False)