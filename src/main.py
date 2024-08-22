# src/main.py
import pygame
import engine
# Pygame Global Setup
pygame.init()
screen_width = 1280
screen_height = 720
screen_flags =  pygame.RESIZABLE
screen = pygame.display.set_mode((screen_width, screen_height), screen_flags)
pygame.display.set_caption("Job Hunter Game")
clock = pygame.time.Clock()
running = True


def event_handler():
    for event in pygame.event.get():
            if event.type == pygame.VIDEORESIZE:
                screen_width = event.w
                screen_height = event.h
                # Apparently you don't have to reset the game screen mode because it just causes the window to relaunch
                #screen = pygame.display.set_mode((screen_width, screen_height), screen_flags)
            if event.type == pygame.QUIT:
                print("Quitting Application")
                pygame.display.quit()
                pygame.quit()
                exit()


def main():
    # Main Program Loop
    print("Starting Application")

    game = engine.Game(screen)
    while running:
        event_handler()
        # I'll leave this in for now as a debug thing
        screen.fill("LightBlue")
        game.update()
        # I also want to leave the main display flip here for now
        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    main()
