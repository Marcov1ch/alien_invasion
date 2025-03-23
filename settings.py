class Settings():
    """Класс для хранения настроект игры Alien Invasion."""
    def __init__(self):
        """Инициализирует настройки игры."""
        # Параметры экрана
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 0, 139)
        # Настройки корабля
        self.ship_speed = 1.5
        # Параметры снаряда
        self.bullet_speed = 1
        self.bullet_width = 5
        self.bullet_height = 20
        self.bullet_color = (255, 60, 60)
