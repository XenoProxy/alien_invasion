import sys
import pygame


class AlienInvasion:
    """Class for managing game resources and behavior"""

    def __init__(self):
        """Game init and creating of the game resources"""
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        """Run the game cycle"""
        while True:  # Отслеживание событий клавиатуры и мыши.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            pygame.display.flip()  # Отображение последнего прорисованного экрана.


if __name__ == '__main__':  # Создание экземпляра и запуск игры
    ai = AlienInvasion()
    ai.run_game()

