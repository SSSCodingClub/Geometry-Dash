import pygame

from setup import *


class Portal:
    width = 50
    height = 200
    colour = {
        "SQUARE": (0, 255, 0),
        "SHIP": (179, 0, 179)
    }
    outline_colour = {
        "SQUARE": (0, 128, 0),
        "SHIP": (89, 0, 89)
    }

    outline_width = 3
    border_radius = 15

    def __init__(self, position, mode):
        self.position = pygame.Vector2(position)
        self.display_position = pygame.Vector2(position)
        self.mode = mode

    def update(self, camera_position):
        self.display_position.x = self.position.x - camera_position.x

    def draw(self, screen):
        pygame.draw.rect(screen, self.colour[self.mode],(self.display_position.x, self.display_position.y + 0.025 * self.height,
                          self.width, self.height * 0.95), border_radius=self.border_radius)
        pygame.draw.rect(screen, self.colour[self.mode],(self.display_position.x, self.display_position.y + 0.025 * self.height,
                          self.width, self.height * 0.95), self.outline_width, border_radius=self.border_radius)
