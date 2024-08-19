import pygame
from constants import *

def main():
    pygame.init()
    print(f"Starting asteroids!\n Screen width: {SCREEN_WIDTH}\n Screen height: {SCREEN_HEIGHT}")
    pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                            return
        pygame.display.flip()
    pass
    
if __name__ == "__main__":
    main()
