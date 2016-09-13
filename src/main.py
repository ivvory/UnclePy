import pygame
import basicgrid
from snake import UnclePy

from exceptions.bounds import OutOfCellsBoundError
from exceptions.twist import SnakeTwistedError

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

CELLS_IN_ROW = 60
CELL_WIDTH = 6
CELL_HEIGHT = 6
MARGIN = 1

FPS = 60

grid = basicgrid.BasicGrid(CELL_WIDTH, CELL_HEIGHT, MARGIN, CELLS_IN_ROW)

pygame.init()

WINDOW_SIZE = grid.calculate_screen_size()
screen = pygame.display.set_mode(WINDOW_SIZE)

pygame.display.set_caption('UnclePy')

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

snake = UnclePy(grid, RED, FPS, 60)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT and snake.direction != 'LEFT':
                snake.direction = 'RIGHT'
            if event.key == pygame.K_LEFT and snake.direction != 'RIGHT':
                snake.direction = 'LEFT'
            if event.key == pygame.K_UP and snake.direction != 'DOWN':
                snake.direction = 'UP'
            if event.key == pygame.K_DOWN and snake.direction != 'UP':
                snake.direction = 'DOWN'

    try:
        snake.move()
    except (OutOfCellsBoundError, SnakeTwistedError):
        snake = UnclePy(grid, RED, FPS)
        grid.clear()

    # Set the screen background
    screen.fill(BLACK)

    # Draw the grid
    grid.draw(screen, pygame)

    # Limit to 60 frames per second
    clock.tick(FPS)

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
pygame.quit()
