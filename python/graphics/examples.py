# Example file showing a basic pygame "game loop"
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Pygame Template")
clock = pygame.time.Clock()
running = True

# initialize colors 
YELLOW = (255,255,0)
PINK = (255,182,193)
GREEN  = (0,128,0)
BLACK = (0,0,0)
TAN = (222,184,135)

font = pygame.font.Font(None, 74)


while running:

    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # fill the screen with a color to wipe away anything from last frame
    screen.fill("white")

    # RENDER YOUR GAME HERE
    pygame.draw.rect(screen, YELLOW, (100,200, 30,200))
    pygame.draw.rect(screen, GREEN, (100,200, 30,20))
    pygame.draw.rect(screen, PINK,(100,170,30,30))
    pygame.draw.polygon(screen, TAN, ((100,400),(130,400),(115,420)))
    pygame.draw.polygon(screen, BLACK, ((108,410), (123,410), (115, 420)))

    # flip() the display to put your work on screen
    pygame.display.flip()
    clock.tick(60)  # limits FPS to 60

pygame.quit()