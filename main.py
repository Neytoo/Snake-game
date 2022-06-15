import pygame
from enum import Enum, auto
from dataclasses import dataclass

WIDTH = 800
HEIGHT = 600
BLOCK_SIZE = 20
BLOCK_STEP = 5

WHITE = (255, 255, 255)
YELLOW = (255, 255, 102)
BLACK = (0, 0, 0)
RED = (213, 50, 80)
GREEN = (0, 255, 0)
BLUE = (50, 153, 213)

pygame.init()
pygame.display.set_caption("Snake game")


class Directions(Enum):
    UP = auto()
    DOWN = auto()
    LEFT = auto()
    RIGHT = auto()


@dataclass(frozen=True)
class Snake:
    x: int = 0
    y: int = 0
    block_with: int = BLOCK_SIZE
    block_height: int = BLOCK_SIZE


class SnakeGame:
    def __init__(self):
        self._game_init()

    def _game_init(self):
        self.game_over = False
        self.clock = pygame.time.Clock()
        self.snake: list = [Snake]
        self.wnd = pygame.display.set_mode((WIDTH, HEIGHT))
        self.wnd.fill(BLUE)
        pygame.display.flip()

        score_font = pygame.font.SysFont(name="Tahoma", size=12)

        # value = score_font.render("Your score: 0", True, BLACK)
        # wnd.blit(value, [10, 10])

        #

        self._game_loop()

    def _game_loop(self) -> None:
        while not self.game_over:
            for event in pygame.event.get():
                self._event_manager(event)

            self._draw_snake()
            self._snake_step()


    def snake_step(self) -> None:
        if self.direction == Directions.RIGHT:


    def _event_manager(self, event: pygame.event) -> None:
        if event.type == pygame.QUIT:
            self._quit_game()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self._quit_game()
            elif event.key == pygame.K_UP:
                self._move(direction=Directions.UP)
            elif event.key == pygame.K_LEFT:
                self._move(direction=Directions.LEFT)
            elif event.key == pygame.K_DOWN:
                self._move(direction=Directions.DOWN)
            elif event.key == pygame.K_RIGHT:
                self._move(direction=Directions.RIGHT)

    def _draw_snake(self):
        for idx, snake_block in enumerate(self.snake):
            snake_config = (
                pygame.Rect(
                    snake_block.x,
                    snake_block.y,
                    snake_block.block_with,
                    snake_block.block_height,
                ),
            )

            pygame.draw.rect(self.wnd, GREEN if idx != 0 else YELLOW, snake_config)
            pygame.display.flip()

    def _quit_game(self) -> None:
        self.game_over = True
        self._game_end()

    @staticmethod
    def _game_end() -> None:
        pygame.quit()
        quit()

    def _move(self, direction: Directions):
        self.direction = direction


if __name__ == "__main__":
    SnakeGame()
