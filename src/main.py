import pygame

from src.exceptions.grid_exceptions import OutOfGridBoundsError
from src.exceptions.snake_exceptions import SnakeTwistedError, SnakeHeadBeatenError
from src.grid.grid import BasicGrid
from src.snake import UnclePy, Directions

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

CELLS_IN_ROW = 60
CELL_WIDTH = 6
CELL_HEIGHT = 6
MARGIN = 1

FPS = 60


def main():
    grid = BasicGrid(
        grid_info=(CELL_WIDTH, CELL_HEIGHT, MARGIN),
        grid_bounds=(CELLS_IN_ROW, CELLS_IN_ROW)
    )

    pygame.init()

    window_size = grid.screen_size()
    screen = pygame.display.set_mode(window_size)
    pygame.display.set_caption('UnclePy')

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()
    speed = 1
    snake = UnclePy(grid, RED, FPS, speed)

    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT and snake.direction != Directions.LEFT:
                    snake.direction = Directions.RIGHT
                if event.key == pygame.K_LEFT and snake.direction != Directions.RIGHT:
                    snake.direction = Directions.LEFT
                if event.key == pygame.K_UP and snake.direction != Directions.DOWN:
                    snake.direction = Directions.UP
                if event.key == pygame.K_DOWN and snake.direction != Directions.UP:
                    snake.direction = Directions.DOWN
        try:
            snake.move()
        except (OutOfGridBoundsError, SnakeTwistedError, SnakeHeadBeatenError):
            grid.clear()
            del grid.structures[-1]
            snake = UnclePy(grid, RED, FPS, speed)

        # Draw the grid
        grid.draw(screen, pygame)

        # Limit to 60 frames per second
        clock.tick(60)

        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

    # Be IDLE friendly. If you forget this line, the program will 'hang'
    # on exit.
    pygame.quit()


if __name__ == "__main__":
    main()
