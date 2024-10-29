import pygame

pygame.init()

WIDTH, HEIGHT = 1280, 720
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('SLIDING BLOCK PUZZLE')

FONT = pygame.font.SysFont('arial', 30, False, False)
FPS = 60
CLOCK = pygame.time.Clock()


def main():
    WINDOW.fill((0, 0, 0))
    pygame.display.update()

    while True:				
        CLOCK.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
					
if __name__ == '__main__':
    main()