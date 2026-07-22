def playBgMusic():
    import pygame
    pygame.mixer.init()
    pygame.mixer.music.load("data/the fiber 16x loop.wav")
    pygame.mixer.music.play(-1)