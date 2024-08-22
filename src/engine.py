#src/engine.py
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
#
# EVIL LAUGH! It's my world and I can do with it what I please!

class World:
    def __init__(self, screen) -> None:
        self.screen = screen

    def world_to_screen(self, position):
        pass

class World_Rect:
    def __init(self) -> None:
        self.world_position = {0, 0}
        self.size = {50, 50}
        self.color = "deepskyblue"
    def Draw(self) -> None:
        main.pygame.draw.rect(main.screen, "Purple", main.pygame.Rect(100,100,100,100))

class Game:
    def __init__(self, screen) -> None:
        self.game_world = World(screen)
        self.rect = World_Rect()

    def update(self) -> None:
        self.rect.Draw()
