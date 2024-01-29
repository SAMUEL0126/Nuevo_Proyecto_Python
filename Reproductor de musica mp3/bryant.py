import pygame


from gtts import gTTS
import pygame
from io import BytesIO

pygame.init()

#Funcion mandar mensaje de audio
def say(text):
    tts = gTTS(text=text, lang='en')
    fp = BytesIO()
    tts.write_to_fp(fp)
    fp.seek(0)
    pygame.mixer.init()
    pygame.mixer.music.load(fp)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

say("Como seria lo mas grosero del pedazo")

def reproducir_cancion(cancion):
    pygame.mixer.init()
    pygame.mixer.music.load(cancion)
    pygame.mixer.music.play()

def pausar_cancion():
    pygame.mixer.music.pause()

def continuar_cancion():
    pygame.mixer.music.unpause()

def detener_cancion():
    pygame.mixer.music.stop()

if __name__ == '__main__':
    cancion = 'Reproductor de musica mp3/videoplayback.m4a' # Ruta de la canción que quieres reproducir
    reproducir_cancion(cancion)

    while True:
        comando = input("Ingrese 'pausar', 'continuar' o 'detener': ")

        if comando == 'pausar':
            pausar_cancion()
        elif comando == 'continuar':
            continuar_cancion()
        elif comando == 'detener':
            detener_cancion()
            break
