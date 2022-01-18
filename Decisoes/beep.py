import pygame
# import vlc

pygame.init()
pygame.mixer.init()
pygame.mixer.Sound("Beep.mp3")
pygame.mixer.music.play(-1)
input()
pygame.event.wait()

# p = vlc.MediaPlayer("beep.mp3")
# p.play("beep.mp3")
# p.stop()