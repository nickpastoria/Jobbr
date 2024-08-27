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

def screen_to_world(x, y) -> (float, float):
    return (x, pygame.display.Info().current_h-y)

class World_Rect:
    def __init__(self, screen) -> None:
        self.world_position = Vec2(pygame.display.Info().current_w / 2, pygame.display.Info().current_h / 2)
        self.size = Vec2(300, 400)
        self.scale = Vec2(1.25, 1.25) 
        self.color = "deepskyblue"
        self.anchor = Vec2(0.5, 0.5)
        self.screen = screen

    def Draw(self) -> None:
        wp = self.world_position
        true_sizeX = self.size.x * self.scale.x
        true_sizeY = self.size.y * self.scale.y
        twpX = wp.x - true_sizeX * self.anchor.x
        twpY = wp.y + true_sizeY * self.anchor.y
        sp = Vec2(*world_to_screen(twpX, twpY))
        rect = pygame.Rect(sp.x, sp.y, true_sizeX, true_sizeY)
        pygame.draw.rect(self.screen, "Purple", rect)

class Card:
    def __init__(self, screen):
        self.world_rect = World_Rect(screen)

    def Update(self):
        mousex, mousey = screen_to_world(*pygame.mouse.get_pos())
        self.world_rect.world_position.x = mousex
        self.world_rect.world_position.y = mousey

    def Draw(self):
        self.world_rect.Draw()

class Game:
    def __init__(self, screen) -> None:
        self.screen = screen
        self.card = Card(screen)

    def update(self) -> None:
        self.card.Update()
        self.card.Draw()
