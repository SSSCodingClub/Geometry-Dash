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
        self.mode = mode

    def update(self, delta, camera_speed):
        self.position.x -= camera_speed * delta

    def draw(self, screen):
        pygame.draw.rect(screen, self.colour[self.mode],(self.position.x, self.position.y + 0.025 * self.height,
                          self.width, self.height * 0.95), border_radius=self.border_radius)
        pygame.draw.rect(screen, self.colour[self.mode],(self.position.x, self.position.y + 0.025 * self.height,
                          self.width, self.height * 0.95), self.outline_width, border_radius=self.border_radius)
