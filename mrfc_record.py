import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
GPIO.setwarnings(False)

leitor = SimpleMFRC522()

texto = "SEL0630/5467"
print("Aproxime a tag do leitor para gravar.")
leitor.write(texto) 
print("Concluído!")




#desabilita os avisos

#cria o objeto "leitor" para a instância "SimpleMFRC522" da biblioteca

#criacao da variavel que armazena o texto que será gravado na tag
 #altere para o texto que deseja gravar
#escreve a tag assim que ela for aproximada do leitor, e informa a conclusão
#função que realiza a gravação do texto configurado