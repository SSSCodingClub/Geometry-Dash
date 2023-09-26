import pygame

pygame.init()
width = 720
height = 640
screen = pygame.display.set_mode((width, height))

is_running = True
while is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

    screen.fill((153, 50, 204))

    pygame.display.update()

pygame.quit()
