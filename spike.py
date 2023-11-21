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
        self.outlines = [True]
        self.hitbox_position = self.position + self.hitbox_offset

    def detect_outlines(self, tiles, spikes):
        for tile in tiles:
            if self.angle == 0:
                if tile.position == self.position + pygame.Vector2(0, self.height):
                    self.outlines[0] = False
            elif self.angle == 90:
                if tile.position == self.position + pygame.Vector2(-self.width, 0):
                    self.outlines[0] = False
            elif self.angle == 180:
                if tile.position == self.position + pygame.Vector2(0, -self.height):
                    self.outlines[0] = False
            elif self.angle == 270:
                if tile.position == self.position + pygame.Vector2(self.width, 0):
                    self.outlines[0] = False
        for spike in spikes:
            if self.angle == 0:
                if spike.position == self.position + pygame.Vector2(0, self.height):
                    self.outlines[0] = False
            elif self.angle == 90:
                if spike.position == self.position + pygame.Vector2(-self.width, 0):
                    self.outlines[0] = False
            elif self.angle == 180:
                if spike.position == self.position + pygame.Vector2(0, -self.height):
                    self.outlines[0] = False
            elif self.angle == 270:
                if spike.position == self.position + pygame.Vector2(self.width, 0):
                    self.outlines[0] = False

    def update(self, camera_position):
        super().update(camera_position)
        self.hitbox_position = self.position + self.hitbox_offset

    def draw(self, screen):
        if self.angle == 0:
            pygame.draw.polygon(screen, self.colour, [(self.display_position.x, self.display_position.y + self.height),
                                                (self.display_position.x + self.width, self.display_position.y + self.height),
                                                (self.display_position.x + self.width/2, self.display_position.y)])
            if self.outlines[0]:
                pygame.draw.polygon(screen, self.outline_colour, [(self.display_position.x, self.display_position.y + self.height),
                                                    (self.display_position.x + self.width, self.display_position.y + self.height),
                                                    (self.display_position.x + self.width/2, self.display_position.y)], width=self.outline_width)
            else:
                pygame.draw.lines(screen, self.outline_colour, False, [(self.display_position.x, self.display_position.y + self.height), (self.display_position.x + self.width/2, self.display_position.y),
                                                    (self.display_position.x + self.width, self.display_position.y + self.height)], width=self.outline_width)

        elif self.angle == 90:
            pygame.draw.polygon(screen, self.colour, [(self.display_position.x, self.display_position.y), (self.display_position.x + self.width, self.display_position.y + self.height/2), (self.display_position.x, self.display_position.y + self.height)])
            if self.outlines[0]:
                pygame.draw.polygon(screen, self.outline_colour, [(self.display_position.x, self.display_position.y), (self.display_position.x + self.width, self.display_position.y + self.height/2), (self.display_position.x, self.display_position.y + self.height)], width=self.outline_width)
            else:
                pygame.draw.lines(screen, self.outline_colour, False, [(self.display_position.x, self.display_position.y), (self.display_position.x + self.width, self.display_position.y + self.height/2), (self.display_position.x, self.display_position.y + self.height)], width=self.outline_width)
        elif self.angle == 180:
            pygame.draw.polygon(screen, self.colour, [(self.display_position.x, self.display_position.y), (self.display_position.x + self.width, self.display_position.y), (self.display_position.x + self.width/2, self.display_position.y + self.height)])
            if self.outlines[0]:
                pygame.draw.polygon(screen, self.outline_colour, [(self.display_position.x, self.display_position.y), (self.display_position.x + self.width, self.display_position.y), (self.display_position.x + self.width/2, self.display_position.y + self.height)], width=self.outline_width)
            else:
                pygame.draw.lines(screen, self.outline_colour, False, [(self.display_position.x, self.display_position.y), (self.display_position.x + self.width/2, self.display_position.y + self.height), (self.display_position.x + self.width, self.display_position.y)], width=self.outline_width)

        elif self.angle == 270:
            pygame.draw.polygon(screen, self.colour, [(self.display_position.x + self.width, self.display_position.y), (self.display_position.x + self.width, self.display_position.y + self.height), (self.display_position.x, self.display_position.y + self.height/2)])
            if self.outlines[0]:
                pygame.draw.polygon(screen, self.outline_colour, [(self.display_position.x + self.width, self.display_position.y), (self.display_position.x + self.width, self.display_position.y + self.height), (self.display_position.x, self.display_position.y + self.height/2)], width=self.outline_width)
            else:
                pygame.draw.lines(screen, self.outline_colour, False, [(self.display_position.x + self.width, self.display_position.y), (self.display_position.x, self.display_position.y + self.height/2), (self.display_position.x + self.width, self.display_position.y + self.height)], width=self.outline_width)



        # pygame.draw.rect(screen, (255,0,0),  [math.ceil(self.position.x + self.hitbox_offset.x), math.ceil(self.position.y+ self.hitbox_offset.y), math.ceil(self.hitbox_width), math.ceil(self.hitbox_height)])
