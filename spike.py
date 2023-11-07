from setup import *
from tile import Tile
import math


class Spike(Tile):

    def __init__(self, position, angle=0):
        super().__init__(position)
        self.angle = angle % 360

        k=0.75
        self.hitbox_width = self.width * (1-k)
        self.hitbox_height = self.height * k
        if self.angle == 0:
            self.hitbox_offset = pygame.Vector2(self.width / 2 - self.hitbox_width / 2, self.height - self.hitbox_height)
        elif self.angle == 90:
            self.hitbox_height, self.hitbox_width = self.hitbox_width, self.hitbox_height
            self.hitbox_offset = pygame.Vector2(k * self.height - self.hitbox_width, self.width/2 - self.hitbox_height/2)
        elif self.angle == 180:
            self.hitbox_offset = pygame.Vector2(self.width / 2 - self.hitbox_width / 2,
                                                self.height * k - self.hitbox_height)
        elif self.angle == 270:
            self.hitbox_height, self.hitbox_width = self.hitbox_width, self.hitbox_height
            self.hitbox_offset = pygame.Vector2((1-k) * self.height, self.width/2 - self.hitbox_height/2)

    def update(self, delta, camera_speed):
        self.position.x -= camera_speed * delta

    def draw(self, screen):
        if self.angle == 0:
            pygame.draw.polygon(screen, (0,255,0), [(self.position.x, self.position.y + self.height),
                                                (self.position.x + self.width, self.position.y + self.height),
                                                (self.position.x + self.width/2, self.position.y)])
        elif self.angle == 90:
            pygame.draw.polygon(screen, (0,255,0), [(self.position.x, self.position.y), (self.position.x + self.width, self.position.y + self.height/2), (self.position.x, self.position.y + self.height)])
        elif self.angle == 180:
            pygame.draw.polygon(screen, (0,255,0), [(self.position.x, self.position.y), (self.position.x + self.width, self.position.y), (self.position.x + self.width/2, self.position.y + self.height)])
        elif self.angle == 270:
            pygame.draw.polygon(screen, (0,255,0), [(self.position.x + self.width, self.position.y), (self.position.x + self.width, self.position.y + self.height), (self.position.x, self.position.y + self.height/2)])

        pygame.draw.rect(screen, (255,0,0),  [math.ceil(self.position.x + self.hitbox_offset.x), math.ceil(self.position.y+ self.hitbox_offset.y), math.ceil(self.hitbox_width), math.ceil(self.hitbox_height)])
