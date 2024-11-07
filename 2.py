import pygame
import os

pygame.init()

current_directory = os.getcwd()

screen = pygame.display.set_mode((400, 300))

Songs = []
for f in os.listdir(current_directory):
    if os.path.isfile(os.path.join(current_directory, f)) and f.endswith(".mp3"):
        Songs.append(f)


s = 0
pygame.mixer.music.load(Songs[s])
pygame.mixer.music.play()

paused = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                paused = not paused
                if paused:
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()
            elif event.key == pygame.K_RIGHT:
                s = (s + 1) % len(Songs)
                pygame.mixer.music.load(Songs[s])
                pygame.mixer.music.play()
            elif event.key == pygame.K_LEFT:
                s = (s - 1) % len(Songs)
                pygame.mixer.music.load(Songs[s])
                pygame.mixer.music.play()


    screen.fill((0, 0, 0))

    font = pygame.font.Font(None, 36)
    text = font.render(Songs[s], True, (255, 255, 255))
    screen.blit(text, (10, 10))

    pygame.display.update()