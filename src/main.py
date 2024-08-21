# src/main.py
import pygame
import sys

# Pygame Global Setup
pygame.init()
screen = pygame.display.set_mode((1280,720))
clock = pygame.time.Clock()
running = True

def event_handler():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("Quitting Application")
            pygame.display.quit()
            pygame.quit()
            exit()
            sys.exit()
            running = False

def main():
    # Main Program Loop
    print("Starting Application")
    while running:
        event_handler()
        screen.fill("Purple")
        pygame.display.flip()
        clock.tick(60)

    
if __name__ == "__main__":
    main()


