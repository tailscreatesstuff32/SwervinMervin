import pygame, os
import settings as s
import world_object as wo

class Sprite(wo.WorldObject):
    """Represents a single sprite in a level."""

    def __init__(self, name, x, y):
        self.offset     = x
        self.offset_y   = y
        self.sprite     = s.SPRITES[name]
        self.hit        = False

        wo.WorldObject.__init__(self)

    def is_speed_boost(self):
        return self.sprite.has_key("speed_boost")

    def is_bonus(self):
        return self.sprite.has_key("bonus")

    def path(self):
        sprite_name = self.sprite["path"]


        return pygame.image.load(os.path.join("lib", sprite_name))
