from setup import *


class Goal:
    width = 50
    height = SCREEN_HEIGHT

    def __init__(self, position):
        self.position = pygame.Vector2(position[0], 0)

    def update(self, delta, camera_speed):
        self.position.x -= camera_speed * delta

    def draw(self, screen):
        pygame.draw.rect(screen, (144,238,144), (self.position.x, self.position.y, SCREEN_WIDTH, SCREEN_HEIGHT))



