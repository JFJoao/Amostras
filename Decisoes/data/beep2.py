# Beeps em tempo aleatorio
import pygame
from random import randint
# from datetime import datetime
import time

parar = "S"
while parar == 'S':
    z = randint(2, 3)
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load("beep.wav")
    pygame.mixer.Sound("beep.wav")
    pygame.mixer.music.play(1)
    # input()
    print(z)
    pygame.event.wait()
    time.sleep(z)
    # (input("\nAperte \"S\" para interromper: ")).upper()

