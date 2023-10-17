from setup import *
from tile import Tile


class Spike(Tile):

    def __init__(self, position, angle=0):
        super().__init__(position)
        self.angle = angle % 360

    def update(self, delta, camera_speed):
        self.position.x -= camera_speed * delta

    def draw(self, screen):
        pygame.draw.polygon(screen, (0,255,0), [(self.position.x, self.position.y + self.height),
                                                (self.position.x + self.width, self.position.y + self.height),
                                                (self.position.x + self.width/2, self.position.y)])

