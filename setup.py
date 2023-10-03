import pygame


pygame.init()

SCREEN_WIDTH = 720
SCREEN_HEIGHT = 640
dimensions = pygame.Vector2(SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


pygame.display.set_caption("Geometry Dash")

icon = pygame.Surface((32,32))
icon.fill((0,0,0))

font = pygame.font.SysFont("Arial", 20)
text = font.render("GD", True, (255,255,255))
text = pygame.transform.scale(text, (28,28))
icon.blit(text, (2,2))
pygame.display.set_icon(icon)

