class Settings():  # класс для хранения настроек игры
    def __init__(self):
        self.screen_width = 1920
        self.screen_height = 1080
        self.ship_limit = 3

        self.bullet_width = 7
        self.bullet_height = 17
        self.bullet_color = 255, 36, 0
        self.bullets_allowed = 3

        self.fleet_drop_speed = 10

        self.speedup_scale = 1.2
        self.score_scale = 1.2
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):  # Настройки, изменяющиеся в ходе игры
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 2
        self.alien_speed_factor = 1
        self.fleet_direction = 1  # движение вправо 
        self.alien_points = 50
        self.static_points = 50

    def increase_speed(self):  # увеличивает скорость
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
