import pygame
from typing import List

from supyplex.GameLogic import GameLogic
from supyplex.commons import *


class SpriteStatus(object):
    def __init__(self, action, frame_rect):
        self.action = action
        self.frame_rect = frame_rect
        self.frame_idx = 0

    def next_frame(self):
        self.frame_idx = (self.frame_idx + 1) % len(self.frame_rect)
        return self.frame_rect[self.frame_idx]

    def reset_frame(self):
        self.frame_idx = 0


class GenericSprite(pygame.sprite.Sprite):

    def __init__(self, screen: pygame.Surface, image: pygame.Surface, level: GameLogic):
        super().__init__()

        self.screen = screen
        self.image = image
        self.level = level
        self.status: List[SpriteStatus] = []
        self.current_status: SpriteStatus = None
        self.position: Point = Point()
        self.next_position: Point = None
        self.actions = []
        self.is_moving = False
        self.speed = 4

    def calculate_rect(self, status):
        pass

    def apply_status(self, status: str):
        self.current_status = next(i for i in self.status if i.action == status)

    def move_to(self, p: Point, status: str):

        self.actions = [self.position.clone(), p]

        self.next_position = p
        self.is_moving = True
        self.apply_status(status)

    def update(self):
        d_rect = self.current_status.next_frame()

        if self.current_status.action == "move_left":
            if self.position != self.next_position:
                self.position = self.position + Point(-self.speed, 0)
            else:
                p_pos = self.position + POINT_RIGHT
                self.level.move_complete(p_pos.map_tuple(), self.position.map_tuple())
                self.is_moving = False
        if self.current_status.action == "move_right":
            if self.position != self.next_position:
                self.position = self.position + Point(self.speed, 0)
            else:
                p_pos = self.position + POINT_LEFT
                self.level.move_complete(p_pos.map_tuple(), self.position.map_tuple())
                self.is_moving = False
        if self.current_status.action == "move_up":
            if self.position != self.next_position:
                self.position = self.position + Point(0, -self.speed)
            else:
                p_pos = self.position + POINT_DOWN
                self.level.move_complete(p_pos.map_tuple(), self.position.map_tuple())
                self.is_moving = False
        if self.current_status.action == "move_down":
            if self.position != self.next_position:
                self.position = self.position + Point(0, self.speed)
            else:
                p_pos = self.position + POINT_UP
                self.level.move_complete(p_pos.map_tuple(), self.position.map_tuple())
                self.is_moving = False

        self.screen.blit(self.image, self.position.tuple(), d_rect)


class Zonk(GenericSprite):
    def __init__(self, screen, image, level):
        """ Constructor. Pass in the color of the block,
        and its x and y position. """
        # Call the parent class (Sprite) constructor
        super().__init__(screen, image, level)

        self.status = [
            SpriteStatus(action="move_left", frame_rect=[(i * 32, 12 * 32, 32, 32) for i in range(4)]),
            SpriteStatus(action="move_right", frame_rect=[(i * 32, 12 * 32, 32, 32) for i in range(4, 8)]),
            SpriteStatus(action="move_down", frame_rect=[(32 * 1, 0, 32, 32)]),
            SpriteStatus(action="move_up", frame_rect=[(32 * 1, 0, 32, 32)]),
            SpriteStatus(action="idle", frame_rect=[(32 * 1, 0, 32, 32)]),

        ]
        self.current_status = self.status[4]


class Murphy(GenericSprite):
    def __init__(self, screen, image, level):
        """ Constructor. Pass in the color of the block,
        and its x and y position. """
        # Call the parent class (Sprite) constructor
        super().__init__(screen, image, level)

        self.status = [
            SpriteStatus(action="move_left", frame_rect=[(i * 32, 11 * 32, 32, 32) for i in range(8)]),
            SpriteStatus(action="move_right", frame_rect=[(i * 32, 11 * 32, 32, 32) for i in range(8, 16)]),
            SpriteStatus(action="move_down", frame_rect=[(i * 32, 11 * 32, 32, 32) for i in range(8, 16)]),
            SpriteStatus(action="move_up", frame_rect=[(i * 32, 11 * 32, 32, 32) for i in range(8, 16)]),
            SpriteStatus(action="idle", frame_rect=[(32 * 3, 0, 32, 32)]),
            SpriteStatus(action="watch_left", frame_rect=[(6*32, 11 * 32, 32, 32)]),
            SpriteStatus(action="watch_right", frame_rect=[(15 * 32, 11 * 32, 32, 32)]),
        ]
        self.current_status = self.status[4]
