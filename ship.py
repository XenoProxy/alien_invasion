import pygame


class Ship:
    """Класс для управления кораблем."""
    def __init__(self, ai_game):
        """Инициализирует корабль и задает его начальную позицию."""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings

        img = pygame.image.load('images/ship.bmp')  # Загружает изображение корабля и получает прямоугольник.
        self.image = pygame.transform.scale(img, (70, 120))
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom  # Каждый новый корабль появляется у нижнего края экрана.
        # Сохранение вещественной координаты центра корабля.
        self.x = float(self.rect.x)
        # Флаги перемещения.
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Обновляет позицию корабля с учетом флага."""
        # Обновляется атрибут x, не rect.
        if self.moving_right:
            self.x += self.settings.ship_speed
        elif self.moving_left:
            self.x -= self.settings.ship_speed

        # Обновление атрибута rect на основании self.x.
        self.rect.x = self.x

    def blitme(self):
        """Рисует корабль в текущей позиции."""
        self.screen.blit(self.image, self.rect)
