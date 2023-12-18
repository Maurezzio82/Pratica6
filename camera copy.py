#!/usr/bin/python3
import cv2 # Biblioteca OpenCV
import os # Biblioteca para operações do sistema
import time # Biblioteca de tempo
import RPi.GPIO as GPIO
from time import sleep
from picamera2 import Picamera2 # Biblioteca da câmera da Raspberry Pi

flag = 0

GPIO.setmode (GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(26,GPIO.OUT) #setagem do LED

# Carrega o classificador para detecção facial (informar o caminho do arquivo)
face_detector = cv2.CascadeClassifier("/home/sel/Desktop/haarcascade_frontalface_default.xml")
# Inicia uma thread para gerenciar janelas de visualização
cv2.startWindowThread()
# Inicializa a câmera da Raspberry Pi
picam2 = Picamera2()
# Configura a câmera para criar uma visualização com formato de representação
# de cores 32 bits “XRGB8888” e resolução de 640x480 pixels
picam2.configure(picam2.create_preview_configuration(main={"format":'XRGB8888', "size": (640, 480)}))
# Inicia a câmera
picam2.start()
# Define o diretório onde as imagens com rostos detectados serão armazenadas
output_directory = "detected_faces"
# Cria o diretório, se ele não existir
os.makedirs(output_directory, exist_ok=True)
# Loop para captura e detecção de rostos
while True:
# Captura um quadro da câmera e armazena na variável
    im = picam2.capture_array()
# Converte a imagem colorida para escala de cinza
    grey = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
# Usa o classificador em cascata para detectar rostos na imagem em escala de cinza
    faces = face_detector.detectMultiScale(grey, 1.1, 5)
# Loop para processar cada rosto detectado
    for (x, y, w, h) in faces:
# Desenha um retângulo verde ao redor do rosto na imagem original
        cv2.rectangle(im, (x, y), (x + w, y + h), (0, 255, 0))
        cv2.putText(im, "Quis es?", (x, y), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 1.0, (65, 159, 96), 4)
# Gera um nome de arquivo único com base no carimbo de data/hora
        timestamp = int(time.time())
        filename = os.path.join(output_directory, f"face_{timestamp}.jpg")
        GPIO.output(26,GPIO.HIGH)
        flag = 1
        i = 0
        print ("Rosto Detectado")
        
# Salva apenas a porção da imagem que contém o rosto detectado como um arquivo JPEG
        cv2.imwrite(filename, im[y:y+h, x:x+w])
        
    if flag == 1:
        i=i+1
        if i >= 10:
            GPIO.output(26,GPIO.LOW)
            flag = 0
# Exibe a imagem com os retângulos desenhados em uma janela com o título "Camera"
    cv2.imshow("Camera", im)

    
# Aguarda 1 milissegundo antes de continuar o loop e capturar a próxima imagem
    cv2.waitKey(1)
