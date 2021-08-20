import sys
import pygame


class AlienInvasion:
    """Class for managing game resources and behavior"""
    def __init__(self):
        """Game init and creating of the game resources"""
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")
        self.bg_color = (230, 230, 230)  # Назначение цвета фона

    def run_game(self):
        """Run the game cycle"""
        while True:  # Отслеживание событий клавиатуры и мыши.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.screen.fill(self.bg_color)  # При каждом проходе цикла перерисовывается экран
            pygame.display.flip()  # Отображение последнего прорисованного экрана.


if __name__ == '__main__':  # Создание экземпляра и запуск игры
    ai = AlienInvasion()
    ai.run_game()

