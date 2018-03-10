class SnakeException(Exception):
    pass


class SpeedIsNotPositiveException(SnakeException):
    pass


class LongDisposeLengthException(SnakeException):
    pass


class SnakeTwistedError(SnakeException):
    pass


class SnakeHeadBeatenError(SnakeException):
    pass


class SnakeBackwardMoveError(SnakeException):
    pass
