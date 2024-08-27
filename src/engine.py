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
        self.width = self.size.x * self.scale.x
        self.height = self.size.y * self.scale.y
        self.color = "deepskyblue"
        self.anchor = Vec2(0.5, 0.5)
        self.screen = screen

    def Draw(self) -> None:
        wp = self.world_position
        anchor_posX = wp.x - self.width * self.anchor.x
        anchor_posY = wp.y + self.height * self.anchor.y
        sp = Vec2(*world_to_screen(anchor_posX, anchor_posY))
        rect = pygame.Rect(sp.x, sp.y, self.width, self.height)
        pygame.draw.rect(self.screen, "Purple", rect)

    def Contains(self, x, y) -> bool:
        return self.world_position.x <= x <= self.world_position.x + self.width and self.world_position.y - self.height <= y <= self.world_position.y

class Card:
    def __init__(self, screen):
        self.world_rect = World_Rect(screen)

    def Update(self):
        left_mouse, right_mouse, middle_mouse = pygame.mouse.get_pressed(num_buttons=3)
        mousex, mousey = screen_to_world(*pygame.mouse.get_pos())
        if left_mouse and self.world_rect.Contains(mousex, mousey):
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
