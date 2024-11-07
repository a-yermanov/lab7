import pygame

pygame.init()
screen = pygame.display.set_mode((400, 300))
done = True
x = 30
y = 30

clock = pygame.time.Clock()


while done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = False
        
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP] and y>30 : y -= 20
        if pressed[pygame.K_DOWN] and y<260 : y += 20
        if pressed[pygame.K_LEFT] and x>30 : x -= 20
        if pressed[pygame.K_RIGHT] and x<360 : x += 20
        
        screen.fill((255, 255, 255))
        color = (255, 0, 0)
        pygame.draw.circle(screen, color, (x, y), 25)
        
        pygame.display.flip()
        clock.tick(60)