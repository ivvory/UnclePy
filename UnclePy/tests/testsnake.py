import unittest

from exceptions.direction import IncorrectMoveDirection
from snake import UnclePy
from basicgrid import BasicGrid
from exceptions.twist import SnakeTwistedError
from exceptions.bounds import OutOfCellsBoundError


class TestUnclePy(unittest.TestCase):
    def test_move(self):
        grid = BasicGrid(20, 20, 8, 10)
        color = (255, 0, 0)
        fps = 2
        snake = UnclePy(grid, color, fps)

        def move(direction):
            snake.direction = direction
            for i in range(fps):
                snake.move()

        try:
            move('Incorrect direction')
        except IncorrectMoveDirection:
            pass  # All right
        else:
            self.fail('Method does not fail when direction is incorrect')

        try:
            move('UP')
        except OutOfCellsBoundError:
            pass  # All right
        else:
            self.fail('Method does not fail when snake is out of grid')

        old_head = list(snake.get_head())

        sequence_of_directions = ['RIGHT', 'DOWN', 'DOWN', 'LEFT', 'UP']
        [move(direction) for direction in sequence_of_directions]

        new_head = list(snake.get_head())
        old_head[1] += 1
        self.assertListEqual(new_head, old_head)

        try:
            move('UP')
        except SnakeTwistedError:
            pass  # All right
        else:
            self.fail('Method does not fail when snake is twisted')

    def test_get_available_cells(self):
        grid = BasicGrid(20, 20, 8, 10)
        color = (255, 0, 0)
        fps = 60
        snake = UnclePy(grid, color, fps)

        snake.occupy_cell(0, 1)
        snake.occupy_cell(1, 0)
        self.assertEqual(set(), snake.get_available_cells(0, 0))

        self.assertEqual({(2, 1), (1, 2), (2, 3), (3, 2)}, snake.get_available_cells(2, 2))
        self.assertEqual({(7, 6), (6, 7)}, snake.get_available_cells(7, 7))

    def test_occupy_cell(self):
        grid = BasicGrid(20, 20, 8, 10)
        color = (255, 0, 0)
        fps = 60
        snake = UnclePy(grid, color, fps)

        self.assertTrue(snake.occupy_cell(1, 1))
        self.assertTrue(snake.occupy_cell(1, 1))
        self.assertFalse(snake.occupy_cell(-1, 1))
