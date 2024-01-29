import pygame

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
    cancion = '/Reproductor de musica de bryant myers/[yt-mp3.blog] Juhn _Apaga El Celular_ Feat Bryant Myers [Video Oficia].mp3' # Ruta de la canción que quieres reproducir
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
