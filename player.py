from setup import *


class Player:
    width, height = 50, 50

    gravity = pygame.Vector2(0, 1900)

    jump_velocity = -715
    jump_cooldown_amount = 0

    colour = (255, 0, 0)
    outline_colour = (128, 0, 0)

    outline_width = 3

    def __init__(self):
        self.position = pygame.Vector2(SCREEN_WIDTH / 5, SCREEN_HEIGHT * 2 / 3)
        self.velocity = pygame.Vector2(0, 0)
        self.acceleration = pygame.Vector2(0, self.gravity.y)

        self.on_ground = False
        self.jumped = False
        self.jump_cooldown = 0

    def update(self, delta, tiles, spikes):
        if self.on_ground:
            self.jump_cooldown = max(0, self.jump_cooldown - delta)

        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE] or keys[pygame.K_UP] or keys[pygame.K_w]:
            self.jump()

        for tile in tiles:
            if self.colliding(tile.position.x, tile.position.y, tile.width, tile.height):
                return PLAYER_DEAD

        # y movement
        self.velocity.y += self.acceleration.y * delta
        self.position.y += self.velocity.y * delta
        self.on_ground = False

        for tile in tiles:
            if self.colliding(tile.position.x, tile.position.y, tile.width, tile.height):
                if self.velocity.y > 0:
                    self.position.y = tile.position.y - self.height
                    self.on_ground = True
                elif self.velocity.y < 0:
                    self.position.y = tile.position.y + tile.height
                    return PLAYER_DEAD
                self.velocity.y = 0

        for spike in spikes:
            if self.colliding(spike.position.x, spike.position.y, spike.width, spike.height):
                return PLAYER_DEAD


    def colliding(self, x, y, width, height):
        if (self.position.x < x + width and
                self.position.x + self.width > x and
                self.position.y < y + height and
                self.position.y + self.height > y):
            return True
        return False

    def jump(self):
        if self.jump_cooldown != 0:
            return

        if self.on_ground:
            self.velocity.y = self.jump_velocity
            self.jump_cooldown = self.jump_cooldown_amount
            self.jumped = True

    def draw(self, screen):
        pygame.draw.rect(screen, self.colour, (self.position.x, self.position.y, self.width, self.height))
        pygame.draw.rect(screen, self.outline_colour, (self.position.x, self.position.y, self.width, self.height),
                         self.outline_width)
