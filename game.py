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
        self.camera_position = pygame.Vector2(0,0)

        self.tile_sections = []
        self.spike_sections = []
        self.section_index = 0

        self.level = level
        self.import_level()

        for i, section in enumerate(zip(self.tile_sections, self.spike_sections)):
            tiles, spikes = section

            for tile in tiles:
                tile.detect_outlines(tiles + self.tile_sections[(i - 1) % len(self.tile_sections)] + self.tile_sections[(i + 1) % len(self.tile_sections)] , spikes + self.spike_sections[(i - 1) % len(self.spike_sections)] + self.spike_sections[(i + 1) % len(self.spike_sections)] )

            for spike in spikes:
                spike.detect_outlines(tiles + self.tile_sections[(i - 1) % len(self.tile_sections)] + self.tile_sections[(i + 1 )% len(self.tile_sections)] , spikes + self.spike_sections[(i - 1) % len(self.spike_sections)] + self.spike_sections[(i + 1) % len(self.spike_sections)] )


    def import_level(self):
        with open("levels/" + self.level + ".txt") as f:
            lines = f.readlines()

            self.tile_sections = [[] for _ in range(max(lines, key=len).count(',') // (SCREEN_WIDTH // Tile.width) + 1)]
            self.spike_sections = [[] for _ in range(max(lines, key=len).count(',') // (SCREEN_WIDTH // Tile.width) + 1)]

            for y, line in enumerate(lines):
                for x, tile_type in enumerate(line.replace(',', "")):
                    if tile_type == "1":
                        t = Tile((x * Tile.width, y * Tile.height))
                        self.tiles.append(t)
                        self.tile_sections[x // (SCREEN_WIDTH // Tile.width)].append(t)
                    elif tile_type == "2":
                        t = HalfTile((x * Tile.width, y * Tile.height))
                        self.tiles.append(t)
                        self.tile_sections[x // (SCREEN_WIDTH // Tile.width)].append(t)
                    elif tile_type == "3":
                        t = Spike((x * Tile.width, y * Tile.height), 0)
                        self.spikes.append(t)
                        self.spike_sections[x // (SCREEN_WIDTH // Tile.width)].append(t)
                    elif tile_type == "4":
                        t = Spike((x * Tile.width, y * Tile.height), 90)
                        self.spikes.append(t)
                        self.spike_sections[x // (SCREEN_WIDTH // Tile.width)].append(t)
                    elif tile_type == "5":
                        t = Spike((x * Tile.width, y * Tile.height), 180)
                        self.spikes.append(t)
                        self.spike_sections[x // (SCREEN_WIDTH // Tile.width)].append(t)
                    elif tile_type == "6":
                        t = Spike((x * Tile.width, y * Tile.height), 270)
                        self.spikes.append(t)
                        self.spike_sections[x // (SCREEN_WIDTH // Tile.width)].append(t)
                    elif tile_type == "7":
                        self.goal = Goal((x * Tile.width, y * Tile.height))
                    elif tile_type == "8":
                        self.portals.append(Portal((x * Tile.width, y * Tile.height), Player.SHIP))
                    elif tile_type == "9":
                        self.portals.append(Portal((x * Tile.width, y * Tile.height), Player.SQUARE))

    def update(self, delta):

        if self.section_index < len(self.tile_sections) - 2:
            if self.camera_position.x > SCREEN_WIDTH // Tile.width * (self.section_index + 1) * Tile.width:
                self.section_index += 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return COMMAND_QUIT
        player_status = self.player.update(delta, self.tile_sections[self.section_index] + self.tile_sections[self.section_index + 1], self.spike_sections[self.section_index] + self.spike_sections[self.section_index + 1], self.goal, self.portals, self.camera_speed,self.camera_position)

        if player_status == PLAYER_DEAD:
            return COMMAND_RESTART
        elif player_status == PLAYER_WIN:
            return COMMAND_QUIT

        for tile in self.tile_sections[self.section_index] + self.tile_sections[self.section_index + 1]:
            tile.update(self.camera_position)
        for spike in self.spike_sections[self.section_index] + self.spike_sections[self.section_index + 1]:
            spike.update(self.camera_position)

        for portal in self.portals:
            portal.update(self.camera_position)

        if self.goal:
            self.goal.update(self.camera_position)


        self.camera_position.x += self.camera_speed.x * delta

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