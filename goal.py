from setup import *


class Goal:
    width = 50
    height = SCREEN_HEIGHT

    def __init__(self, position):
        self.position = pygame.Vector2(position[0], 0)
        self.display_position = pygame.Vector2(position[0], 0)

    def update(self, camera_position):
        self.display_position.x = self.position.x - camera_position.x

    def draw(self, screen):
        pygame.draw.rect(screen, (144,238,144), (self.display_position.x, self.display_position.y, SCREEN_WIDTH, SCREEN_HEIGHT))



