# Example file showing a basic pygame "game loop"
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Pygame Template")
clock = pygame.time.Clock()
running = True

# initialize colors 
RED = (255, 0, 0)
BLACK = (0,0,0)
WHITE = (255,255,255)

while running:

    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")
    # RENDER YOUR GAME HERE
    pygame.draw.line(screen, RED, (20,30), (200,30), 6)

    # flip() the display to put your work on screen
    pygame.display.flip()
    clock.tick(60)  # limits FPS to 60

pygame.quit()