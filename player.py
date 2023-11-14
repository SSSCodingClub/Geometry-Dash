from setup import *


class Player:
    width, height = 50, 50

    gravity = pygame.Vector2(0, 1900)
    jump_velocity = -715
    jump_cooldown_amount = 0

    ship_gravity = pygame.Vector2(0, 450)
    ship_velocity = -125
    ship_jump_cooldown = 0.1
    ship_display_angle_increment = 0.25

    colour = (255, 0, 0)
    outline_colour = (128, 0, 0)

    outline_width = 3

    SQUARE = "SQUARE"
    SHIP = "SHIP"

    default_points = {SQUARE: [pygame.Vector2(0, 0), pygame.Vector2(width, 0), pygame.Vector2(width, height),
                               pygame.Vector2(0, height)],
                      SHIP: [pygame.Vector2(0,0), pygame.Vector2(width, height/2), pygame.Vector2(0, height)]}

    def __init__(self):
        self.position = pygame.Vector2(SCREEN_WIDTH / 5, SCREEN_HEIGHT * 2 / 3)
        self.velocity = pygame.Vector2(0, 0)
        self.acceleration = pygame.Vector2(0, self.gravity.y)

        self.on_ground = False
        self.jumped = False
        self.jump_cooldown = 0

        self.mode = self.SQUARE

        self.points = self.default_points[self.mode][:]
        self.angle = 0

    def change_mode(self, mode):
        if self.mode == mode:
            return

        self.mode = mode
        self.velocity = pygame.Vector2(0,0)
        self.jumped = False
        self.angle = 0
        self.rotate(self.angle)
        self.points = self.default_points[self.mode][:]
        if mode == self.SQUARE:
            self.acceleration = pygame.Vector2(0, self.gravity.y)
        elif mode == self.SHIP:
            self.acceleration = pygame.Vector2(0, self.ship_gravity.y)


    def update(self, delta, tiles, spikes, goal, portals):
        if not (self.mode == self.SQUARE and self.on_ground):
            self.jump_cooldown = max(0, self.jump_cooldown - delta)

        if self.mode == self.SHIP:
            old_angle = self.angle
            new_angle = max(min(self.velocity.y / 10, 30), -30)
            if abs(new_angle-old_angle) > self.ship_display_angle_increment:
                self.angle = old_angle + math.copysign(self.ship_display_angle_increment, new_angle - old_angle)
            else:
                self.angle = new_angle

            self.rotate(self.angle)

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
            if self.colliding(spike.position.x + spike.hitbox_offset.x, spike.position.y + spike.hitbox_offset.y,
                              spike.hitbox_width, spike.hitbox_height):
                return PLAYER_DEAD

        for portal in portals:
            if self.colliding(portal.position.x + self.width, portal.position.y, portal.width, portal.height):
                self.change_mode(portal.mode)

        if goal:
            if self.colliding(goal.position.x + self.width, goal.position.y, goal.width, goal.height):
                return PLAYER_WIN

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
        if self.mode == self.SQUARE:
            if self.on_ground:
                self.velocity.y = self.jump_velocity
                self.jump_cooldown = self.jump_cooldown_amount
                self.jumped = True
        if self.mode == self.SHIP:
            self.velocity.y += self.ship_velocity
            self.jump_cooldown = self.ship_jump_cooldown
            self.jumped = True

    def rotate(self, angle):
        points = [point.copy() for point in self.default_points[self.mode]]
        display_angle = round(angle)
        center = pygame.Vector2(self.width/2, self.height/2)
        for point in points:
            point -= center
            point.rotate_ip(display_angle)
            point += center
        self.points = points[:]


    def draw(self, screen):
        display_points = [self.position + point for point in self.points]
        pygame.draw.polygon(screen, self.colour, display_points)
        pygame.draw.polygon(screen, self.colour, display_points , self.outline_width)

