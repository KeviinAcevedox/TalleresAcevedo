import pygame

pygame.init()

screen_w = 600
screen_h = 600

window = pygame.display.set_mode((screen_w, screen_h))
pygame.display.set_caption("ACE-WARS")

#Character first design

x = 50
y = 440
w = 40
h = 40
speed = 10

running = True
while running:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and y > 0:
            y -= speed

        if keys[pygame.K_s] and y < screen_h - h - speed:
            y += speed

        if keys[pygame.K_a] and x > 0:
            x -= speed

        if keys[pygame.K_d] and x < screen_w - w - speed:
            x += speed

        window.fill((0,0,0))
        pygame.draw.rect(window, (255,0,0), (x, y, w, h))
        pygame.display.update()

pygame.quit()






