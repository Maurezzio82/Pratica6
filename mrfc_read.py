from mfrc522 import SimpleMFRC522
from time import sleep
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
leitor = SimpleMFRC522()
print("Aproxime a tag do leitor para leitura.")
while True: 
    id,texto = leitor.read()
    print("ID: {}\nTexto: {}".format(id, texto))
    sleep(3)

#desabilitar os avisos


#cria o objeto "leitor" para a instância "SimpleMFRC522" da biblioteca
#loop

#cria as variáveis "id" e "texto", e as atribui as leituras da id e do texto coletado da tag pelo leitor, respectivamente

#exibe as informações coletadas

#aguarda 3 segundos para nova leitura


#O ID da Tag é 426883519919