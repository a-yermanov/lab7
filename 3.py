import pygame
from datetime import datetime
pygame.init()

W, H = 900,900
WHITE = (255, 255, 255)
place = pygame.display.set_mode((W,H))
mid = W/2, H/2

back = pygame.image.load('main.png')
sec = pygame.image.load('left.png')
min = pygame.image.load('right.png')

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    time = datetime.now()
    sec_ang =(time.second / 60) * 360
    min_ang = (time.minute / 60) * 360 + (time.second / 60) * 6

    rtLeft = pygame.transform.rotate(sec, -sec_ang)
    rcLeft = rtLeft.get_rect(center = mid)
    rtRight = pygame.transform.rotate(min, -min_ang-45)
    rcRight = rtRight.get_rect(center = mid)

    place.fill(WHITE)
    place.blit(back, (0, 0))
    place.blit(rtLeft, rcLeft)
    place.blit(rtRight, rcRight)
    pygame.display.update()
    clock.tick(60)