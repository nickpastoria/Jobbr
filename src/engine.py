#src/engine.py
import pygame
# I guess we'll start with a function and build it up as we need it :shrug:

# Handles translation from screenspace to worldspace and vice versa
# since the window is resizeable
# I'll have to come up with a new set of units for the game space
#   Lets call them nicks.
#       Not sure how to handle object scaling yet
# Screen:
#           (tm)
#      -------*-------
#      |             |
# (ml) *      *      * (mr)
#      |     (m)     |
#      *------*-------
# (0,0)      (bm)
# (0, height)
# EVIL LAUGH! It's my world and I can do with it what I please!

class Vec2:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

def world_to_screen(x, y) -> (float, float):
    return (x, pygame.display.Info().current_h-y)
    

class World_Rect:
    def __init__(self) -> None:
        self.world_position = Vec2(0,50)
        self.size = Vec2(50, 50)
        self.color = "deepskyblue"

    def Draw(self, screen) -> None:
        wp = self.world_position
        rect = pygame.Rect(*world_to_screen(wp.x, wp.y), self.size.x, self.size.y)
        pygame.draw.rect(screen, "Purple", rect)

class Game:
    def __init__(self, screen) -> None:
        self.screen = screen
        self.rect = World_Rect()

    def update(self) -> None:
        self.rect.Draw(self.screen)
