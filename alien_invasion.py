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
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_hight)
        )
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)

    def run_game(self):
        """Run the game cycle"""
        while True:  # Отслеживание событий клавиатуры и мыши.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.screen.fill(self.settings.bg_color)  # При каждом проходе цикла перерисовывается экран
            self.ship.blitme()
            pygame.display.flip()  # Отображение последнего прорисованного экрана.


if __name__ == '__main__':  # Создание экземпляра и запуск игры
    ai = AlienInvasion()
    ai.run_game()

