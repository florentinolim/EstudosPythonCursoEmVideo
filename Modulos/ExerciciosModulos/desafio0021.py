#Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.
#pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org pygame -vvv
#import pygame
#pygame.init()
#pygame.mixer.music.load('ex021.mp3')
#pygame.mixer.music.play()
#pygame.event.wait()


#import pygame
#pygame.mixer.init()
#pygame.init()
#pygame.mixer.music.load('ex021.mp3')
#pygame.mixer.music.play()
#pygame.event.wait()

from pygame import mixer
mixer.init()
mixer.music.load('ex021.mp3')
mixer.music.play()
x = input('Digite algo para parar...')