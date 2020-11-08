import pygame
from pygame.sprite import Sprite

class Alien(Sprite):  # Класс для корабля пришельца
    def __init__(self, ai_settings, screen):
    	super(Alien, self).__init__()  # Инициализируем корабль и задаем его начальные коор-ды
    	self.screen = screen
    	self.ai_settings = ai_settings

    	self.image = pygame.image.load('C:/Users/Edgar/Desktop/alien_invasion_game/images/enemy_ship.bmp')
    	self.rect = self.image.get_rect()  # Загрузка изображдения пришельца

    	self.rect.x = self.rect.width  # корабль появляется в левом верхнем угре экрана
    	self.rect.y = self.rect.height

    	self.x = float(self.rect.x)

    def blitme(self):  # Выводит пришельца в текущем положении
    	self.screen.blit(self.image, self.rect)

    def check_edges(self):  # возращает True, если пришелец находятся у края экрана
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
        	return True
        if self.rect.left <= 0:
        	return True


    def update(self):
    	self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
    	self.rect.x = self.x