import pygame

from src.config import CELL_WIDTH, CELL_HEIGHT, MARGIN, CELLS_IN_ROW, FPS
from src.exceptions.grid_exceptions import OutOfGridBoundsError
from src.exceptions.snake_exceptions import SnakeTwistedError, SnakeHeadBeatenError
from src.grid.grid import BasicGrid
from src.snake import Directions


class GameManager:
    def __init__(self):
        self.grid = BasicGrid(
            grid_info=(CELL_WIDTH, CELL_HEIGHT, MARGIN),
            grid_bounds=(CELLS_IN_ROW, CELLS_IN_ROW)
        )

        pygame.init()

        window_size = self.grid.screen_size()
        self.screen = pygame.display.set_mode(window_size)
        pygame.display.set_caption('UnclePy')

        # Used to manage how fast the screen updates
        self.clock = pygame.time.Clock()

    def dispose(self):
        self.grid.clear()

        self.snake = self.grid.add_snake(5, (0, 100, 100), 5)
        self.grid.add_food((100, 100, 0), 3)
        self.grid.add_food((100, 100, 0), 3)

    def start(self):
        frame_counter = 0
        speed = 60

        self.dispose()
        self.grid.draw(self.screen, pygame)
        pygame.display.flip()

        done = False
        while not done:
            if frame_counter < (FPS - 1) / speed:
                frame_counter += 1
                continue

            frame_counter = 0

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT and self.snake.direction != Directions.LEFT:
                        self.snake.direction = Directions.RIGHT
                    if event.key == pygame.K_LEFT and self.snake.direction != Directions.RIGHT:
                        self.snake.direction = Directions.LEFT
                    if event.key == pygame.K_UP and self.snake.direction != Directions.DOWN:
                        self.snake.direction = Directions.UP
                    if event.key == pygame.K_DOWN and self.snake.direction != Directions.UP:
                        self.snake.direction = Directions.DOWN
            try:
                self.snake.move()
            except (OutOfGridBoundsError, SnakeTwistedError, SnakeHeadBeatenError):
                print(f'Total scores {self.snake.scores}')
                break

            self.grid.draw(self.screen, pygame)

            self.clock.tick(60)
            pygame.display.flip()


