from setup import *
from player import Player
from tile import Tile, HalfTile
from spike import Spike
from goal import Goal
from portal import Portal


class Game:

    def __init__(self, level):
        self.player = Player()
        self.tiles = []
        self.spikes = []
        self.portals = []
        self.goal = None

        self.camera_speed = pygame.Vector2(300,0)

        self.level = level
        self.import_level()

        for tile in self.tiles:
            tile.detect_outlines(self.tiles, self.spikes)
        for spike in self.spikes:
            spike.detect_outlines(self.tiles, self.spikes)

    def import_level(self):
        with open("levels/" + self.level + ".txt") as f:
            lines = f.readlines()
            for y, line in enumerate(lines):
                for x, tile_type in enumerate(line.replace(',', "")):
                    if tile_type == "1":
                        self.tiles.append(Tile((x * Tile.width, y * Tile.height)))
                    elif tile_type == "2":
                        self.tiles.append(HalfTile((x * Tile.width, y * Tile.height)))
                    elif tile_type == "3":
                        self.spikes.append(Spike((x * Tile.width, y * Tile.height), 0))
                    elif tile_type == "4":
                        self.spikes.append(Spike((x * Tile.width, y * Tile.height), 90))
                    elif tile_type == "5":
                        self.spikes.append(Spike((x * Tile.width, y * Tile.height), 180))
                    elif tile_type == "6":
                        self.spikes.append(Spike((x * Tile.width, y * Tile.height), 270))
                    elif tile_type == "7":
                        self.goal = Goal((x * Tile.width, y * Tile.height))
                    elif tile_type == "8":
                        self.portals.append(Portal((x * Tile.width, y * Tile.height), Player.SHIP))
                    elif tile_type == "9":
                        self.portals.append(Portal((x * Tile.width, y * Tile.height), Player.SQUARE))




    def update(self, delta):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return COMMAND_QUIT
        player_status = self.player.update(delta, self.tiles, self.spikes, self.goal, self.portals)

        if player_status == PLAYER_DEAD:
            return COMMAND_RESTART
        elif player_status == PLAYER_WIN:
            return COMMAND_QUIT

        for tile in self.tiles:
            tile.update(delta, self.camera_speed.x)
        for spike in self.spikes:
            spike.update(delta, self.camera_speed.x)

        for portal in self.portals:
            portal.update(delta, self.camera_speed.x)

        if self.goal:
            self.goal.update(delta, self.camera_speed.x)

    def draw(self, screen):
        screen.fill((0, 0, 0))
        self.player.draw(screen)
        if self.goal:
            self.goal.draw(screen)
        for tile in self.tiles:
            tile.draw(screen)
        for spike in self.spikes:
            spike.draw(screen)
        for portal in self.portals:
            portal.draw(screen)