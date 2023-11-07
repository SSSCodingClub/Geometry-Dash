from setup import *


class Tile:
    width, height = 50, 50
    colour = (0,0,0)
    outline_colour = (150,150,150)
    outline_width = 3

    def __init__(self, position):
        self.position = pygame.Vector2(position)
        self.outlines = [True, True, True, True] # Top, Right, Bot, Left

    def detect_outlines(self, tiles, spikes):
        for tile in tiles:
            if tile.position == self.position + pygame.Vector2(0, -self.height):
                self.outlines[0] = False
            if tile.position == self.position + pygame.Vector2(self.width, 0):
                self.outlines[1] = False
            if tile.position == self.position + pygame.Vector2(0, self.height):
                self.outlines[2] = False
            if tile.position == self.position + pygame.Vector2(-self.width, 0):
                self.outlines[3] = False




    def update(self, delta, camera_speed):
        self.position.x -= camera_speed * delta

    def draw(self, screen):
        pygame.draw.rect(screen, self.colour, (self.position.x, self.position.y, self.width, self.height))

        if self.outlines[0]:
            pygame.draw.line(screen, self.outline_colour, (self.position.x, self.position.y), (self.position.x + self.width, self.position.y), self.outline_width)
        if self.outlines[1]:
            pygame.draw.line(screen, self.outline_colour, (self.position.x + self.width, self.position.y), (self.position.x + self.width, self.position.y + self.height), self.outline_width)
        if self.outlines[2]:
            pygame.draw.line(screen, self.outline_colour, (self.position.x + self.width, self.position.y + self.height), (self.position.x, self.position.y + self.height), self.outline_width)
        if self.outlines[3]:
            pygame.draw.line(screen, self.outline_colour, (self.position.x, self.position.y + self.height), (self.position.x, self.position.y), self.outline_width)



class HalfTile(Tile):
    height = 25
