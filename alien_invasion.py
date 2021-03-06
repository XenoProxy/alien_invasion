import sys
import pygame

from ship import Ship
from settings import Settings


class AlienInvasion:
    """Class for managing game resources and behavior"""
    def __init__(self):
        """Game init and creating of the game resources"""
        pygame.init()
        self.settings = Settings()
        #  Полноэкранный режим
        # self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        # self.settings.screen_width = self.screen.get_rect().width
        # self.settings.screen_height = self.screen.get_rect().height
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_hight)
        )
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)

    def run_game(self):
        """Запуск основного цикла игры."""
        while True:  # Отслеживание событий клавиатуры и мыши.
            self._chech_events()
            self.ship.update()
            self._update_screen()

    def _chech_events(self):
        """Обрабатывает нажатия клавиш и события мыши."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Реагирует на нажатие клавиш."""
        if event.key == pygame.K_LEFT:  # Переместить корабль влево.
            self.ship.moving_left = True
        elif event.key == pygame.K_RIGHT:  # Переместить корабль вправо.
            self.ship.moving_right = True
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        """Реагирует на отпускание клавиш."""
        if event.key == pygame.K_LEFT:  # Переместить корабль влево.
            self.ship.moving_left = False
        elif event.key == pygame.K_RIGHT:  # Переместить корабль вправо.
            self.ship.moving_right = False

    def _update_screen(self):
        """Обновляет изображения на экране и отображает новый экран."""
        self.screen.fill(
            self.settings.bg_color
            )  # При каждом проходе цикла перерисовывается экран
        self.ship.blitme()
        pygame.display.flip()  # Отображение последнего прорисованного экрана.


if __name__ == '__main__':  # Создание экземпляра и запуск игры
    ai = AlienInvasion()
    ai.run_game()

