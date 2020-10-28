# Import and initialize the pygame library
import pygame
from supyplex.commons import *
from supyplex.sprites import Murphy
from supyplex.game_logic import GameLogic
from os import path

pygame.init()


class SuPyplex(object):
    def __init__(self, base_dir):
        self.surface = None
        self.level = None
        self.running = False
        self.levelInfo = None
        self.sprites = None
        self.window = None
        self.murphy = None
        self.base_dir = base_dir

    def setup(self):
        self.window = pygame.display.set_mode([800, 600])
        self.surface = pygame.Surface((MAX_X, MAX_Y))
        self.running = True
        self.level = GameLogic(5, self.base_dir)
        self.sprites = pygame.image.load(path.join(self.base_dir, "resources/Mpx32.bmp"))
        self.murphy = Murphy(self.surface, self.sprites, self.level)

    def draw(self):
        self.surface.fill((0, 0, 0))
        self.level.calculate_next_move()

        for i in range(24):
            for j in range(60):
                current = self.level.map[i][j]
                x_s = current % 16
                y_s = current // 16
                if current != 3:
                    self.surface.blit(self.sprites, (j * CELL_SIZE, i * CELL_SIZE, CELL_SIZE, CELL_SIZE),
                                      (x_s * CELL_SIZE, y_s * CELL_SIZE, CELL_SIZE, CELL_SIZE))
                else:
                    if self.murphy.next_position is None:
                        self.murphy.position = Point(j * 32, i * 32)
        self.murphy.update()

    def get_surface_position(self):

        r = (max(self.murphy.position.x - 400, 0), max(self.murphy.position.y - 300, 0),
             min(self.murphy.position.x + 400, MAX_X), min(self.murphy.position.y + 300, MAX_Y))

        x, y = r[0], r[1]
        if r[0] == 0:
            x = 0
        elif r[2] == MAX_X:
            x = MAX_X - 800

        if r[1] == 0:
            y = 0
        elif r[3] == MAX_Y:
            y = MAX_Y - 600
        return x, y, 800, 600

    def manage_key(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_q]:
            self.running = False

        if keys[pygame.K_LEFT]:
            if not self.murphy.is_moving:
                n_pos: Point = self.murphy.position + POINT_LEFT
                if self.level.can_move(n_pos.map_tuple()):
                    self.murphy.move_to(n_pos, "move_left")
                else:
                    self.murphy.apply_status("watch_left")
        elif keys[pygame.K_RIGHT]:
            if not self.murphy.is_moving:
                n_pos: Point = self.murphy.position + POINT_RIGHT
                if self.level.can_move(n_pos.map_tuple()):
                    self.murphy.move_to(n_pos, "move_right")
                else:
                    self.murphy.apply_status("watch_right")

        elif keys[pygame.K_UP]:
            if not self.murphy.is_moving:
                n_pos: Point = self.murphy.position + POINT_UP
                if self.level.can_move(n_pos.map_tuple()):
                    self.murphy.move_to(n_pos, "move_up")
        elif keys[pygame.K_DOWN]:
            if not self.murphy.is_moving:
                n_pos: Point = self.murphy.position + POINT_DOWN
                if self.level.can_move(n_pos.map_tuple()):
                    self.murphy.move_to(n_pos, "move_down")
        else:
            if not self.murphy.is_moving:
                self.murphy.apply_status("idle")

    def main_loop(self):
        clock = pygame.time.Clock()

        while self.running:
            clock.tick(FPS)
            self.manage_key()
            self.draw()

            self.window.blit(self.surface, (0, 0), self.get_surface_position())
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    self.running = False
            pygame.display.set_caption("Memory Game - FPS: %.0f" % clock.get_fps())
            pygame.display.flip()
            # pygame.display.update()

        pygame.quit()
