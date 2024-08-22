import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    framerate = pygame.time.Clock()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    player.containers = (updatable, drawable)
    dt = 0
    
    while True:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return

        screen.fill("black")
        
        for obj in updatable:
            obj.update(dt)
        for obj in drawable:
            obj.draw(screen)
        
        pygame.display.flip()
        
        dt = framerate.tick(60)/1000
    
if __name__ == "__main__":
    main()
